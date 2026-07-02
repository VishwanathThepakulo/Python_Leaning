from pydantic import BaseModel, Field
from typing import List, Dict, Optional


# class ContactInfo(BaseModel):
#     name:str = Field(description='user name')
#     number: int = Field(description='user name')
#     email: str = Field(description='user name')


# def contact_info(request: ContactInfo):
#     print(request.name)
#     print(request.number)
#     print(request.email)
    

# contactinfo = {'name':"xyz", 'number':123, 'email':"abc@gmail.com"}
# info = ContactInfo(**contactinfo)
# contact_info(info)


class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: Optional[bool]=None
    allergies: List[str]
    contact_details: Dict[str, str]



def insrt_patient_details(patient: Patient):
    print(patient.name)
    print(patient.married)
    print(patient.allergies[1])
    print(patient.contact_details['phone1'])


patient_info= {
    'name':'abc',
    'age':123,
    'weight':123,
    # 'married':True,
    'allergies': [
        'rabbis', 'tb' 
    ],
    'contact_details':{
        'phone1': "1234567890",
        'phone2': "1234567890"
    }
}


patient = Patient(**patient_info)

insrt_patient_details(patient)











