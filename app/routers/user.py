from ..db import get_db
from sqlalchemy.orm import Session
from fastapi import FastAPI, Response, HTTPException, Depends, APIRouter
from .. import models, schemas, utils

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", status_code=201, response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=404, detail=f"User with id: {id} does not exist."
        )

    return user
