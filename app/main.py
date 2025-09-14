"""
logging
"""
import logging

from typing import Union
from fastapi import FastAPI

logger = logging.getLogger(__name__)
logging.info("Starting FastAPI app")

app = FastAPI()


@app.get("/")
async def read_root():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {"success": "true", "message": "successfully", "data": "hello world"}
