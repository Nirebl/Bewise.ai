from fastapi import FastAPI

from endpoints import questions_app

app = FastAPI(title="Bewise.ai test solution")

app.include_router(questions_app)
