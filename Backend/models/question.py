import os
import typing

from sqlalchemy import create_engine, Column, Integer, String, TEXT, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

import config
from dto import QuestionInputDTO

# SQLAlchemy database setup
Base = declarative_base()
engine = create_engine(f'postgresql+psycopg2://{config.DBS_USER}:{config.DBS_PASS}@{config.DBS_URL}/bewise_ai',
                       echo=False)
Session = sessionmaker(bind=engine)
session = Session()


class QuestionDB(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    text = Column(String, nullable=False)
    answer = Column(TEXT, nullable=False)
    date = Column(TEXT, nullable=False)


class QuestionDBModerator:
    @staticmethod
    async def get_question_by_id(question_id: int) -> typing.Union[int, None]:
        return session.query(QuestionDB).filter_by(id=question_id).first() or None

    @staticmethod
    async def add_question(question_input: QuestionInputDTO) -> int:
        question_db = QuestionDB(text=question_input.question, answer=question_input.answer,
                                 date=question_input.created_at)
        session.add(question_db)
        session.commit()
        return question_db.id

    @staticmethod
    async def question_exists(question_input: QuestionInputDTO) -> bool:
        return session.query(QuestionDB).filter(and_(QuestionDB.text == question_input.question,
                                                     QuestionDB.answer == question_input.answer,
                                                     QuestionDB.date == question_input.created_at)).first() is not None


Base.metadata.create_all(engine)
