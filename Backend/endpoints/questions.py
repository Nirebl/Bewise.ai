import typing

from fastapi import FastAPI

from dto import QuestionRequest, QuestionInputDTO, QuestionOutDTO
from models.question import QuestionDBModerator
from utils import JserviceAPI

questions_app = FastAPI(title="questions module")


@questions_app.post("/")
async def get_question(request: QuestionRequest) -> typing.Union[QuestionOutDTO, None]:
    questions: typing.List[QuestionInputDTO] = []
    while len(questions) != request.questions_num:
        questions += await JserviceAPI.get_questions(min(100, request.questions_num - len(questions)))

    last_index: int = 0

    for i in questions:
        current_question = i
        while await QuestionDBModerator.question_exists(current_question):
            current_question = (await JserviceAPI.get_questions(1))[0]
            print("change_question")

        last_index = await QuestionDBModerator.add_question(current_question)

    if last_index == 0:
        return None
    return await QuestionDBModerator.get_question_by_id(last_index - 1)
