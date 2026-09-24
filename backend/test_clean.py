import re

def clean_text(text):
    # حذف فاصله‌های اضافی
    text = re.sub(r'\s+', ' ', text)

    # تبدیل سه نقطه به مکث
    text = text.replace("...", "…")

    # اصلاح فاصله‌های اطراف علائم نگارشی
    text = re.sub(r'\s*،\s*', '، ', text)
    text = re.sub(r'\s*؛\s*', '؛ ', text)
    text = re.sub(r'\s*؟\s*', '؟ ', text)
    text = re.sub(r'\s*!\s*', '! ', text)
    text = re.sub(r'\s*\.\s*', '. ', text)

    return text.strip()


if __name__ == "__main__":
    sample = """
    ایران امروز، داستانی از تغییر و تحول است...
    اما آیا می‌توان گذشته را فراموش کرد؟
    """

    print(clean_text(sample))
