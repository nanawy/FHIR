

"""
Note on resource submission order:
1. We first send the QuestionnaireResponse to the server.
2. Then, we send the Practitioner resource.
3. Finally, we send the Patient resource, which contains the IDs of the previously sent resources.

There's also a complete_questionnaire.json file that contains all the questions of the form.
"""





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


#with this function you can send the data to hapi fhir server
def send_to_hapi_server(resource, resource_type):
    hapi_base_url = "http://hapi.fhir.org/baseR4"  # Use this for the public test server
    
    headers = {
        'Content-Type': 'application/fhir+json',
        'Accept': 'application/fhir+json'
    }
    
    response = requests.post(f"{hapi_base_url}/{resource_type}", json=resource, headers=headers)
    
    if response.status_code == 201:
        print(f"{resource_type} successfully sent to HAPI server. ID: {response.json()['id']}")
        return response.json()['id']
    else:
        print(f"Failed to send {resource_type}. Status code: {response.status_code}")
        print(f"Response: {response.text}")



# if you add the duo code in each question of your form, you can get it in the responses by this function
def get_duo_code(item):
    if 'extension' in item:
        for ext in item['extension']:
            if ext.get('url') == "http://example.org/fhir/StructureDefinition/duo-code":
                return ext['valueCoding']['code']
    return None







def main():

   
    duo_mapping = {
    "4.1": {"code": "GRU", "display": "General Research Use"},
    "4.2": {"code": "HMB", "display": "Health/Medical/Biomedical Research"},
    "4.3": {"code": "NCTRL", "display": "Research Specific - Controlled"},
  
    }
  



    # Spécifiez le chemin du fichier JSON
    file_path = 'complete_questionnaire.json'

    try:
        # Ouvrir et lire le fichier JSON
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Afficher les questions et obtenir les réponses
        responses = {}
        duo_codes = {}
        for item in data['item']:
            response = print_question(item)
            responses[item['linkId']] = response
            duo_codes[item['linkId']] = get_duo_code(item)


        
        # Afficher les réponses collectées
        print("\nCollected Responses:")
        for linkId, response in responses.items():
            duo_code = duo_codes.get(linkId, "No DUO code")
            print(f"LinkId: {linkId}, Response: {response}, DUO Code: {duo_code}")


        #patient_id = input("Enter patient ID: ")
        patient_email = input("Enter patient email: ")
        practitioner_id = input("Enter practitioner ID: ")
        practitioner_name = input("Enter practitioner name: ")
        birth_date = input("Enter patient's birth date (YYYY-MM-DD): ")

        # Generate a single unique ID based on email
        unique_id = patient_email
        questionnaire_response_id = f"{patient_email}_response"  # Add 'response' suffix
        
        # Update the Questionnaire ID
        data['id'] = unique_id


         # Créer le QuestionnaireResponsecreate_questionnaire_response(questionnaire, responses, questionnaire_response_id):

        questionnaire_response = create_questionnaire_response(data, responses,  questionnaire_response_id)
        
    
        practitioner_resource = create_practitioner_resource(practitioner_id, practitioner_name)
    


        save_to_file(questionnaire_response, f'questionnaire_response_{questionnaire_response_id}.json')
      
          #send resources to HAPI server
        send_to_hapi_server(questionnaire_response, "QuestionnaireResponse")
       

        # Envoyer le Practitioner et obtenir l'ID attribué par le serveur
        server_practitioner_id = send_to_hapi_server(practitioner_resource, "Practitioner")
        print(f"Server Practitioner ID: {server_practitioner_id}")
        if server_practitioner_id:
        # Créer et envoyer le Patient avec l'ID correct du Practitioner
            patient_resource = create_patient_resource(patient_email, unique_id, questionnaire_response, questionnaire_response_id, server_practitioner_id, birth_date, practitioner_name)
            save_to_file(patient_resource, f'patient_{unique_id}.json')
            send_to_hapi_server(patient_resource, "Patient")
        # creer et envoyer le consent
            consent1 = create_consent_resource(unique_id, server_practitioner_id, responses, duo_mapping)
            consent = create_consent_resource_withprovision(unique_id, server_practitioner_id, responses, duo_mapping)
            save_to_file(consent,f'consent_{unique_id}.json' )
            send_to_hapi_server(consent, "Consent")

            # Integrate provision data
            #consent_final = integrate_provision(consent, responses, duo_mapping)
            


           


        else:
            print("Failed to create Practitioner, cannot proceed with Patient creation.")

    except FileNotFoundError:
        print(f"Le fichier {file_path} est introuvable.")
    except json.JSONDecodeError:
        print("Erreur de décodage JSON.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")




##############RESOURCES


# we create a fhir format of the responses collected using the QuestionnaireResponse ressource
def create_questionnaire_response(questionnaire, responses, questionnaire_response_id):

   
    questionnaire_response = {
        "resourceType": "QuestionnaireResponse",
        "id": questionnaire_response_id,  # Create a unique ID
        "questionnaire" : questionnaire['url'],
        "status": "completed",
        """
        "subject": {
            "reference": f"Patient/{unique_id}"
        },"""


        "authored": datetime.now(timezone.utc).isoformat(),
        "item": []
      }
  
         #for each item in our ressource we add the responses (including the types we mention here: boolean,str...)
    def add_item(item, response):
        response_item = {
            "linkId": item['linkId'],
           
            "text": item['text'],
            "answer": [],
            
            
              # Add 'answer' key for group questions
        }

        
        if 'extension' in item:
            response_item['extension'] = item['extension']

        if item['type'] == 'group':
            #response_item['item'] = [add_item(sub_item, response.get(sub_item['linkId'], {})) for sub_item in item.get('item', [])]
            response_item['item'] = [add_item(sub_item, response[sub_item['linkId']]) for sub_item in item['item']]
        else:
            if item['type'] == 'boolean':
                response_item['answer'] = [{"valueBoolean": response}]
            else:
                response_item['answer'] = [{"valueString": response}]

        

         # Add DUO code if present
        duo_code = get_duo_code(item)
        if duo_code:
            response_item['extension'] = [{
            "url": "http://example.org/fhir/StructureDefinition/duo-code",
            "valueCoding": {
                #"system": "http://purl.obolibrary.org/obo/duo.owl",
                "code": duo_code
            }
        }]



        print(f"Created response item: {response_item}")
        return response_item



    for item in questionnaire['item']:
        questionnaire_response['item'].append(add_item(item, responses[item['linkId']]))  






    return questionnaire_response

#we create practitioner resource in fhir format
def create_practitioner_resource(practitioner_id, practitioner_name) : 
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

#we create patient resource
def create_patient_resource(patient_email, unique_id, questionnaire_response, questionnaire_response_id, practitioner_id, birth_date, practitioner_name):

    
     # Extract family and given names from questionnaire response
    family_name = None
    given_name = None
    for item in questionnaire_response['item']:
        if item['text'] == '[Parent/Guardian Name]':
            for sub_item in item['item']:
                if sub_item['text'] == "Family Name":
                    if sub_item['answer']:
                        family_name = sub_item['answer'][0]['valueString']
                elif sub_item['text'] == "Given Name":
                    if sub_item['answer']:
                        given_name = sub_item['answer'][0]['valueString']




     # Collect additional patient information
    
    patient_phone = input("Enter patient phone number: ")
    patient_address = input("Enter patient address: ")
    #patient_signature = input("Enter patient signature: ") 
     # Consider using a digital signature mechanism
    
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
        ],"telecom": [
            {
                "system": "email",
                "value": patient_email
            },
            {
                "system": "phone",
                "value": patient_phone
            }
        ],
        "address": [
            {
                "use": "home",
                "line": [patient_address],
                # Add other address components as needed
            }
        ],
        "gender": input("Enter patient's gender (male/female/other): "),
        "birthDate": birth_date,
        "generalPractitioner": [
            {
                "reference": f"Practitioner/{practitioner_id}",
                 "display": practitioner_name,
            }
        ],
        "extension": [    
             
                    {
                        "url": "http://example.org/fhir/StructureDefinition/Patient/questionnaire-response",
                        "valueReference": {
                            "reference": f"questionnaire_response/{questionnaire_response_id}"
                        }
                    }
                ]
           
        
    }

            

    return patient




#we create consent resource with the provision (method 2 : is better one, but in FHIR server : we have only one provision added.)

def create_consent_resource_withprovision(unique_id, server_practitioner_id, questionnaire_response,duo_mapping ):

    print("Debug: QuestionnaireResponse structure:")
    print(json.dumps(questionnaire_response, indent=2))
    
    consent = {
        "resourceType": "Consent",
        "id": f"consent-{unique_id}",
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
        "sourceReference": {
            "reference": f"QuestionnaireResponse/{int(server_practitioner_id) -1}"
        },
        "provision": [
           
            #{
            #    "type": None, 
            #    "purpose": []  
           # }
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

    for linkId, response in questionnaire_response.items():
        if linkId in duo_mapping:
            duo_codes[duo_mapping[linkId]] = str(response).lower()

    # Gestion du cas spécial pour le genre
    if "4.4" in questionnaire_response and questionnaire_response["4.4"] is True:
        gender_response = questionnaire_response.get("4.5")
        if gender_response:
            if gender_response == "Male":
                duo_codes["RS_M"] = "true"
            elif gender_response == "Female":
                duo_codes["RS_F"] = "true"
            else:
                duo_codes["RS_G"] = "true"

   


#### this section helps to add in the provision data 

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
        print(f"DUO Code: {duo_code}, Value: {value}")
        print(f"Provision Added: {provision}")
      

      # Check the entire consent resource before sending
    print("Final Consent Resource: ", consent)







    return consent












#method 1 , the 3 functions underneath ( we create consent resource, and then add the provision data as an extension. some problems appear, the provisions are empty, we should maybe add an ID.. )
#the provision data is just extensions with the duo code and the value answer (we will find it the QuestionnaireResponse), so this method is just a repetition
#use method 2

def create_consent_resource(unique_id, server_practitioner_id, questionnaire_response,duo_mapping ):

    print("Debug: QuestionnaireResponse structure:")
    print(json.dumps(questionnaire_response, indent=2))
    
    consent = {
        "resourceType": "Consent",
        "id": f"consent-{unique_id}",
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
        "sourceReference": {
            "reference": f"QuestionnaireResponse/{int(server_practitioner_id) -1}"
        },
        "provision": {
            "type": "permit",
            "period": {
                "start": datetime.now(timezone.utc).isoformat()
            }, 
            "data": []
        }}
       
    
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

    for linkId, response in questionnaire_response.items():
        if linkId in duo_mapping:
            duo_codes[duo_mapping[linkId]] = str(response).lower()

    # Gestion du cas spécial pour le genre
    if "4.4" in questionnaire_response and questionnaire_response["4.4"] is True:
        gender_response = questionnaire_response.get("4.5")
        if gender_response:
            if gender_response == "Male":
                duo_codes["RS_M"] = "true"
            elif gender_response == "Female":
                duo_codes["RS_F"] = "true"
            else:
                duo_codes["RS_G"] = "true"

    # Ajout des codes DUO à la section provision.data
   
    consent["provision"]["data"].append( [f"{code} = {value}" for code, value in duo_codes.items()])



    # Print or return the consent object
    # You can comment out the following line for production use
    print(json.dumps(consent, indent=2))


    return consent







def create_consent_provision(response, duo_mapping):
    consent_provision = []

    for link_id, answer in response.items():
        if link_id in duo_mapping:
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
                    if sub_link_id in duo_mapping:
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


def integrate_provision(consent, questionnaire_response, duo_mapping, server_practitioner_id):
    provision_data = create_consent_provision(questionnaire_response, duo_mapping, server_practitioner_id)
    
    # Remplacer entièrement la section provision
    consent["provision"] = {
        "type": "permit",
        "period": {
            "start": datetime.now(timezone.utc).isoformat()
        },
        "provision": provision_data
    }
    
    return consent








if __name__ == '__main__':
    main()











