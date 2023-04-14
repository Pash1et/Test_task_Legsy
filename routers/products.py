from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.crud import crud
from core.models.database import SessionLocal

router = APIRouter(prefix='/items')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/add_product/{id}')
def add_product(id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, id=id)
    if product:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Product already added')
    return crud.add_product(id=id, db=db)


@router.get('/all_products')
def get_all_products(db: Session = Depends(get_db)):
    products = crud.all_products(db=db)
    return products


@router.get('/get_product/{id}')
def get_product(id: int, db: Session = Depends(get_db)):
    product = crud.get_product(id=id, db=db)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Product is not found')
    return product


@router.delete('/del_product/{id}')
def del_product(id: int, db: Session = Depends(get_db)):
    product_exists = crud.get_product(id=id, db=db)
    if not product_exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Product is not found')
    crud.del_product(id=id, db=db)
    return {'delete': 'The product has been removed'}
