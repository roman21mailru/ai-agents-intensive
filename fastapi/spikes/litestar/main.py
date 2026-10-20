from dataclasses import dataclass

from litestar import Litestar, get, post

items: list[dict[str, object]] = []


@dataclass
class ItemIn:
    name: str
    price: float


@get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@post("/items", status_code=201)
async def create_item(data: ItemIn) -> dict[str, object]:
    record: dict[str, object] = {"id": len(items) + 1, "name": data.name, "price": data.price}
    items.append(record)
    return record


app = Litestar(route_handlers=[health, create_item])
