# from pydantic import BaseModel, Field
# from typing import List, Dict, Optional


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


# class Patient(BaseModel):
#     name: str
#     age: int
#     weight: float
#     married: Optional[bool]=None
#     allergies: List[str]
#     contact_details: Dict[str, str]



# def insrt_patient_details(patient: Patient):
#     print(patient.name)
#     print(patient.married)
#     print(patient.allergies[1])
#     print(patient.contact_details['phone1'])


# patient_info= {
#     'name':'abc',
#     'age':123,
#     'weight':123,
#     # 'married':True,
#     'allergies': [
#         'rabbis', 'tb' 
#     ],
#     'contact_details':{
#         'phone1': "1234567890",
#         'phone2': "1234567890"
#     }
# }


# patient = Patient(**patient_info)

# insrt_patient_details(patient)


# from pydantic import BaseModel, Field, field_validator, model_validator, computed_field
# from typing import List, Dict, Optional


# class User(BaseModel):
#     id: int
#     name: str
#     is_active: bool

# input_data = {'id':101,'name':'abc','is_active':1}

# user = User(**input_data)
# print(user)

# class ProductModel(BaseModel):
#     id: int
#     name: str
#     price: float
#     in_stock: bool = None #type: ignore
#     items = List



# def product(result: ProductModel):
#     print(result.id)
#     print(result.name)
#     print(result.price)
#     print(result.in_stock)

# product_model = {
#     'id':123,
#     "name": "abc",
#     'price':123.456,
#     'in_stock': True,
#     'items':['rice', 'wheat'] 
# }

# pro = ProductModel(**product_model)
# # product(pro)

# class Employee(BaseModel):
#     id: int
#     name: str = Field(
#         ...,
#         min_length=3,
#         max_length=50,
#         description='Employee Name',
#         examples= ['Vishwa']
#     ) 
#     # department: Optional[str]= 'general'
#     department: str | None = 'general'
#     salary: float = Field(..., ge=10000)


# from pydantic import BaseModel, Field, field_validator, model_validator, computed_field
# from typing import List, Dict, Optional

# class User(BaseModel):
#     username: str

#     @field_validator('username')
#     def usename_length(cls, v):
#         if len(v)<4:
#             raise ValueError('user name must be atleast 4 characters')
#         return v


# class SignUpData(BaseModel):
#     password: str
#     confirm_password: str

#     @model_validator(mode="after")
#     def password_match(cls, v):
#         if v.password != v.confirm_password:
#             raise ValueError("Password do not match")
#         return v


# class Product(BaseModel):
#     price: float
#     quantity: int

#     @computed_field
#     @property
#     def total_price(self)->float:
#         return self.price * self.quantity


# from pydantic import BaseModel, Field, field_validator, model_validator, computed_field
# from typing import List, Dict, Optional

# class Booking(BaseModel):
#     user_id: int
#     room_id: int
#     nights: int = Field(gt=1)
#     rate_per_night:float

#     @computed_field
#     @property
#     def total_amount(self)->float:
#         return self.nights*self.rate_per_night




# from typing import List, Optional
# from pydantic import BaseModel

# class Address(BaseModel):
#     street: str
#     city: str
#     postal_code: str

# class User(BaseModel):
#     id: int
#     name: str
#     address: Address

# class Comment(BaseModel)
#     id:int
#     content: str
#     replies: Optional[List['Comment']] = None

# Comment.model_rebuild()


# adddress = Address(
#     street="abcd",
#     city="efgh",
#     postal_code='10001'
# )

# user = User(
#     id = 1001,
#     name='xyz',
#     address=adddress
# )

# comment = Comment(
#     id=102,
#     content="first comment",
#     replies=[
#         Comment(id=1, content='reply1'),
#         Comment(id=2, content='reply2')
#     ]
# )








# from pydantic import BaseModel
# from typing import List
# from datetime import datetime




# class Address(BaseModel):
#     street:str
#     city:str
#     pin_code:str


# class User(BaseModel):
#     id:int
#     name:str
#     email: str
#     is_active:bool=True
#     createdAt: datetime
#     address: Address
#     tags: List[str]=[]

# #create a user instance
# user = User(
#     id = 1,
#     name =  'Vishwa',
#     email = "Vishwa@gmail.com",
#     createdAt = datetime(2026,3,15,12,30),
#     address = Address(
#         street = "something",
#         city = "abcd",
#         pin_code = "111111"
#     ),
#     is_active = False,
#     tags = ['premium', 'subscriber']
# )

# response = user.model_dump()

# print(response)

# print()

# json_str = user.model_dump_json()
# print(len(json_str))




from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr


app = FastAPI()

class User(BaseModel):
    username: str
    email: EmailStr
    password: str

class Settings(BaseModel)
    app_name: str = "fastest API"
    admin_email: str = "admin@fastest.com"



def get_settings():
    return Settings

@app.post('/signup')
def SignUp(user: User):
    return {'message': f'User {user.username} signed up successfully'}


@app.get('/settings')
def get_settings_endpoint(settings: Settings = Depends(get_settings))
    return settings
















