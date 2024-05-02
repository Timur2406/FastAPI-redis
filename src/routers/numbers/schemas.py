from pydantic import BaseModel
from typing import Optional


class PhoneData(BaseModel):
    phone: str

class FullData(PhoneData):
    address: str