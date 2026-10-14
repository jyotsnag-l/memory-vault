from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from rag import ask_question


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Memory Vault API is running"}


@app.post("/ask")
def ask(request: QuestionRequest):

    answer = ask_question(request.question)

    return {
        "answer": answer
    }