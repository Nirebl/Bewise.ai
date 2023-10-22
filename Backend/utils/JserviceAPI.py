import requests

from dto import QuestionInput


class JserviceAPI:
    @staticmethod
    async def get_questions(count: int) -> list[QuestionInput]:
        response = None
        try:
            response = requests.get(f"https://jservice.io/api/random?count={count}")
        except Exception as e:
            print(e)

        return [QuestionInput.QuestionInputDTO(**question) for question in response.json()]
