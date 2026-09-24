import subprocess
import os

MODEL = "fa_IR-gyro-medium"

def generate_voice(text, output_wav="output.wav"):
    raw_file = output_wav + ".raw"

    subprocess.run(
        ["piper", "-m", MODEL, "-f", raw_file, "--", text],
        check=True
    )

    subprocess.run(
        [
            "ffmpeg", "-y",
            "-f", "f32le",
            "-ar", "22050",
            "-ac", "1",
            "-i", raw_file,
            "-c:a", "pcm_s16le",
            output_wav
        ],
        check=True
    )

    os.remove(raw_file)

if __name__ == "__main__":
    generate_voice("سلام دنیا، من آواگویا هستم.", "output.wav")
    print("فایل صوتی ساخته شد: output.wav")
