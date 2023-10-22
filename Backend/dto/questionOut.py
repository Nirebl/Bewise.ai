import datetime

from pydantic import BaseModel


class QuestionOutDTO(BaseModel):
    id: int
    text: str
    answer: str
    date: str


