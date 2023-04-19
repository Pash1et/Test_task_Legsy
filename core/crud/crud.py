import requests
from sqlalchemy.orm import Session

from core.models import models
from core.models.database import SessionLocal


def add_product(db: Session, id: int):
    response = requests.get(
        'https://card.wb.ru/cards/detail'
        f'?curr=rub&dest=123586087&spp=19&nm={id}').json()

    data_products = response.get('data').get('products')[0]

    product = models.Product(
        nm_id=data_products.get('id'),
        name=data_products.get('name'),
        brand=data_products.get('brand'),
        brand_id=data_products.get('brandId'),
        site_brand_id=data_products.get('siteBrandId'),
        supplier_id=data_products.get('supplierId'),
        sale=data_products.get('sale'),
        price=str(data_products.get('priceU'))[:-2],
        sale_price=str(data_products.get('salePriceU'))[:-2],
        rating=data_products.get('rating'),
        feedbacks=data_products.get('feedbacks'),
        colors=data_products.get('colors'),
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


def update_product():
    db = SessionLocal()

    products = db.query(models.Product).all()
    for product in products:
        response = requests.get(
            'https://card.wb.ru/cards/detail?curr=rub&'
            f'dest=123586087&spp=19&nm={product.nm_id}'
        ).json()
        data_products = response.get('data').get('products')[0]

        product.nm_id = data_products.get('id')
        product.name = data_products.get('name'),
        product.brand = data_products.get('brand'),
        product.brand_id = data_products.get('brandId'),
        product.site_brand_id = data_products.get('siteBrandId'),
        product.supplier_id = data_products.get('supplierId'),
        product.sale = data_products.get('sale'),
        product.price = str(data_products.get('priceU'))[:-2],
        product.sale_price = str(data_products.get('salePriceU'))[:-2],
        product.rating = data_products.get('rating'),
        product.feedbacks = data_products.get('feedbacks'),
        product.colors = data_products.get('colors'),

        db.add(product)
        db.commit()

    db.close()
