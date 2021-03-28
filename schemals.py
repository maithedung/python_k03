from pydantic import BaseModel
from typing import List, Optional


class Blog(BaseModel):
    title: str
    body: str
