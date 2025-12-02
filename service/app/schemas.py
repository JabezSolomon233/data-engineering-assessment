from pydantic import BaseModel
from typing import Optional, List

class Employment(BaseModel):
    id: int
    company_name: str
    designation: str
    start_date: Optional[str]
    end_date: Optional[str]
    is_current: bool
    salary: float

    class Config:
        from_attributes = True


class BankInfo(BaseModel):
    id: int
    bank_name: str
    account_number: str
    ifsc: str
    account_type: str

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    address_line1: str
    city: str
    state: str
    pincode: str


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address_line1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    pincode: Optional[str] = None


class User(UserBase):
    id: int
    employment: List[Employment] = []
    bank_info: List[BankInfo] = []

    class Config:
        from_attributes = True
