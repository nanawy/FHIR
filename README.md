
## PROJECT 

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


## FHIR 

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


### fhir code.py : 
  
1. <mark> def print_question(question)   <mark> :

    - This feature displays a question and collects the user's response.
      
- It handles different types of questions: Boolean, multiple choice, textual, and grouped.


   
3.  <mark>  def create_questionnaire_response(questionnaire, responses, questionnaire_response_id) <mark> : 

 - we create the questionnaire response resource.
   
 - by using an add_item() function , we take the answers of each item that has been given by answering the questionnaire.
   
 NB :  in your QuestionnaireResponse resource , you will find every item structured in this way : (linkID, text, answer, extension(with the duo code))
   
3. <mark> def create_patient_resource(patient_email, unique_id, questionnaire_response, questionnaire_response_id, practitioner_id, birth_date, practitioner_name):  <mark>

- we create the patient resource.
  
- we add an extension to add the reference of the questionnaireResponse's resource.

NB : I ask others questions in my function because it was missing in the questionnaire : like phone number, gender..... of the child. 

4. <mark> def create_practitioner_resource(practitioner_id, practitioner_name)  <mark>

- we create the practitioner resource.
  
- it contains the name and the ID of the practitioner.
  


5. <mark> def save_to_file(data, filename)    <mark>

- we save our data in json format on the laptop.
  
- we save the resource in our laptop with the ID given by the patient. (not the ID of the server) 


6. <mark>  def send_to_hapi_server(resource, resource_type) <mark> :


   - It allows us to send the resource we’ve created to the HAPI FHIR server to test the proper creation of this resource.
     
- If it has been well sent, we have a code that is displayed which is 201, with the ID of this resource in FHIR (which we will adjust in the creation of our resources to ensure the proper reference between them, because they are created and sent to the FHIR server).

- note : the resources has the ID of the server. (by doing some changes, i will explain in the main.py)



7. <mark>  def create_consent_resource(unique_id, server_practitioner_id, responses, duo_codes) <mark>

- method 1
  
- We create the consent resource. 

NB : - when we save it on our laptop : we will that the data.provision is filled by duo codes. unlike the HAPI server.


9.  <mark>  def create_consent_resource_withprovision(unique_id, server_practitioner_id, responses ) <mark>

- method 2
  
- we also create the consent resource ( I modify the function create_consent_resource by adding a boucle ‘for’ , to add the duo_codes in the provision.consent attributes.)

NB : we can have the provision.consent filled by the duo codes. But in HAPI server, you will have one provision by consent. unlike in the laptop, you will have all the provisions you put


    
8. <mark> def create_consent_provision_extensions(responses) /// def integrate_provision(consent, responses)  <mark>

- method 3
  
- We create the provision ( def create_consent_provision_extension(responses)
  
- and then we add it in the data.provision.consent as extensions (def integrate_provision_ext(consent, responses))


NB : the responses i filled doesnt contain the DUO code, so there is a problem to run the function. even if I created a duo mapping in the function. so? 




### main.py : 

- i run the function print_question(item)

- I print the collected answers with the linkID , response , duo code ( I can think about adding the Duo code in my dict responses ?)
  
- I create :

  1st : my resource questionnaireResponse (With the ID of HAPI  : server_practitioner_id - 1) 

  2nd >: my practitioner Resource (With the ID of HAPI  : server_practitioner_id) : ID of reference for me

  3rd : Patient resource (With the ID of HAPI  : server_practitioner_id + 1)

  4th : Consent resource ( there are 3 methods )
  


## If I had time, I would make these changes : 

- Create an Organization Resource, to add it in our Consent Resource with the server ID to link it. 

- Better organize the items of the questionnaire, and adding the additional informations I asked for in the resources function 

- some duo codes doesnt appear because they are in subitems of item. (even if i called them item too).so?




  Thank you :-)





