from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field
from typing import Optional, Dict
import uuid
app = FastAPI(title="My Testing API")

db = {}

class ObjectData(BaseModel):
    name: Optional[str] = None
    data: Optional[dict] = None


@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)
    print(f"Request {request.method} {request.url.path} | Status: {response.status_code}")
    return response


@app.post("/objects", status_code=200)
async def create_object(obj: ObjectData):
    obj_id = str(uuid.uuid4())
    new_obj = {"id": obj_id, "name": obj.name, "data": obj.data}
    db[obj_id] = new_obj
    return new_obj

@app.get("/objects/{obj_id}")
async def get_object(obj_id: str):
    if obj_id not in db:
        raise HTTPException(status_code=404, detail="Object not found")
    return db[obj_id]


@app.patch("/objects/{obj_id}")
async def update_object_patch(obj_id: str, obj: ObjectData):
    if obj_id not in db:
        raise HTTPException(status_code=404, detail="Not found")

    stored_obj = db[obj_id]
    update_data = obj.model_dump(exclude_unset=True)

    stored_obj.update(update_data)
    return stored_obj


@app.put("/objects/{obj_id}")
async def update_object_put(obj_id: str, obj: ObjectData):
    if obj_id not in db:
        raise HTTPException(status_code=404, detail="Not found")

    updated_obj = {"id": obj_id, "name": obj.name, "data": obj.data}
    db[obj_id] = updated_obj
    return updated_obj


@app.delete("/objects/{obj_id}")
async def delete_object(obj_id: str):
    if obj_id in db:
        del db[obj_id]
        return {"message": "Object deleted"} 
    raise HTTPException(status_code=404, detail="Object not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)