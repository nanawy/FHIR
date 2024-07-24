


 # A- FHIR FORM
 
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




Note: All parties signing the consent form must date their own signature. 

# Section 1 : Genomic Testing Details


 It is my choice for my child/person under my care to have genomic testing.

 I [Parent/Guardian Name] , understand that my child's/ the person under my care's DNA will be tested by :

 [Panel] [Exome] [Genome]

to look for changes in genes that may be associated with :

[Condition or Clinical Indication]



 ### About the Test

[ ] Genomic test results are based on current knowledge, which may change in the future 

[ ] If I change my mind, I can choose not to be told about the result 


### Potential Outcomes

[ ] This test might find a cause for the condition(s)

[ ] This test might not find a cause for the condition(s)

[ ] This result might be of 'unknown significance', which means it cannot be understood today

[ ] There is a chance that genomic testing could find other medical conditions (incidental findings)

[ ] Genomic testing may show unexpected family relationships 

[ ] Further tests or information sharing may be needed to finalize the result 



### Results

[ ] I will be told the results by a health professional

[ ] Results may have implications for the health/genetic risks for ;y child/the person under my care and family members

[ ] Results can be used to inform counselling and testing of family members, though my child's/ the person under my care's identity will not be revealed to them

[ ] Results from these tests may affect my child's /the person under my care's ability to obtain some types of insurance

[ ] The results will be available to health professionals involved in the care of my children/the person under my care

[ ] Results are confidential and may not be release without my consent unless allowed by law

[ ] The following individual can be given my child's / the person under my care's results if I am unable to be contacted 


### Contact Information : 

###### Contact Name : 

###### Contact Number :

###### Relationship to Patient : 




# Section 2 : Consent for Data Sharing

I provide consent to share my child’s/ person under my care’s sample, genomic data, and related health information for 

[ ] Data is available for future general research use 

[ ] Future is limited for health/medical/biomedical research 

[ ] Future use is limited to research involving the following disease area(s)

### Specified diseases : 

[ ] Future commercial use is prohibited 

[ ]  Future use by for-profit entities is prohibited 

[ ]  Future use for methods research (analytic/software/technology development) outside the bounds of the other specified restrictions is prohibited 

[ ]  Future use of aggregate-level data for general research purposes is prohibited 

[ ]  Future use as a control set for diseases other than those specified is prohibited 

[ ]  Future use is limited to research involving a particular gender 

[ ] Future use is limited to pediatric research 

[ ]  Future use is limited to research involving a specific population 

[ ] Future use is limited to data generated from samples collected after the following consent form date 




# Section 3 :  Consent Summary 

 I have had enough time to consider the information in this consent form and have : 

[ ] Had the opportunity to discuss genomic testing and its implication with a health professional 

[ ] Been given access to information about genomic testing 

[ ] Been able to ask questions until I am satisfied with the answers

[ ] Been offered a copy of this consent form 



### I provide consent to have genomic testing as summarized in these forms 

###### Child’s name : 

###### Date of Birth : 

###### Parent/ Guardian’s ID : 

###### Print Parent/ Guardian’s Name : 

###### Email/ Address :

###### Health Professional AHPRA ID : 

###### Health Professional Name : 

Note: All parties signing the consent form must date their own signature. 






# Section 4: Confirmation for Research Study




## I confirm that :

[ ]        I have read the information statement about the study and I understand its contents. 
 
       
[ ]        I understand what my child and I have to do in this study.  
 
      
[ ]       I understand the risks my child could face because of their involvement in this study

   
[ ]        I voluntarily consent for myself and/or my child to take part in this research study. 
 
    
[ ]      I have had an opportunity to ask questions about the study and I am satisfied with the answers I have received. 

     
[ ]      I understand that this study has been approved by a suitable Human Research Ethics Committee. I understand that the study is required to be carried out in line with the National Statement on Ethical Conduct in Human Research (2023).  

    
[ ]    I understand I will receive a copy of this Information Statement and Consent Form


 


# Section 5: Genomic Testing Consent

Please choose from the following options : I consent / I do not consent



### b. Consent for use of my child’s NBS card and diagnostic specimen        :        [ ]        /        [ ] 
Consent for researchers to access my child’s NBS card and diagnostic specimen to see
if it is possible to detect the gene change/changes in my child from the original heel prick sample taken when they were born
 
 
### c. Consent for future contact                                             : [ ]           /             [ ] 
Consent for me to be contacted again after this study for potential follow-up studies 
 
 
###### Child’s Full name                                    

###### Child’s co-signature (optional) 
###### Date 
  
 
###### Parent 1/Guardian 1 Name      

###### Parent 1/Guardian 1 Signature 
 ###### Date 
                                                                        
  
###### Parent 2/Guardian 2 Name 

###### Parent 2/Guardian 2 Signature 
###### Date                                                                     
                                                                   

 
Note: All parties signing the consent form must date their own signature. 


 
#### Please choose from the following options : Yes / No

I would like to receive a summary of the study findings :  [ ]  /     [ ]
 
 
#### If yes, please provide your contact details

Email : 

Phone number : 
 









 








# Section 06 :  Declaration by Researcher

I have explained the study to the parent(s)/guardian(s) who has signed above. I believe that they understand the purpose, extent, and possible risks of their child’s involvement in this study. 
  
  
  
###### Research Team Member Name 
  
###### Research Team Member Signature 
  
###### Date 

Note: All parties signing the consent form must date their own signature. 








# B- FHIR RESSOURCES

 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Link : https://www.hl7.org/fhir/resourcelist.html 

- the ressources are divised in different manners : Categorized, Alphabetic, R2 Layout, ...... i'll work by Maturity(the more the number of level is high, the more if change occures in ressources, it doesn't have a lot of consequences on it) 
- i'll create a board for each questions and the ressources and attributs it needed to, to create the form in the most complete way.



|                                                   Question for Section 1   :   Genomic Testing Details                                                                                                         | Ressource FHIR  | Attributs  |Description|
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|-------------------------|------------|
|  It is my choice for my child/person under my care to have genomic testing  | CanonicalResource  | url, status, version | provide url for the test, status (active,draft...), manage different versions|
|   | Patient  |  name,contact,telecom,address, gender| provide informations about the patient, birthDate |
|   | RelatedPerson  | relationship, name,  birthDate, gender | to give informations about the child   | 
|  I [Parent/Guardian Name] , understand that my child's/ the person under my care's DNA will be tested by :   | Valeur C  | Valeur D  |
|  [Panel] [Exome] [Genome]   | Observation | Valeur F  |
|    | Parameters |parameter,name, value  |   Parameters for the genomic testing operation   |
|    | Parameters |parameter,name, value  |   Parameters for the genomic testing operation   |
|  to look for changes in genes that may be associated with :   | Observation  | Valeur F  |
|  [Condition or Clinical Indication]   | Observation  | Valeur F  |
|  Genomic test results are based on current knowledge, which may change in the future  | Observation  | Valeur B  |
|  If I change my mind, I can choose not to be told about the result    | Valeur C  | Valeur D  |
|  This test might find a cause for the condition(s)      | Observation  | Valeur F  |
|  This test might not find a cause for the condition(s)   | Observation  | Valeur F  |
|  This result might be of 'unknown significance', which means it cannot be understood today   | Observation  | Valeur F  |
|  There is a chance that genomic testing could find other medical conditions (incidental findings)  | Observation| Valeur B  |
|  Genomic testing may show unexpected family relationships   | Observation  | Valeur D  |
|  Further tests or information sharing may be needed to finalize the result  | Binary  | Valeur F  |
|  I will be told the results by a health professional   | Valeur E  | Valeur F  |
|  Results may have implications for the health/genetic risks for the child/the person under my care and family members   | Valeur E  | Valeur F  |
|  Results can be used to inform counselling and testing of family members, though my child's/ the person under my care's identity will not be revealed to them | Valeur A  | Valeur B  |
|  Results from these tests may affect my child's /the person under my care's ability to obtain some types of insurance    | Valeur C  | Valeur D  |
|  The results will be available to health professionals involved in the care of my children/the person under my care      | Valeur E  | Valeur F  |
|  Results are confidential and may not be release without my consent unless allowed by law   | Valeur E  | Valeur F  |
|  The following individual can be given my child's / the person under my care's results if I am unable to be contacted  | Valeur E  | Valeur F  |
| Contact Information :  Name , Number , Relationship to Patient  | Valeur E  | Valeur F  |









|                                                   Question for Section 2   : Consent for Data Sharing                                                                                                          | Ressource FHIR  | Attributs  | Description |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|-------------------------|----------|
|  I provide consent to share my child’s/ person under my care’s sample, genomic data, and related health information for   | Binary  | Valeur B  |
|   | Observation | Valeur B  |
|  Data is available for future general research use    | Binary | Valeur D  |
|   | Observation | Valeur B  |
|  Future is limited for health/medical/biomedical research | Valeur E  | Valeur F  |
|  Future commercial use is prohibited   | Valeur E  | Valeur F  |
|  Future use for methods research (analytic/software/technology development) outside the bounds of the other specified restrictions is prohibited   | Valeur E  | Valeur F   |
|   Future use of aggregate-level data for general research purposes is prohibited   | Valeur A  | Valeur B  |
|  Future use as a control set for diseases other than those specified is prohibited    | Valeur C  | Valeur D  |
|  Future use is limited to research involving a particular gender  | Valeur E  | Valeur F  |
|  Future use is limited to pediatric research   | Valeur E  | Valeur F  |
|  Future use is limited to research involving a specific population  | Valeur E  | Valeur F   |
|  Future use is limited to data generated from samples collected after the following consent form date    | Valeur E  | Valeur F   |















|                                                   Question for Section 3   :  Consent Summary                                                                                                         | Ressource FHIR  | Attributs  | Description |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|-------------------------|----------|
|   I have had enough time to consider the information in this consent form and have :    | CanonicalResource  | name, title  | provide identifiers for different consent summaries   |
|     | OperationDefinition |  description,  status, purpose |  | 
|   Had the opportunity to discuss genomic testing and its implication with a health professional     | Valeur C  | Valeur D  |
|   Been given access to information about genomic testing  | Valeur E  | Valeur F  |
|   Been able to ask questions until I am satisfied with the answers   | Valeur E  | Valeur F  |
|   Been offered a copy of this consent form   | Binary  | Valeur F   |
|   I provide consent to have genomic testing as summarized in these forms   | Valeur C  | Valeur D  |
|  Child’s name  | Valeur E  | Valeur F  |
|  Date of Birth   | Valeur E  | Valeur F  |
|  Print Parent/ Guardian’s Name :  | Valeur E  | Valeur F   |
|  Email/ Address :     | Valeur E  | Valeur F   |
|  Health Professional AHPRA ID  | Valeur E  | Valeur F  |
|  Health Professional Name   | Valeur E  | Valeur F  |









|                                                   Question for Section 4  :   Confirmation for Research Study                                                                                                         | Ressource FHIR  | Attributs  | Description |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|-------------------------|----------|
|     I have read the information statement about the study and I understand its contents   | Location  |  name, address, hoursOfOperation, identifier, type, managingOrganization (reference)    |   location specific details    |
|     I understand what my child and I have to do in this study     | Valeur C  | Valeur D  |
|     I understand the risks my child could face because of their involvement in this study  | Valeur E  | Valeur F  |
|     I voluntarily consent for myself and/or my child to take part in this research study   | Valeur E  | Valeur F  |
|     I have had an opportunity to ask questions about the study and I am satisfied with the answers I have received  | Valeur E  | Valeur F   |
|     I understand that this study has been approved by a suitable Human Research Ethics Committee. I understand that the study is required to be carried out in line with the National Statement on Ethical Conduct in Human Research (2023)  | Valeur A  | Valeur |
|     I understand I will receive a copy of this Information Statement and Consent Form | Binary  | ContentType , data     |   or to share genomic fils (as a binary file : pdf,..)  |
| |  Practitioner      |  identifier,active,name,telecom, gender, birthDate, address,  communication, generalPractitioner,  managingOrganization,  link     |   information about the practitioner(maybe researcher) who will resend to them the form   |










|                                            Question for Section 5 :         Genomic Testing Consent                                                                                            | Ressource FHIR  | Attributs  | Description |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|-------------------------|----------|
|    Please choose from the following options : I consent, I do not consent  | Valeur A  | Valeur B  |
|     Consent for use of my child’s NBS card and diagnostic specimen | Observation | Valeur D  |
|     Consent for future contact  | Observation | Valeur F  |
|     Child’s Full name , co-signature (optional) & Date  | Observation  | Valeur F  |
|     Parent / Guardian 1 & 2 ’s Full name , co-signature (optional) & Date  | Observation  | effectiveDateTime, performer,note,   |   |
|     | OperationDefinition  | contact,   extension,  date, |  for signature (extension) |
|    I would like to receive a summary of the study findings Y/N  | Binary  | Valeur F  |
|     contact details  : email , phone number | Valeur E  | Valeur F   |






|                                                   Question for Section 6        :   Declaration by Researcher                                                                          | Ressource FHIR  | Attributs  | Description|
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|-------------------------|----------|
|   I have explained the study to the parent(s)/guardian(s) who has signed above,...  | CanonicalResource | publisher  | to indicate the name of the researcher  |
|        |    Location |  managingOrganization , address, name, hoursOfOperation | physical adress, the responsible of the site... |
|   Research Team Member Name, Signature & Date |  Observation | performer, issued, note | we can add a signature with note |
|    |  OperationDefinition | description, date,extension,contact,name | we can add a signature with extension |










C- RECAP RESSOURCES 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 
 | RESSOURCES (level 5)  | ATTRIBUTS  | WHY  |
 |--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|-------------------------|
 |  Binary     | ContentType , data          | to handle genomic data files,  or to share genomic test (as a binary file : pdf,..)        |         
 |  Bundle     |   identifier, type, link, entry, signature    |    to group all consent forms, test results ... to a single bundle      |  
 |   CanonicalResource    |     url, version, status, description, publisher     |  provide unique identifiers, url for the form, identify different versions and statuses       |  
 |    Location    |    name, address, hoursOfOperation, identifier, type, managingOrganization (reference)    |   location specific details    |  
 |  Observation      |  identifier,    triggeredBy,   status, subject, focus, issued,  note, hasMember,   | we can track multiple related consents(hasMember, triggeredBy) or the time when the observation is made(issued), ...      |  
 |  Observation    |   RelatedPerson  (  name, gender,  birthDate, address, communication )  |   typically have a personal relationship to the patient     |  
 |   OperationDefinition    |   contact,   extension ,  date, description,  status,  purpose, approvalDate |      for the signature(we better use extension),  Date when the research study was approved ( approvalDate) , but not necessarily important to implement  |  
 |  OperationOutcome     |   issue,  severity, details,  diagnostics,location, expression,location |      to capture any erros (can be useful) |  
 |   Organization    |   partOf,    identifier,  name, type, contact, qualification|      represent organizations involved in the consent process   |  
 |    Parameters   |  parameter,   resource, name, value[x], part|  capture operation requests or responses within your consent form system, particularly for operations related to handling consent data      |  
 |    Patient   |  identifier,name, telecom,address,birthDate, maritalStatus, contact (A contact party (e.g. guardian, partner, friend) for the patient),  communication(language)  |   informations about the patient      |  
 |  Practitioner      |  identifier,active,name,telecom, gender, birthDate, address,  communication, generalPractitioner,  managingOrganization,  link     |   information about the practitioner    |  
 |    Questionnaire   |  url, identifier, version, name, title, status, publisher, contact, description,  purpose, copyRight, item, linkId,     |     set of questions (in each sections)    |  
 |  QuestionnaireResponse     |   identifier, questionnaire (the url), status, subject, author, item     |  represent the answers to a Questionnaire. Each response corresponds to a specific instance of a questionnaire being filled out  (in each sections)   |  
 |   Resource    |   id, meta, implicitRules, language       |      the base structure for all FHIR resources   |  
 |   StructureDefinition     |   element    |     helps in standardizing the structure of your consent forms, making them interoperable with other systems that use FHIR  |  
 |ValueSet        |   url,identifier,version,name,title,status       |         |   
 |       |        |       |  


 value set a mettre +++  dans le form (valeur de form genre genomic exome etc>>>)






| RESSOURCES (level 4)             | ATTRIBUTS | WHY |
|----------------------------------|-----------|-----|
| ActivityDefinition               |  url, identifier, version, name, status, description, action         |     |
| AuditEvent                       |           |     |
| Composition                      |  identifier, status, type, subject, date, section ++        | aggregate consent forms or related documents into a single composition    |
| Coverage                         |           |     |
| CoverageEligibilityRequest       |           |     |
| CoverageEligibilityResponse      |           |     |
| DocumentReference                | identifier, status, type, subject, content, description          |  manage and reference documents related to consent or research   |
| Encounter                        |           |     |
| HealthcareService                |    identifier, type, serviceType, location, organization       |     |
| ImagingStudy                     |           |     |
| ImplementationGuide              |           |     |
| Library                          |           |  store reusable libraries of codes or data for consent management   |
| List                             |           |     |
| Measure                          |           |     |
| MeasureReport                    |           |     |
| Medication                       | identifier, status, code, form, amount, ingredient          |  medications related to consent,   |
| MedicationRequest                |           |     |
| MedicationStatement              |   identifier, status, patient, medication, effectiveDate        |   track statements about medications taken by patients related to consent  |
| MessageHeader                    |           |     |
| NamingSystem                     |           |     |
| PaymentNotice                    |           |     |
| PaymentReconciliation            |           |     |
| Person                           |identifier, name, gender, birthDate, address, contact           |  Manage information about individuals related to consent or research   |
| PlanDefinition                   |           |     |
| PractitionerRole                 | identifier, status, role, practitioner, organization          |  Define the  role of practitioners involved in the consent process   |
| Procedure                        |     identifier, status, code, subject, performed, outcome      |   to manage procedures related to consent or genetic testing  |
| Provenance                       |           |     |
| RequestOrchestration             |           |     |
| ServiceRequest                   |           |     |
| StructureMap                     |           |     |
| TestScript                       |           |     |



| RESSOURCES (level 3)             | ATTRIBUTS | WHY |
|----------------------------------|-----------|-----|
| AllergyIntolerance               |     identifier, patient,code,reaction,criticality,onset      | take into account the allergies relevant to consent or research    |
| Appointment                      |           |     |
| AppointmentResponse              |           |     |
| Basic                            |           |     |
| CompartmentDefinition            |           |     |
| ConceptMap                       |           |     |
| DiagnosticReport                 |           |     |
| Group                            |           |     |
| MedicinalProductDefinition       |           |     |
| Schedule                         |           |     |
| Slot                             |           |     |
| Subscription                     |           |     |
| Task                             |           |     |
| VisionPrescription               |           |     |



| RESSOURCES (level 2)             | ATTRIBUTS | WHY |
|----------------------------------|-----------|-----|
| Account                          |           |     |
| AdministrableProductDefinition   |           |     |
| AdverseEvent                     |           |     |
| BiologicallyDerivedProduct       |           |     |
| CarePlan                         |           |     |
| CareTeam                         |           |     |
| Claim                            |           |     |
| ClaimResponse                    |           |     |
| ClinicalUseDefinition            |           |     |
| Communication                    |           |     |
| CommunicationRequest             |           |     |
| Consent                          |           |     |
| DetectedIssue                    |           |     |
| Device                           |           |     |
| Endpoint                         |           |     |
| EpisodeOfCare                    |           |     |
| ExplanationOfBenefit             |           |     |
| FamilyMemberHistory              |           |     |
| Goal                             |           |     |
| GraphDefinition                  |           |     |
| GuidanceResponse                 |           |     |
|Ingredient                       |           |     |
| ManufacturedItemDefinition       |           |     |
| MedicationAdministration          |           |     |
| MedicationDispense               |           |     |
| NutritionOrder                   |           |     |
| PackagedProductDefinition        |           |     |
| RegulatedAuthorization           |           |     |
| RiskAssessment                   |           |     |
| Specimen                         |           |     |
| SubscriptionStatus               |           |     |
| SubscriptionTopic                |           |     |
| Substance                        |           |     |



| RESSOURCES (level 1)             | ATTRIBUTS | WHY |
|----------------------------------|-----------|-----|
| ActorDefinition                  |           |     |
| ArtifactAssessment               |           |     |
| BodyStructure                    |           |     |
| ChargeItem                       |           |     |
| ChargeItemDefinition             |           |     |
| Citation                         |           |     |
| ClinicalImpression               |           |     |
| Contract                         |           |     |
| DeviceDefinition                 |           |     |
| DeviceMetric                     |           |     |
| DeviceRequest                    |           |     |
| DeviceUsage                      |           |     |
| Evidence                         |           |     |
| EvidenceVariable                 |           |     |
| ExampleScenario                  |           |     |
| Flag                             |           |     |
| ImagingSelection                 |           |     |
| ImmunizationEvaluation           |           |     |
| ImmunizationRecommendation       |           |     |
| MedicationKnowledge              |           |     |
| MessageDefinition                |           |     |
| MolecularSequence                |           |     |
| NutritionIntake                  |           |     |
| NutritionProduct                 |           |     |
| ObservationDefinition            |           |     |
| OrganizationAffiliation          |           |     |
| Requirements                     |           |     |
| SpecimenDefinition               |           |     |
| SubstanceDefinition              |           |     |
| SupplyDelivery                   |           |     |
| SupplyRequest                    |           |     |
| TerminologyCapabilities          |           |     |
| TestReport                       |           |     |
| Transport                        |           |     |
| VerificationResult               |           |     |



| RESSOURCES (level 0)                         | ATTRIBUTS | WHY |
|----------------------------------------------|-----------|-----|
| BiologicallyDerivedProductDispense           |           |     |
| ConditionDefinition                          |           |     |
| DeviceAssociation                            |           |     |
| DeviceDispense                               |           |     |
| EncounterHistory                             |           |     |
| EnrollmentRequest                            |           |     |
| EnrollmentResponse                           |           |     |
| EventDefinition                              |           |     |
| EvidenceReport                               |           |     |
| FormularyItem                                |           |     |
| GenomicStudy                                 |           |     |
| InsurancePlan                                |           |     |
| InventoryItem                                |           |     |
| InventoryReport                              |           |     |
| Invoice                                      |           |     |
| Linkage                                      |           |     |
| Permission                                   |           |     |
| ResearchStudy                                |           |     |
| ResearchSubject                              |           |     |
| SubstanceNucleicAcid                         |           |     |
| SubstancePolymer                             |           |     |
| SubstanceProtein                             |           |     |
| SubstanceReferenceInformation                |           |     |
| SubstanceSourceMaterial                      |           |     |
| TestPlan                                     |           |     |

