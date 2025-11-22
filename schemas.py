"""
Database Schemas for Sweet Shop (Ice cream, chocolates, pralines, brittles)

Each Pydantic model represents a collection in MongoDB. The collection name
is the lowercase of the class name (e.g., Product -> "product").
"""

from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import datetime


class Product(BaseModel):
    title: str = Field(..., description="Product name")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Category (ice-cream, chocolate, praline, brittle)")
    image: Optional[str] = Field(None, description="Image URL")
    in_stock: bool = Field(True, description="Whether product is in stock")


class CartItem(BaseModel):
    product_id: str = Field(..., description="Referenced product _id as string")
    title: str
    price: float
    quantity: int = Field(1, ge=1)
    image: Optional[str] = None


class Customer(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None


class Order(BaseModel):
    items: List[CartItem]
    subtotal: float = Field(..., ge=0)
    tax: float = Field(..., ge=0)
    total: float = Field(..., ge=0)
    customer: Customer
    note: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
