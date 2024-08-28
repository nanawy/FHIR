
- je dois rajouter plus de details avec le code (finir jeudi matin) 

# PROJECT 

This work is part of the Gene Guardian project, previously named Dynamic Consent
Protocol, which suggests a perfect framework that puts the individual in the middle of
the decision making.

As we know the use of genomic information in medical treatments and disease risk
management must balance personal and societal benefits against risks to individuals
contributing their data.

Trust in the professional and ethical handling of genomic data is crucial for
participants to consent to the use of their data.

figure 1 : diagram of the medical application : 

![image](https://github.com/user-attachments/assets/4da8674e-5d39-4aa0-b89d-244d0da2569c)


# FHIR 

my role is : Create a form using FHIR resources (& adapting it to our needs)
This form is a mixture of forms of hospitals and a form already created by the team
and later on interacting with a server.

- What is HL7 FHIR ?
  
It was created by the standards development organization Health Level 7 (HL7). It
was designed to enable health data to be quickly and efficiently exchanged.
FHIR is a set of modular components called "Resources." These fields include basic
elements like identifiers, metadata, and attributes relevant to the type of resource.

figure 2 : example of a resource : 


![image](https://github.com/user-attachments/assets/e6864e9c-c89f-4ff7-a294-8ea47dcfdd48)



- HL7 FHIR has evolved through four releases since its initial presentation in
May 2012. It has grown from a true draft standard with 49 Resources to its
current 145.

- In that time, the standard has improved and changed to meet the needs of
the health information technology community


# my work 

## 
##



<img width="667" alt="image" src="https://github.com/user-attachments/assets/b6fd16d2-04cc-43cc-8796-c2d7ac1e97f0">










<img width="779" alt="image" src="https://github.com/user-attachments/assets/ddc9a47c-935e-4a7d-8f9f-fd0a7014dc22">








note : 
- the pink color represent the resources 
- the paralleogram contains the function 


  
1. <mark> def print_question(question)   <mark> :

    - It displays the questions of the questionnaire with an input for the patient's entry, and it encompasses all types of questions.

   
3.  <mark>  def create_questionnaire_response(questionnaire, responses, questionnaire_response_id) <mark> : 

 - we create the questionnaire response resource.
 - by using an add_item() function , we take the answers of each item that has been give by answering the questionnaire.
   
   
5. <mark> def create_patient_resource(patient_email, unique_id, questionnaire_response, questionnaire_response_id, practitioner_id, birth_date, practitioner_name):  <mark>

- we create the patient resource.
- we add an extension to add the reference of the questionnaireResponse's resource.



6. <mark> def create_practitioner_resource(practitioner_id, practitioner_name)  <mark>

- we create the practitioner resource.
- it contains the name and the ID of the practitioner.


7. <mark> def save_to_file(data, filename)    <mark>

- we save our data in json format on the laptop.


8. <mark>  def send_to_hapi_server(resource, resource_type) <mark> :


   - It allows us to send the resource we’ve created to the HAPI FHIR server to test the proper creation of this resource.
     
- If it has been well sent, we have a code that is displayed which is 201, with the ID of this resource in FHIR (which we will adjust in the creation of our resources to ensure the proper reference between them, because they are created and sent to the FHIR server).

- note : the resources has the ID of the server. 



10. <mark>  def create_consent_resource(unique_id, server_practitioner_id, responses, duo_codes) <mark>



    
12. <mark> def create_consent_provision(response, duo_mapping, server_practitioner_id) , def integrate_provision(consent, questionnaire_response, duo_mapping, server_practitioner_id)  <mark>




    
14. <mark>  def create_consent_resource_withprovision(unique_id, server_practitioner_id, questionnaire_response,duo_mapping ) <mark>
    




If I had time, I would make these changes : 

Create an Organization Resource, to add it in our Consent Resource with the server ID.

Better organize the items of the questionnaire, and adding the additional informations I asked for in the main_function in the questionnaire (named : complete_questionnaire.json)

In my consent ressource, I can add only one provision by consent in the FHIR server. 
(but in my laptop, I can have other provisions added. try it with another server?)

The duo code that is in some sub_items doesn’t appear. (like 4.1 : GRU, 4.2 : HMB..), i’ve got to modify how to make the questions, or the function.





