from sqlalchemy.orm import Session
import requests

from core.models import models


def add_product(db: Session, id: int):
    response = requests.get(
        'https://card.wb.ru/cards/detail'
        f'?curr=rub&dest=123586087&spp=19&nm={id}').json()

    product = models.Product(
        nm_id=response.get('data').get('products')[0].get('id'),
        name=response.get('data').get('products')[0].get('name'),
        brand=response.get('data').get('products')[0].get('brand'),
        brand_id=response.get('data').get('products')[0].get('brandId'),
        site_brand_id=response.get('data').get(
            'products')[0].get('siteBrandId'),
        supplier_id=response.get('data').get('products')[0].get('supplierId'),
        sale=response.get('data').get('products')[0].get('sale'),
        price=str(response.get('data').get('products')[0].get('priceU'))[:-2],
        sale_price=str(response.get('data').get(
            'products')[0].get('salePriceU'))[:-2],
        rating=response.get('data').get('products')[0].get('rating'),
        feedbacks=response.get('data').get('products')[0].get('feedbacks'),
        colors=response.get('data').get('products')[0].get('colors'),
    )

    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def all_products(db: Session):
    return db.query(models.Product).all()


def get_product(db: Session, id: int):
    return db.query(models.Product).filter(models.Product.nm_id == id).first()


def del_product(db: Session, id: int):
    product = db.query(models.Product).filter(models.Product.nm_id == id)
    product.delete()
    db.commit()
    return
