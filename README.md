# Web based Software Solution for small scale Hospitals

![alt text](https://drive.google.com/uc?id=14sbc_6MEwMa57RfuH3-FckXCW_s4wNzr)

When it comes to hospitals in rural areas, the major problem that they face is maintaining patient history in their records. Also, when patient comes for next visit, they tend to forget the documents containing history of their treatment. In such cases it becomes difficult for doctors to give uniform treatment to patients.

Parents being Doctors, I got to know about this problem with small scale Hospitals in rural areas so I decided to create solution for this problem since small scale hospitals have limited resources and it is economically not viable for them to purchase and maintain licenced softwares for their needs. This project is intented to solve some of the record and documentation problems for small scale hospitals with a very light web based software solution desined using Django web framework along with sqlite as backend database. 

With this software, doctors will be able to maintain the record of patients along with their history and create a printed prescription. This is successfully being used in 2 hospitals in my hometown currently.

Some of the features of this web based solution are illustrated using below description along with images:

### A. Creating Patient Records

Each patient will be assigned a unique id as a parent key for prescription which will again have unique ids for each visit. Steps to add a new patient are shown below.

1. First step would be to add some frequently used medicines to the database. This can be added with Medicines tab at the top

![alt text](https://drive.google.com/uc?id=1hozhNtebnmIQA2vOUiORyw2H2GaWqKpB)

2. Second will be to add patient and all the details. There are multiple stages of adding a patient.
    
    Stage 1:
    
    ![alt text](https://drive.google.com/uc?id=16n2bxXMDgEPxpKt2ZyBDPjK-FTiMazmC)
    
    Stage 2:
    ![alt text](https://drive.google.com/uc?id=1S95_cU2-XoYZNAJP_p4YPSU7YsmfECTD)
    
    Stage 3:
    ![alt text](https://drive.google.com/uc?id=1jpO1hjATE9s1pnS8q7LXJZWYx7CeMARH)
    
    Stage 4:
    ![alt text](https://drive.google.com/uc?id=1M-ohNKG83kELEGj-ZYcjXqs0Clwt1hwL)
    
    Stage 5:
    Stage 5 will be to print prescription which will change from hospital to hospital.
    
  ### B. All patient Entries can be Viewed for a particular day with Patient List tab
  
  ![alt text](https://drive.google.com/uc?id=1tx3qP3F2fXNj9F6O8QZDYdCeXmkgKPGL)
  
  ### C. Patient Related data is processed for Hospital use and can be viewed later with Patient Data tab
  
  ![alt text](https://drive.google.com/uc?id=1c3Yh7zG6AkDl42HdQLvr6LLEcvvSJz2j)
  
  ### D. There are more subtabs which can be used for Hospital purpose. It will not be possible to add all tabs here.

### You can explore all non explained tabs by running the software as local server by using following steps :

1. Go to the project directory

2. create superuser using "python manage.py createsuperuser"

3. run "python manage.py runserver"

4. open localserver http://127.0.0.1:8000/
