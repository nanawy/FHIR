


"""
Note on resource submission order:
1. We first send the QuestionnaireResponse to the server.
2. Then, we send the Practitioner resource.
3. Finally, we send the Patient resource, which contains the IDs of the previously sent resources.

There's also a complete_questionnaire.json file that contains all the questions of the form.
"""





from datetime import datetime, timezone
import json
import uuid
import hashlib
import requests

"""
def create_unique_id(email) : 
     # Generate a hash of the email address for a more secure ID
    hashed_email = hashlib.sha256(email.encode('utf-8')).hexdigest()
    return hashed_email[:16]  # Truncate to a shorter ID
"""


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
        return input("Answer: ")
    elif question['type'] == 'group':
        return {item['linkId']: print_question(item) for item in question['item']}
    else:
        print("Unsupported question type.")
        return None

def save_to_file(data, filename) : 
            with open(filename, 'w') as outfile : 
                json.dump(data, outfile, indent = 4)
            print (f"Data saved to {filename}")


def main():
    # Spécifiez le chemin du fichier JSON
    file_path = 'complete_questionnaire.json'

    try:
        # Ouvrir et lire le fichier JSON
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Afficher les questions et obtenir les réponses
        responses = {}
        for item in data['item']:
            response = print_question(item)
            responses[item['linkId']] = response
        
        # Afficher les réponses collectées
        print("\nCollected Responses:")
        for linkId, response in responses.items():
            print(f"LinkId: {linkId}, Response: {response}")


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
        
       # Generate IDs
        #complete_questionnaire_id = create_unique_id(patient_email)
        #questionnaire_response_id = create_unique_id(patient_email)
        #['id'] = complete_questionnaire_id
        #questionnaire_response['id'] = questionnaire_response_id

 # Créer la ressource Practitioner
        practitioner_resource = create_practitioner_resource(practitioner_id, practitioner_name)
    

# i added this 
        #patient_resource = create_patient_resource(patient_email, unique_id, questionnaire_response, questionnaire_response_id, practitioner_id, birth_date, practitioner_name )
    
# update the questionnaire and questionnaire_response with their new IDs (y a de la repetition que je dois supprimer)
 



         # Save files with consistent naming
        #save_to_file(data, f'complete_questionnaire_{unique_id}.json')
        save_to_file(questionnaire_response, f'questionnaire_response_{questionnaire_response_id}.json')
        #save_to_file(practitioner_resource, f'practitioner_{practitioner_id}.json')
        #save_to_file(patient_resource, f'patient_{unique_id}.json')

          #send resources to HAPI server
        send_to_hapi_server(questionnaire_response, "QuestionnaireResponse")
        #send_to_hapi_server(practitioner_resource, "Practitioner")
        #send_to_hapi_server(patient_resource, "Patient")


        # Envoyer le Practitioner et obtenir l'ID attribué par le serveur
        server_practitioner_id = send_to_hapi_server(practitioner_resource, "Practitioner")
        print(f"Server Practitioner ID: {server_practitioner_id}")
        if server_practitioner_id:
        # Créer et envoyer le Patient avec l'ID correct du Practitioner
            patient_resource = create_patient_resource(patient_email, unique_id, questionnaire_response, questionnaire_response_id, server_practitioner_id, birth_date, practitioner_name)
            save_to_file(patient_resource, f'patient_{unique_id}.json')
            send_to_hapi_server(patient_resource, "Patient")
        else:
            print("Failed to create Practitioner, cannot proceed with Patient creation.")

    except FileNotFoundError:
        print(f"Le fichier {file_path} est introuvable.")
    except json.JSONDecodeError:
        print("Erreur de décodage JSON.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")





"""
          # Save the updated questionnaire
        with open('complete_questionnaire.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)

          # Save the updated questionnaire_response
        with open('questionnaire_response.json', 'w') as outfile:
            json.dump(questionnaire_response, outfile, indent=4)

          # Save the patient resource
        with open('patient_with_questionnaire.json', 'w') as outfile:
            json.dump(patient_resource, outfile, indent=4)


        output_file_path2 = 'patient_with_questionnaire.json'
        with open(output_file_path2, 'w') as outfile:
            json.dump(patient_resource, outfile, indent=4)

        print(f"Patient resource with QuestionnaireResponse has been saved to {output_file_path2}")

        # Sauvegarder le QuestionnaireResponse dans un fichier JSON
        output_file_path = 'questionnaire_response.json'
        with open(output_file_path, 'w') as outfile:
            json.dump(questionnaire_response, outfile, indent=4)
        
        print(f"QuestionnaireResponse has been saved to {output_file_path}")


    except FileNotFoundError:
        print(f"Le fichier {file_path} est introuvable.")
    except json.JSONDecodeError:
        print("Erreur de décodage JSON.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")"""

   

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

    def add_item(item, response):
        response_item = {
            "linkId": item['linkId'],
            "text": item['text'],
            "answer": []  # Add 'answer' key for group questions
        }
        if item['type'] == 'group':
            response_item['item'] = [add_item(sub_item, response[sub_item['linkId']]) for sub_item in item['item']]
        else:
            if item['type'] == 'boolean':
                response_item['answer'] = [{"valueBoolean": response}]
            else:
                response_item['answer'] = [{"valueString": response}]
        return response_item

    for item in questionnaire['item']:
        questionnaire_response['item'].append(add_item(item, responses[item['linkId']]))

    return questionnaire_response


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


def create_patient_resource(patient_email, unique_id, questionnaire_response, questionnaire_response_id, practitioner_id, birth_date, practitioner_name):


    # Generate IDs
    #complete_questionnaire_id = str(uuid.uuid4())
    #questionnaire_response_id = str(uuid.uuid4())

    # Generate unique IDs based on email
    #questionnaire_response_id = complete_questionnaire_id = create_unique_id(patient_email)
    
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
    patient_signature = input("Enter patient signature: ") 
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











"""
    for item in questionnaire_response['item'] : 
        answer = item.get ('answer', [] )
        if answer : 
        
            value = answer [0]. get9
        extension = {
            "url": f"http://example.org/fhir/StructureDefinition/questionnaire-{item['linkId']}",
            "valueString": str(item['answer'][0].get('valueBoolean', item['answer'][0].get('valueString', '')))
        }
        patient['extension'].append(extension)

     # Add a reference to the QuestionnaireResponse
    patient['questionnaireResponse'] = [
        {
            "reference": f"QuestionnaireResponse/{questionnaire_response['id']}"
        }
    ]


    return patient"""



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

if __name__ == '__main__':
    main()


