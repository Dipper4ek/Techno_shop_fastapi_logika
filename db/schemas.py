from pydantic import BaseModel, Field

class ItemBase(BaseModel):
    name: str
    description: str
    price: float = Field(..., ge=0, description="Ціна повинна бути 0 або більше")
    quantity: int

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
