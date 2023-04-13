from sqlalchemy import JSON, Column, Integer, String

from .database import Base


class Product(Base):
    __tablename__ = 'product'

    nm_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    brand = Column(String)
    brand_id = Column(Integer)
    site_brand_id = Column(Integer)
    supplier_id = Column(Integer)
    sale = Column(Integer)
    price = Column(String)
    sale_price = Column(String)
    rating = Column(Integer)
    feedbacks = Column(Integer)
    colors = Column(JSON)
