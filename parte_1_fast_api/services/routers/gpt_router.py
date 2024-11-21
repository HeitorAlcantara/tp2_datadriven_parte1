from fastapi import APIRouter
from transformers import pipeline
from models.gpt_model import AutoCompleteModel

gpt_router = APIRouter()


def generate_response(message: str):
    generator = pipeline("text-generation", model="gpt2")
    return generator(message)


@gpt_router.post("/autocomplete")
async def autocomplete(body: AutoCompleteModel):
    response = generate_response(body.phrase)
    return {"assistant": response[0]['generated_text']}