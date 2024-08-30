from datetime import datetime, timezone
import json
import requests



#############SOME FUNCTIONS


# we use this function to print every questions of the form 
def print_question(question):

    print(f"Question: {question['text']}")
    if question['type'] == 'boolean':
        return input("Answer (yes/no): ").strip().lower() in ['yes', 'y']
    elif question['type'] == 'choice':
        print("Options:")
        for idx, option in enumerate(question['answerOption']):
            print(f"{idx + 1}. {option['valueString']}")
        choice = int(input("Choose an option number: ")) - 1
        return question['answerOption'][choice]['valueString']
    elif question['type'] == 'string':
        return input("Type your answer: ")
    elif question['type'] == 'group':
        return {item['linkId']: print_question(item) for item in question['item']}
    else:
        print("Unsupported question type.")
        return None
    

#we use this function to save the data in json format in our laptop
def save_to_file(data, filename) : 
            with open(filename, 'w') as outfile : 
                json.dump(data, outfile, indent = 4)
            print (f"Data saved to {filename}")





# if you add the duo code in each question of your form, you can get it in the responses by this function
def get_duo_code(item):
    if 'extension' in item:
        for ext in item['extension']:
            if ext.get('url') == "http://example.org/fhir/StructureDefinition/duo-code":
                return ext['valueCoding']['code']
    return None




#with this function you can send the data to hapi fhir server
def send_to_hapi_server(resource, resource_type):
    hapi_base_url = "http://hapi.fhir.org/baseR4"  # Use this for the public test server
    
    headers = {
        'Content-Type': 'application/fhir+json',
        'Accept': 'application/fhir+json'
    }
    


    try : 
        response = requests.post(f"{hapi_base_url}/{resource_type}", json=resource, headers=headers)
        response.raise_for_status()  # This will raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Error sending {resource_type} to HAPI server: {e}")
        return None



    if response.status_code == 201:
        print(f"{resource_type} successfully sent to HAPI server. ID: {response.json()['id']}")
        return response.json()['id']
    else:
        print(f"Failed to send {resource_type}. Status code: {response.status_code}")
        print(f"Response: {response.text}")








##############RESOURCES




# we create a fhir format of the responses collected using the QuestionnaireResponse ressource  
def create_questionnaire_response(questionnaire, responses, questionnaire_response_id):
    questionnaire_response = {
        "resourceType": "QuestionnaireResponse",
        "id": questionnaire_response_id,
        "questionnaire": questionnaire['url'],
        "status": "completed",
        "authored": datetime.now(timezone.utc).isoformat(),
        "item": []
    }

    def add_item(item, response):
        response_item = {
            "linkId": item['linkId'],
            "text": item['text']
        }

        if 'extension' in item:
            response_item['extension'] = item['extension']

        if item['type'] == 'group':
            response_item['item'] = [add_item(sub_item, response.get(sub_item['linkId'], {})) for sub_item in item.get('item', [])]
        else:
            if response is not None:  # Vérifier si une réponse existe
                if item['type'] == 'boolean':
                    response_item['answer'] = [{"valueBoolean": response}]
                else:
                    response_item['answer'] = [{"valueString": str(response)}]

        # Ajouter le code DUO dans notre réponse
        duo_code = get_duo_code(item)
        if duo_code:
            if 'extension' not in response_item:
                response_item['extension'] = []
            response_item['extension'].append({
                "url": "http://example.org/fhir/StructureDefinition/duo-code",
                "valueCoding": {"code": duo_code}
            })

        return response_item

    for item in questionnaire['item']:
        questionnaire_response['item'].append(add_item(item, responses.get(item['linkId'])))

    return questionnaire_response



#we create practitioner resource in fhir format
def create_practitioner_resource() : 
     
    practitioner_id = input("Enter the practitioner's ID: ")
    practitioner_name = input("Enter the practitioner's full name: ")

    practitioner = {
        "resourceType": "Practitioner",
        "id": practitioner_id,
        "name": [
            {
                "use": "official",
                "text": practitioner_name
            }
        ],
        "active": True
    }

    return practitioner




def create_patient_resource(unique_id, responses, server_practitioner_id ):
     
    birth_date = input("Enter the birth date: ")
    patient_phone = input("Enter patient phone number: ")
    patient_email = input("Enter your mail adress: ")
    gender = input("Enter patient gender (male/female/other): ").lower()

    # a reminder , this family and given name are thoses of the parents . 
    # you should search for the child name . add it to the questions in the form and extract it

    def find_response(linkId, subLinkId=None):
        if linkId in responses:
            if isinstance(responses[linkId], dict) and subLinkId:
                return responses[linkId].get(subLinkId)
            return responses[linkId]
        return None

    family_name = find_response('2', '2.1')
    given_name = find_response('2', '2.2')

    

    patient = {
        "resourceType": "Patient",
         "id": unique_id,
        "meta": {
            "profile": ["http://hl7.org/fhir/StructureDefinition/Patient"]
        },
        "active": True,
        "name": [
            {
                "use": "official",
                "family": family_name,
                "given": [given_name]
            }
        ],
        "telecom": [
            {
                "system": "email",
                "value": patient_email
            },
            {
                "system": "phone",
                "value": patient_phone
            }
        ],
        "gender": gender,
        "birthDate": birth_date,
        "generalPractitioner": [
            {
                "reference": f"Practitioner/{server_practitioner_id}",
                
            }
        ]
    }

    
    return patient

from datetime import datetime, timezone

#method 1

def create_consent_resource(unique_id, server_practitioner_id, responses):
    

    consent = {
        "resourceType": "Consent",
        "id": unique_id,
        "status": "active",
        "scope": {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/consentscope",
                    "code": "research",
                    "display": "Research"
                }
            ]
        },
        "category": [
            {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/consentcategorycodes",
                        "code": "rsc",
                        "display": "Research Study Consent"
                    }
                ]
            }
        ],
        "patient": {
            "reference": f"Patient/{int(server_practitioner_id)+ 1}"
        },
        "dateTime": datetime.now(timezone.utc).isoformat(),
        "organization": [
            {
                "reference": "Organization/example"
            }
        ],
        #there is a problem here, you can not send the source reference as a questionnaire response in FHIR
        #you may find another way to linked it, as in extension for exemple
        #"sourceReference": {
           # "reference": f"QuestionnaireResponse/{int(server_practitioner_id)-1}"
       # },
        "provision": {
            "type": "permit",
            "period": {
                "start": datetime.now(timezone.utc).isoformat()
            },
            "data" : [],
            
        }
    }


                     # Mapping des questions aux codes DUO
    duo_mapping = {
        "4.1": "GRU",
        "4.2": "HMB",
        "4.6": "RS_PD",
        "4.7": "RS_POP",
        "4.9": "NCTRL",
        # Ajoutez d'autres mappings selon votre questionnaire
    }

    duo_codes = {}

    for linkId, response in responses.items():
        if linkId in duo_mapping:
            duo_codes[duo_mapping[linkId]] = str(response).lower()

    consent["provision"]["data"].append( [f"{code} = {value}" for code, value in duo_codes.items()])
        

    return consent



#method 2 



def create_consent_resource_withprovision(unique_id, server_practitioner_id, responses ):


    
    consent = {
        "resourceType": "Consent",
        "id": unique_id,
        "status": "active",
        "scope": {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/consentscope",
                    "code": "research",
                    "display": "Research"
                }
            ]
        },
        "category": [
            {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/consentcategorycodes",
                        "code": "dna",
                        "display": "DNA analysis"
                    }
                ]
            }
        ],
        "patient": {
            "reference": f"Patient/{int(server_practitioner_id) + 1}"
        
        },

        "dateTime": datetime.now(timezone.utc).isoformat(),
        "organization": [
            {
                "reference": "Organization/example"  
            }
        ],
        #"sourceReference": {
        #    "reference": f"QuestionnaireResponse/{int(server_practitioner_id) -1}"
       # },
        "provision": [
           
        ]
        }
       
    
                   # Mapping des questions aux codes DUO
    duo_mapping = {
        "4.1": "GRU",
        "4.2": "HMB",
        "4.6": "RS_PD",
        "4.7": "RS_POP",
        "4.9": "NCTRL",
        # Ajoutez d'autres mappings selon votre questionnaire
    }

    duo_codes = {}

    for linkId, response in responses.items():
        if linkId in duo_mapping:
            duo_codes[duo_mapping[linkId]] = str(response).lower()

   


#### this section helps to add in the provision 

    for duo_code, value in duo_codes.items():
        provision = {
        "type": "permit" if value == "true" else "deny",
        "purpose": [
            {
                "system": "http://purl.obolibrary.org/obo/duo.owl",
                "code": duo_code
            }
        ]
    }

        consent["provision"].append(provision)


    return consent




#method 3
#by adding extensions with the duo code and the answer value in my consent resource 
#with 2 functions 


def create_consent_provision_extension(responses):

    duo_mapping = {
    
        4.1: {"code": "GRU", "display": "Genetic Research Use"},
        4.2: {"code": "HMB", "display": "Health Monitoring Biomarkers"},
        4.6: {"code": "RS_PD", "display": "Research Study - Parkinson's Disease"},
        4.7: {"code": "RS_POP", "display": "Research Study - Population-Based"},
        4.9: {"code": "NCTRL", "display": "No Control"}
    }
                   
    
    consent_provision = []

    for link_id, answer in responses.items():
      
        if link_id in responses:
            duo_code = duo_mapping[link_id]["code"]
            display = duo_mapping[link_id]["display"]
            
            # Handle boolean responses directly
            if isinstance(answer, bool):
                consent_provision.append({
                    "extension": [
                        {
                            "url": "http://example.org/fhir/StructureDefinition/duo-code",
                            "valueCoding": {
                                "system": "http://purl.obolibrary.org/obo/duo.owl",
                                "code": duo_code,
                                "display": display
                            }
                        }
                    ],
                    "valueBoolean": answer
                })

            # Handle nested responses (like for linkId "4" with sub-items)
            elif isinstance(answer, dict):
                for sub_link_id, sub_answer in answer.items():
                    if sub_link_id in responses:
                        sub_duo_code = duo_mapping[sub_link_id]["code"]
                        sub_display = duo_mapping[sub_link_id]["display"]
                        consent_provision.append({
                            "extension": [
                                {
                                    "url": "http://example.org/fhir/StructureDefinition/duo-code",
                                    "valueCoding": {
                                        "system": "http://purl.obolibrary.org/obo/duo.owl",
                                        "code": sub_duo_code,
                                        "display": sub_display
                                    }
                                }
                            ],
                            "valueBoolean": sub_answer if isinstance(sub_answer, bool) else None,
                            "valueString": sub_answer if isinstance(sub_answer, str) else None
                        })
            else:
                # Handle other types (like strings or dates)
                consent_provision.append({
                    "extension": [
                        {
                            "url": "http://example.org/fhir/StructureDefinition/duo-code",
                            "valueCoding": {
                                "system": "http://purl.obolibrary.org/obo/duo.owl",
                                "code": duo_code,
                                "display": display
                            }
                        }
                    ],
                    "valueString": answer if isinstance(answer, str) else None
                })


    
    return consent_provision


def integrate_provision_ext(consent, responses):
    provision_data = create_consent_provision_extension(responses)
    
   
    consent["provision"] = {
        "type": "permit",
        "period": {
            "start": datetime.now(timezone.utc).isoformat()
        },
        "provision": provision_data
    }
    
    return consent






















