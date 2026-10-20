from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
items: list[dict[str, object]] = []


class ItemIn(BaseModel):
    name: str
    price: float


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/items", status_code=201)
async def create_item(item: ItemIn) -> dict[str, object]:
    record: dict[str, object] = {"id": len(items) + 1, **item.model_dump()}
    items.append(record)
    return record
