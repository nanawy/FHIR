# Summary : 



### Function print_question:

This feature displays a question and collects the user's response.
It handles different types of questions: Boolean, multiple choice, textual, and grouped.

### Function save_to_file:

Save data in JSON format to a file.

### Main function:

This is the main function that orchestrates the process.
She reads a JSON file that contains a questionnaire.
It collects the user's answers for each question.
It asks for additional information about the patient and the practitioner.
It generates unique identifiers.
It creates and saves various FHIR (QuestionnaireResponse, Practitioner, Patient) resources.
It sends these resources to a HAPI FHIR server.


### Function create_questionnaire_response:

Creates a QuestionnaireResponse FHIR resource from the collected responses.

### Function create_practitioner_resource:

Creates a Practitioner FHIR resource.

### Function create_patient_resource:

Creates a Patient FHIR resource, including the patient's information and a reference to the QuestionnaireResponse.

### Function send_to_hapi_server:

Sends a FHIR resource to the HAPI FHIR server and returns the ID assigned by the server.


