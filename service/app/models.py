# service/app/models.py

from sqlalchemy import Column, Integer, String, Date, Boolean, Float, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    phone = Column(String(50))
    address_line1 = Column(String(255))
    city = Column(String(100))
    state = Column(String(100))
    pincode = Column(String(20))
    created_at = Column(DateTime, server_default=func.now())

    employment = relationship("EmploymentInfo", back_populates="user", cascade="all, delete-orphan")
    bank_info = relationship("UserBankInfo", back_populates="user", cascade="all, delete-orphan")


class EmploymentInfo(Base):
    __tablename__ = "employment_info"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    company_name = Column(String(255))
    designation = Column(String(255))
    start_date = Column(Date)
    end_date = Column(Date, nullable=True)
    is_current = Column(Boolean, default=False)
    salary = Column(Float, default=0.0)

    user = relationship("User", back_populates="employment")


class UserBankInfo(Base):
    __tablename__ = "user_bank_info"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    bank_name = Column(String(255))
    account_number = Column(String(255))
    ifsc = Column(String(50))
    account_type = Column(String(50))

    user = relationship("User", back_populates="bank_info")
