
## Project Overview

This work is part of the Gene Guardian project (formerly known as the Dynamic Consent Protocol), which aims to create a framework that places individuals at the center of decision-making.

Using genomic information in medical treatments and disease risk management requires balancing personal and societal benefits against the risks to individuals providing their data. Trust in the professional and ethical handling of genomic data is essential for participants to consent to its use.

figure 1 : Diagram of the medical application : 

![image](https://github.com/user-attachments/assets/4da8674e-5d39-4aa0-b89d-244d0da2569c)


## FHIR Overview

My role: Create a consent form using FHIR resources, adapting it to our needs by merging forms from hospitals and an existing team-created form. This will later be integrated with a server.

- What is HL7 FHIR ?
  
HL7 FHIR (Fast Healthcare Interoperability Resources) was developed by Health Level 7 (HL7) to enable the rapid and efficient exchange of health data. It consists of modular components called "Resources," which include basic elements like identifiers, metadata, and relevant attributes.

Figure 2: Example of a FHIR resource :


![image](https://github.com/user-attachments/assets/e6864e9c-c89f-4ff7-a294-8ea47dcfdd48)



- HL7 FHIR has evolved through four releases since its initial presentation in
May 2012. It has grown from a true draft standard with 49 Resources to its
current 145.

- In that time, the standard has improved and changed to meet the needs of
the health information technology community


# My Work 

 




<img width="667" alt="image" src="https://github.com/user-attachments/assets/b6fd16d2-04cc-43cc-8796-c2d7ac1e97f0">










<img width="779" alt="image" src="https://github.com/user-attachments/assets/ddc9a47c-935e-4a7d-8f9f-fd0a7014dc22">








note : 

- the pink color represent the resources
  
- the paralleogram contains the function 



### fhir_code.py

1. `def print_question(question)`:

   - Displays a question and collects the user's response.
     
   - Handles different types of questions: Boolean, multiple choice, textual, and grouped.

2. `def create_questionnaire_response(questionnaire, responses, questionnaire_response_id)`:
   
   - Creates the `QuestionnaireResponse` resource using answers provided in the questionnaire.
     
   - The resource is structured as: `(linkID, text, answer, extension(with DUO code))`.

3. `def create_patient_resource(patient_email, unique_id, questionnaire_response, questionnaire_response_id, practitioner_id, birth_date, practitioner_name)`:
   
   - Creates the Patient resource and adds a reference to the `QuestionnaireResponse`.
     
   - Includes additional questions such as phone number and gender.

4. `def create_practitioner_resource(practitioner_id, practitioner_name)`:
   
   - Creates the Practitioner resource, including the name and ID.

5. `def save_to_file(data, filename)`:
   
   - Saves the resource data in JSON format on the local system.

6. `def send_to_hapi_server(resource, resource_type)`:
   
   - Sends the created resource to the HAPI FHIR server for testing.
     
   - A successful send returns a 201 status code and the resource ID.
     

7. `def create_consent_resource(unique_id, server_practitioner_id, responses, duo_codes)`:
   
   - Method 1 :  for creating a Consent resource. Data provisions are filled with DUO codes on the local system.

8. `def create_consent_resource_with_provision(unique_id, server_practitioner_id, responses)`:
    
   - Method 2 for creating a Consent resource, with additional logic to add DUO codes in the provisions.

9. `def create_consent_provision_extensions(responses)`** and **`def integrate_provision(consent, responses)`:
   - Method 3 for creating and adding consent provisions with extensions.



### main.py

- Run `print_question(item)` to display and collect answers.
  
- Print answers with their `linkID`, response, and DUO code.
  
- Create and send resources to HAPI FHIR server in the following order:
  
  1. `QuestionnaireResponse`
  2. `Practitioner Resource`
  3. `Patient Resource`
  4. `Consent Resource` (using three different methods)




## Planned Improvements

- Create an Organization resource and link it in the Consent resource.
  
- Improve the organization of questionnaire items and include additional required information.
  
- Resolve missing DUO codes for sub-items.



## Results

You can view the results on the HAPI server: [HAPI FHIR Server History](https://hapi.fhir.org/history-server?serverId=home_r4&pretty=false&_summary=&limit=&since=)




Thank you! 😊










