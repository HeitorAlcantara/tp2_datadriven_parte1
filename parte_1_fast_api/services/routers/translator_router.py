from fastapi import APIRouter
from transformers import pipeline
from models.translator_model import TranslateModel

translator_router = APIRouter()


def generate_response(message: str):
    generator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")
    return generator(message)


@translator_router.post("/translate")
async def translate(body: TranslateModel):
    response = generate_response(body.en_phrase)
    return {"user": body.en_phrase, "assistant": response[0]['translation_text']} # A ordem das respostas vem ao contrário...