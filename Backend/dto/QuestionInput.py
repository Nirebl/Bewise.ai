import datetime
import typing

from pydantic import BaseModel


class Category(BaseModel):
    id: int
    title: str
    created_at: str
    updated_at: str
    clues_count: int


class QuestionInputDTO(BaseModel):
    id: int
    answer: str
    question: str
    value: typing.Union[int, None]
    airdate: str
    created_at: str
    updated_at: str
    category_id: int
    game_id: int
    invalid_count: typing.Union[None, bool, int, str]
    category: Category
