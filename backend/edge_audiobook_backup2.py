import asyncio
import edge_tts
import os

VOICE = "fa-IR-FaridNeural"
RATE = "-10%"
PITCH = "-8Hz"

INPUT_FILE = "book.txt"
OUTPUT_FILE = "audiobook_pro.mp3"

async def main():
    if not os.path.exists(INPUT_FILE):
        print("❌ book.txt پیدا نشد")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        text = f.read().strip()

    if not text:
        print("❌ book.txt خالی است")
        return

    print("🎙️ در حال ساخت کتاب صوتی...")
    
    communicate = edge_tts.Communicate(
        text,
        voice=VOICE,
        rate=RATE,
        pitch=PITCH
    )

    await communicate.save(OUTPUT_FILE)

    print(f"✅ تمام شد: {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(main())
