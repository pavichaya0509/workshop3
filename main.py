from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
from typing import Dict, Optional, List, Tuple
import uvicorn

app = FastAPI()


@app.get("/") # / คือ root path 
def index():
    return JSONResponse(content={"message": "Hello,  Jim"}, status_code=200)

@app.get("/example/")
def get_query_parameter(start: int = 0, limit: int = 0):

    print("--> start : ", start)
    print("--> limit : ", limit)

    return JSONResponse(
        content={"message": f"start: {start} limit: {limit}"},
        
        status_code=200,
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)