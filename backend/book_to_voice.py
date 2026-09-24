import re
import os
import subprocess
import sys

from piper_engine import generate_voice


def split_text(text):
    text = re.sub(r'\s+', ' ', text).strip()

    sentences = re.split(r'(?<=[.!؟؛])\s+', text)

    return [s.strip() for s in sentences if s.strip()]


def make_silence(filename, duration):
    subprocess.run([
        "ffmpeg", "-y",
        "-f", "lavfi",
        "-i", f"anullsrc=r=22050:cl=mono",
        "-t", str(duration),
        "-c:a", "pcm_s16le",
        filename
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def book_to_voice(input_file, output_file="book-output.wav"):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    sentences = split_text(text)

    print(f"تعداد جمله‌ها: {len(sentences)}")

    files = []

    for i, sentence in enumerate(sentences, 1):
        print(f"[{i}/{len(sentences)}] {sentence}")

        voice_file = f".sentence_{i}.wav"
        silence_file = f".silence_{i}.wav"

        generate_voice(sentence, voice_file)

        if i < len(sentences):
            make_silence(silence_file, 0.6)

        files.append(voice_file)

        if i < len(sentences):
            files.append(silence_file)

    list_file = ".concat_list.txt"

    with open(list_file, "w", encoding="utf-8") as f:
        for filename in files:
            f.write(f"file '{os.path.abspath(filename)}'\n")

    subprocess.run([
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", list_file,
        "-c:a", "pcm_s16le",
        output_file
    ], check=True)

    for filename in files:
        if os.path.exists(filename):
            os.remove(filename)

    if os.path.exists(list_file):
        os.remove(list_file)

    print()
    print(f"تمام شد: {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("استفاده:")
        print("python book_to_voice.py book.txt")
        sys.exit(1)

    input_file = sys.argv[1]

    output_file = "book-output.wav"

    if len(sys.argv) >= 3:
        output_file = sys.argv[2]

    book_to_voice(input_file, output_file)
