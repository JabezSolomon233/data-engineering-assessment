# service/app/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import get_db

router = APIRouter()

@router.post("/users", response_model=schemas.User, tags=["users"])
def create_user(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    # email uniqueness handled by DB; catch exceptions if needed
    user = crud.create_user(db, user_in)
    return user

@router.get("/users", response_model=list[schemas.User], tags=["users"])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.list_users(db, skip=skip, limit=limit)

@router.get("/users/{user_id}", response_model=schemas.User, tags=["users"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}", response_model=schemas.User, tags=["users"])
def update_user(user_id: int, payload: schemas.UserUpdate, db: Session = Depends(get_db)):
    user = crud.update_user(db, user_id, payload.model_dump(exclude_unset=True))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{user_id}", tags=["users"])
def delete_user_route(user_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_user(db, user_id)
    if not ok:
        raise HTTPException(status_code=404, detail="User not found")
    return {"ok": True}

@router.post("/users/{user_id}/employment", response_model=schemas.Employment, tags=["employment"])
def add_employment(user_id: int, payload: schemas.EmploymentCreate, db: Session = Depends(get_db)):
    return crud.add_employment(db, user_id, payload)

@router.post("/users/{user_id}/bank", response_model=schemas.Bank, tags=["bank"])
def add_bank(user_id: int, payload: schemas.BankCreate, db: Session = Depends(get_db)):
    return crud.add_bank(db, user_id, payload)
