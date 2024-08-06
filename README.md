


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
|             |ValueSet        |   url,identifier,version,name,title,status       |     you just put the value like 'exome'    | 
|  to look for changes in genes that may be associated with :   | Observation  | Valeur F  |
|  [Condition or Clinical Indication]   | Observation  | Valeur F  |
|             |ValueSet        |   url,identifier,version,name,title,status       |     you just put the value like 'any condition'    | 
|  Genomic test results are based on current knowledge, which may change in the future  | Observation  | code, valueCodeableConcept, category  |Record the target of the genomic test |
|  If I change my mind, I can choose not to be told about the result    | consent  | provision  | details on how consent can be modified or withdrawn 
| This test might find a cause for the condition(s)  | Observation  |  |
|  This test might not find a cause for the condition(s)   | Observation  |  |
|  This result might be of 'unknown significance', which means it cannot be understood today   | Observation  |   |
|  There is a chance that genomic testing could find other medical conditions (incidental findings)  | Observation|  |
|  Genomic testing may show unexpected family relationships   | Observation  |   |
|  Further tests or information sharing may be needed to finalize the result  | Binary  |   |
|  I will be told the results by a health professional   |  |  |
|  Results may have implications for the health/genetic risks for the child/the person under my care and family members   |   |   |
|  Results can be used to inform counselling and testing of family members, though my child's/ the person under my care's identity will not be revealed to them |   |   |
|  Results from these tests may affect my child's /the person under my care's ability to obtain some types of insurance    |   |   |
|  The results will be available to health professionals involved in the care of my children/the person under my care      |   |   |
|  Results are confidential and may not be release without my consent unless allowed by law   |   |   |
|  The following individual can be given my child's / the person under my care's results if I am unable to be contacted  |   |   |
| Contact Information :  Name , Number , Relationship to Patient  |   |  |









|                                                   Question for Section 2   : Consent for Data Sharing                                                                                                          | Ressource FHIR  | Attributs  | Description |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|-------------------------|----------|
|  I provide consent to share my child’s/ person under my care’s sample, genomic data, and related health information for   | Binary  |   |
|   | Observation |  |
|  Data is available for future general research use    | Binary |  |
|   | Observation |  |
|  Future is limited for health/medical/biomedical research |  |   |
|  Future commercial use is prohibited   |  |   |
|  Future use for methods research (analytic/software/technology development) outside the bounds of the other specified restrictions is prohibited   |  |
|   Future use of aggregate-level data for general research purposes is prohibited   | | |
|  Future use as a control set for diseases other than those specified is prohibited    |   |   |
|  Future use is limited to research involving a particular gender  |  |   |
|  Future use is limited to pediatric research   |  |   |
|  Future use is limited to research involving a specific population  |   |    |
|  Future use is limited to data generated from samples collected after the following consent form date    | |    |















|                                                   Question for Section 3   :  Consent Summary                                                                                                         | Ressource FHIR  | Attributs  | Description |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|-------------------------|----------|
|   I have had enough time to consider the information in this consent form and have :    | CanonicalResource  | name, title  | provide identifiers for different consent summaries   |
|     | OperationDefinition |  description,  status, purpose |  | 
|   Had the opportunity to discuss genomic testing and its implication with a health professional     |  |  |
|   Been given access to information about genomic testing  |  |  |
|   Been able to ask questions until I am satisfied with the answers   |   |   |
|   Been offered a copy of this consent form   | Binary  |   |
|   I provide consent to have genomic testing as summarized in these forms   |   |   |
|  Child’s name  |   |  |
|  Date of Birth   |   |   |
|  Print Parent/ Guardian’s Name :  |   |    |
|  Email/ Address :     |   |    |
|  Health Professional AHPRA ID  |   |   |
|  Health Professional Name   |   |   |









|                                                   Question for Section 4  :   Confirmation for Research Study                                                                                                         | Ressource FHIR  | Attributs  | Description |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|-------------------------|----------|
|     I have read the information statement about the study and I understand its contents   | Location  |  name, address, hoursOfOperation, identifier, type, managingOrganization (reference)    |   location specific details    |
|     I understand what my child and I have to do in this study     |   |   |
|     I understand the risks my child could face because of their involvement in this study  |   |   |
|     I voluntarily consent for myself and/or my child to take part in this research study   |   |   |
|     I have had an opportunity to ask questions about the study and I am satisfied with the answers I have received  |   |    |
|     I understand that this study has been approved by a suitable Human Research Ethics Committee. I understand that the study is required to be carried out in line with the National Statement on Ethical Conduct in Human Research (2023)  |   |  |
|     I understand I will receive a copy of this Information Statement and Consent Form | Binary  | ContentType , data     |   or to share genomic fils (as a binary file : pdf,..)  |
| |  Practitioner      |  identifier,active,name,telecom, gender, birthDate, address,  communication, generalPractitioner,  managingOrganization,  link     |   information about the practitioner(maybe researcher) who will resend to them the form   |










|                                            Question for Section 5 :         Genomic Testing Consent                                                                                            | Ressource FHIR  | Attributs  | Description |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|-------------------------|----------|
|    Please choose from the following options : I consent, I do not consent  |  |   |
|     Consent for use of my child’s NBS card and diagnostic specimen | Observation |   |
|     Consent for future contact  | Observation | |
|     Child’s Full name , co-signature (optional) & Date  | Observation  |   |
|     Parent / Guardian 1 & 2 ’s Full name , co-signature (optional) & Date  | Observation  | effectiveDateTime, performer,note,   |   |
|     | OperationDefinition  | contact,   extension,  date, |  for signature (extension) |
|    I would like to receive a summary of the study findings Y/N  | Binary  |   |
|     contact details  : email , phone number | | |






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








| RESSOURCES (level 4)             | ATTRIBUTS | WHY |
|----------------------------------|-----------|-----|
| ActivityDefinition               |  url, identifier, version, name, status, description, action         |     |
| Composition                      |  identifier, status, type, subject, date, section ++        | aggregate consent forms or related documents into a single composition    |
| DocumentReference                | identifier, status, type, subject, content, description          |  manage and reference documents related to consent or research   |
| HealthcareService                |    identifier, type, serviceType, location, organization       |     |
| Library                          |           |  store reusable libraries of codes or data for consent management   |
| Medication                       | identifier, status, code, form, amount, ingredient          |  medications related to consent,   |
| MedicationStatement              |   identifier, status, patient, medication, effectiveDate        |   track statements about medications taken by patients related to consent  |
| Person                           |identifier, name, gender, birthDate, address, contact           |  Manage information about individuals related to consent or research   |
| PractitionerRole                 | identifier, status, role, practitioner, organization          |  Define the  role of practitioners involved in the consent process   |
| Procedure                        |     identifier, status, code, subject, performed, outcome      |   to manage procedures related to consent or genetic testing  |




| RESSOURCES (level 3)             | ATTRIBUTS | WHY |
|----------------------------------|-----------|-----|
| AllergyIntolerance               |     identifier, patient,code,reaction,criticality,onset      | take into account the allergies relevant to consent or research    |
| Appointment                      |    identifier, status, type, patient, start, end, reason       |   track appointements to genetic testing for ex  |
| CompartmentDefinition            |     url, identifier, version, name, description, resource      | compartments for managing consent - related data    |
| Group                            |   identifier, type, member, name, description        |  manage groups of individuals relevant to consent or research   |
| MedicinalProductDefinition       |  identifier, status, form, ingredient, type         |  definition of medicinal products related to consent or research   |



| RESSOURCES (level 2)             | ATTRIBUTS | WHY |
|----------------------------------|-----------|-----|
| Account                          |           |     |
| AdministrableProductDefinition   | identifier, form,ingredient,type           |   define products related to the consent or research  |
| AdverseEvent                     |      identifier, status, patient, code , outcome, description     | adverse events related to genetic testing or research    |
| CarePlan                         |   identifier, status, patient, goal, activity, description        |   we can define the care plans (including consent - related activities )  |
| Consent                          |    identifier, status, patient, scope, dateTime, provision       |     |
| DetectedIssue                    |     identifier, status, patient, code, severity, detail      |   issues related to consent or research  |
| FamilyMemberHistory    +++          |  identifier, status, patient, relationship, condition         |  manage family history relevant to consent or genetic research   |
| MedicationAdministration          | identifier, status, patient, medication, dosage          |    track medication administration related to research for ex  |
| MedicationDispense               | identifier, status, patient, medication, quantity          |   manage medication dispensing related to consent or research   |
| NutritionOrder                   |   identifier, status, patient, type, diet        | track nutrition orders relevant to consent or research    |
| Specimen                         |     identifier, status, subject,type,collection, container      |    track specimens collected for genetic testing o research  |
| Substance                        | identifier, status, code, description, instance          |  to manage substances used in genetic testing o research    |



| RESSOURCES (level 1)             | ATTRIBUTS | WHY |
|----------------------------------|-----------|-----|
| ActorDefinition                  |     url, identifier, version, name, status, description      |  define actors involved in the consent process   |
| BodyStructure                    |  identifier, status, patient, location, description         |   body structures relevant to consent or research  |
| ChargeItem                       |       identifier, status, code, patient, performer    |  charge items related to consent services   |
| ChargeItemDefinition             |     url, identifier, version, name, status, code      |    define charge items and their usage in consent processes |
| Contract                         |   identifier, status, patient, subject, issued        | manage contracts related to consent or research agreements     |
| ExampleScenario                  |   url,identifier, version,name, status, actor, instance        | create example  scenarios for consent processes   |
| Flag                             |       identifier, status, patient, code, period    |    flag important information relevant to consent or research |
| MedicationKnowledge              |     identifier, status, code, classification, doseForm      | manage knowledge about medications used in genetic testing or research     |
| MolecularSequence                |     identifier, status, patient, coordinateSystem, sequence +++(could be intersting)  | manage molecular sequences related to genetic testing or research    |
| ObservationDefinition            |  url, identifier, version, name, status, description         |    define observations relevant to consent or research |
| OrganizationAffiliation          |  identifier, status, organization, role, period         |   manage affiliations of organizations involved in consent processes  |
| Requirements                     |  url , identifier , version , name , status, description         |  define requierments for consent or research activities   |
| SpecimenDefinition               |  url, identifier, version, name, type, collection         |  define speciments relevant to genetic testing or consent   |
| SubstanceDefinition              | url, identifier, version, name, type, collection | manage definitions of substances used in genetic testing or research     |
| TestReport                       | identifier, status, name, result,           |   manage reports of test conducted on consent form implementations  |
| VerificationResult               | identifier, status, target, validationType, frequency          |  Verify information relevant to consent or research   |



| RESSOURCES (level 0)                         | ATTRIBUTS | WHY |
|----------------------------------------------|-----------|-----|
| ConditionDefinition                          | url, identifier, version, name, status, description         | Define conditions relevant to genetic testing or research |
| EnrollmentRequest                            |  identifier, status, patient, provider, coverage         |   Handle enrollment requests for consent or research studies  |
| EnrollmentResponse                           | identifier, status, patient, outcome, request          |   Manage responses to enrollment requests related to consent  |
| EventDefinition        | url, identifier, version, name, status, event  | Define events relevant to consent or research activities    |
| EvidenceReport                               | url, identifier, version, name, status, description          | Manage reports of evidence related to consent or research    |
| FormularyItem   |   url, identifier, version, name, status, drug        | Manage formulary items related to consent or research    |
| GenomicStudy                                 |           |     |
| InsurancePlan   (why not?)  |  identifier, status, name, type, coverage, network     |  Manage insurance plans relevant to consent or research   |
| InventoryItem               |           |     |
| Linkage                                      | identifier, status, type, resource  | Manage linkages between related consent or research resources    |
| Permission                                   | identifier, status, patient, policy, data          |Manage permissions relevant to consent or research data     |
| ResearchStudy                                | identifier, status, title, sponsor, period          | Track research studies related to consent or genetic testing    |
| ResearchSubject   |  identifier, status, study, individual, consent         | Manage subjects participating in research studies related to consent    |
| SubstanceReferenceInformation                |  identifier, status, gene, target, classification         | Manage reference information for substances used in research    |
| TestPlan                                     |  identifier, status, name, description, testMethod         |  Manage test plans for validating consent form implementations   |

