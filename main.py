from datetime import datetime, timezone
import json


from fhir_code import print_question, save_to_file, send_to_hapi_server, get_duo_code, create_consent_provision_extension,create_consent_resource,create_patient_resource,create_practitioner_resource,create_questionnaire_response,create_consent_resource_withprovision, integrate_provision_ext


######################################### main function 


def main():

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


        #this informations we dont have it in questionnaire, i asked them here. 
        #by changing the questionnaire and put these questions on it,
        #  you do not have to put it in the main anymore

        patient_email = input("Enter patient email: ")   
        # Generate a single unique ID based on email (you will need it in your own server)
        unique_id = patient_email
        questionnaire_response_id = f"{patient_email}_response"  # Added 'response' suffix
        
        # Update the Questionnaire ID
        #data['id'] = unique_id


         # Create the questionnaire response resource
        questionnaire_response = create_questionnaire_response(data, responses,  questionnaire_response_id)
        save_to_file(questionnaire_response, f'questionnaire_response_{questionnaire_response_id}.json')
        #by sending it to hapi server, the function will give you the ID of the hapi server
        send_to_hapi_server(questionnaire_response, "QuestionnaireResponse")

       
        # Create the practitioner resource (i will use the hapi server ID of the practitioner 
        # as a reference to others resources)
        #so i can link them with one another 
        # so the questionnaire response i sent first , his ID : (the hapi server ID of the practitioner - 1 )
        #etc...

        practitioner_resource = create_practitioner_resource()
        save_to_file(practitioner_resource, f"practitioner_{practitioner_resource['id']}.json")
        send_to_hapi_server(practitioner_resource, "Practitioner")

     
        #this is the ID of reference i choose
        server_practitioner_id = send_to_hapi_server(practitioner_resource, "Practitioner")

        # create patient resource 
        patient_resource = create_patient_resource( unique_id, responses, server_practitioner_id)
        save_to_file(patient_resource, f'patient_{unique_id}.json')
        send_to_hapi_server(patient_resource, "Patient")
        
        ### note : we save the file in our laptop with the true ID given in our form by the patient
        ### but when sending it to the server , we use the reference ID i choose

        # create consent resource 
        # method 1 : in our laptop we can find : in our consent.provision.data, but not in the hapi server 

        consent = create_consent_resource(unique_id, server_practitioner_id, responses)
        save_to_file(consent,f'consent_{unique_id}.json' )
        send_to_hapi_server(consent, "Consent")

        # method 2 
        # in fhir server : we have only provision with the type : permit or deny depending on the answer and the duo code
        #in our laptop : we have more than one provision 

        consent_prov = create_consent_resource_withprovision(unique_id, server_practitioner_id, responses )
        save_to_file(consent_prov,f'consent_{unique_id}.json' )
        send_to_hapi_server(consent_prov, "Consent")

        # method 3 
        # is to have the duo code and value answer in the extensions
        #consent_ext =  create_consent_provision_extension(responses)
        #save_to_file(consent_ext,f'consent_{unique_id}.json' )
        #send_to_hapi_server(consent_ext, "Consent")

        


    except FileNotFoundError:
        print(f"Le fichier {file_path} est introuvable.")
    except json.JSONDecodeError:
        print("Erreur de décodage JSON.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")



########## RUN 


if __name__ == '__main__':
    main()


