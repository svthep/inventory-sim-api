import random
from typing import Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Simulated inventory
inventory = {"item-A": 50, "item-B": 75, "item-C": 100}


class Order(BaseModel):
    item: str
    quantity: int


@app.get("/stock")
def get_stock():
    return inventory


@app.post("/order")
def place_order(order: Order):
    if order.item not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")

    if inventory[order.item] < order.quantity:
        raise HTTPException(status_code=400, detail="Not enough stock")

    inventory[order.item] -= order.quantity
    return {"message": "Order placed", "remaining": inventory[order.item]}


@app.post("/refill")
def refill_stock():
    # Probabilistic refill (50% chance to refill each item)
    for item in inventory:
        if random.random() < 0.5:
            added = random.randint(10, 30)
            inventory[item] += added
    return {"message": "Refill attempted", "stock": inventory}
