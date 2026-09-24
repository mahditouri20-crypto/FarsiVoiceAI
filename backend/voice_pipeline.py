from text_cleaner import clean_text
from prosody import add_prosody


def prepare_voice_text(text):
    cleaned = clean_text(text)
    voiced = add_prosody(cleaned)

    return voiced


if __name__ == "__main__":
    text = """
    ایران امروز، داستانی از تغییر و تحول است...
    اما آیا می‌توان گذشته را فراموش کرد؟
    """

    result = prepare_voice_text(text)

    print(result)
