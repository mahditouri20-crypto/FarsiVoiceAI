from fastapi import FastAPI
from pydantic import BaseModel
import edge_tts
import uuid
from text_cleaner import prepare_text

app = FastAPI(title="FarsiVoiceAI")


class TextRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return {
        "message": "FarsiVoice AI آماده است"
    }


@app.post("/text")
async def process_text(request: TextRequest):
    filename = f"voice_{uuid.uuid4().hex}.mp3"

    clean_text = prepare_text(request.text)

    communicate = edge_tts.Communicate(
        clean_text,
        "fa-IR-FaridNeural"
    )

    await communicate.save(filename)

    return {
        "original_text": clean_text,
        "audio_file": filename,
        "message": "صدا ساخته شد"
    }
