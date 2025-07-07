from fastapi import APIRouter


router = APIRouter(prefix="/v1", tags=["Orders"])

@router.get("/orders/{order_id}")
async def get_user_order():
    return {"message": "Hello World"}

@router.post("/orders")
async def create_order():
    return {"message": "Hello World"}

@router.patch("/orders/{order_id}")
async def change_order():
    return {"message": "Hello World"}

@router.delete("/orders/{order_id}")
async def delete_order():
    return {"message": "Hello World"}