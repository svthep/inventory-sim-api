import json
import os
import random
from typing import Dict
from uuid import uuid4

import boto3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Simulated inventory
inventory = {"item-A": 50, "item-B": 75, "item-C": 100}

# S3 Setup
s3_bucket = os.getenv("S3_BUCKET", "inventory-logs-placeholder")
s3_client = boto3.client("s3", region_name="us-east-1")


def log_to_s3(event: dict):
    log_id = f"logs/{uuid4()}.json"
    s3_client.put_object(Bucket=s3_bucket, Key=log_id, Body=json.dumps(event))


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

    log_to_s3({"event": "order", "item": order.item, "quantity": order.quantity})

    inventory[order.item] -= order.quantity
    return {"message": "Order placed", "remaining": inventory[order.item]}


@app.post("/refill")
def refill_stock():
    # Probabilistic refill (50% chance to refill each item)
    for item in inventory:
        if random.random() < 0.5:
            added = random.randint(10, 30)
            inventory[item] += added
    log_to_s3({"event": "refill", "inventory": inventory})
    return {"message": "Refill attempted", "stock": inventory}
