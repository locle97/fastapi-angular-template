from sqlmodel import Field, SQLModel


# Shared properties
# TODO replace email str with EmailStr when sqlmodel supports it
class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str | None = None
    completed: bool | None = None


class Items(SQLModel):
    data: list[Item]
    count: int
