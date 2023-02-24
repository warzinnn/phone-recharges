from sqlalchemy import FLOAT, Column, ForeignKey, String, Table
from sqlalchemy.exc import ArgumentError
from sqlalchemy.orm import class_mapper, registry, relationship
from sqlalchemy.orm.exc import UnmappedClassError

from src.domain.company import Company
from src.domain.products import Products

""" Mapper (Imperative Mapping)
Using this approach the ORM Depends on Model.
The mapper will bind our domain model to the SQL tables.
"""
mapper_registry = registry()


""" Company entity
company_id -> str : id of company

Explanation
===========
In the configure_mappers() the relationship is defined.
- Company relationship (company has products)
"""
company_table = Table(
    "company",
    mapper_registry.metadata,
    Column("company_id", String(25), primary_key=True),
)

""" Product entity
id -> str : id of product
value -> float : value of product
id_company -> str : id of company

Explanation
===========
In the configure_mappers() the relationship is defined.
- Company relationship (product belongs to company)
"""
products_table = Table(
    "products",
    mapper_registry.metadata,
    Column("id", String(25), primary_key=True),
    Column("value", FLOAT, nullable=False),
    Column("id_company", String, ForeignKey("company.company_id")),
)


def is_mapped_class(cls):
    """Checks if the class is already mapped to avoid errors"""
    try:
        class_mapper(cls)
    except (ArgumentError, UnmappedClassError):
        return False
    else:
        return True


def configure_mappers():
    """Configure mappers"""
    if not is_mapped_class(Company) and not is_mapped_class(Products):
        mapper_registry.map_imperatively(
            Company,
            company_table,
            properties={
                "producties": relationship(
                    Products, back_populates="companies", lazy="subquery"
                )
            },
        )
        mapper_registry.map_imperatively(
            Products,
            products_table,
            properties={
                "companies": relationship(Company, back_populates="producties")
            },
        )
