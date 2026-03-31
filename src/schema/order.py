from pydantic import BaseModel, Field

class OrderCreate(BaseModel):
    item_id   : int = Field(..., ge = 0)
    quantity  : int = Field(..., gt = 0)
    address   : str = Field(..., min_length = 1)


class OrderResponse(BaseModel):
    order_id  : int = Field(..., ge = 0)
    item_id   : int = Field(..., ge = 0)
    quantity  : int = Field(..., gt = 0)
    address   : str = Field(..., min_length = 1)
    # total_price : float = Field(..., gt=0)
    # order_status : str = Field(..., min_length = 1)
    # payment_status : str = Field(..., min_length = 1)

    class Config:
        from_attributes = True