from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/user/{user_id}/workspace/{workspace_id}/board/{board_id}/list/{list_id}/card/{card_id}")
async def read_card(user_id: int, workspace_id: int, board_id: int, list_id: int, card_id: int):
    return {"user_id": user_id, "workspace_id": workspace_id, "board_id": board_id, "list_id": list_id, "card_id": card_id}
