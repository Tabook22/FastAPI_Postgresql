from fastapi import Form, File, UploadFile
from pydantic import BaseModel


# https://stackoverflow.com/a/60670614
class UserForm(BaseModel):
    firstname:str 
    lastname:str 
    details:str
    cvfile: UploadFile

    @classmethod
    def as_form(
        cls,
        firstname: str = Form(...),
        lastname: str = Form(...),
        details:str=Form(...),
        cvfile: UploadFile = File(...)
    ):
        return cls(
            firstname=firstname,
            lastname=lastname,
            details=details,
            cvfile=cvfile
        )

