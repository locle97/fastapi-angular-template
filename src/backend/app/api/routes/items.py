from typing import Union
from sqlmodel import select

from fastapi import APIRouter
from app.core.models import Item
from app.api.deps import SessionDep

router = APIRouter()


@router.get("")
def get_items(session: SessionDep) -> list[Item]:
    statement = select(Item)
    items = session.exec(statement).all()
    return items


@router.get("/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
