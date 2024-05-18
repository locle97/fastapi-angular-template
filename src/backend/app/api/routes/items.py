from typing import Union

from fastapi import APIRouter

router = APIRouter()


@router.get("")
def read_root():
    return [{"id": 1, "name": "Foo", "completed": False},
            {"id": 2, "name": "Bar", "completed": True},
            {"id": 3, "name": "FooBar", "completed": False}]


@router.get("/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
