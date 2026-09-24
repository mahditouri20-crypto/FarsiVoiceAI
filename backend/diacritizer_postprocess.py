import re


def postprocess_diacritics(text):
    """Clean CANINE Persian diacritization output for TTS."""

    # حذف اعراب تکراری
    text = re.sub(r"([ًٌٍَُِّْ])\1+", r"\1", text)

    # حذف ترکیب‌های متناقض
    text = text.replace("کُِ", "کِ")
    text = text.replace("کُِ", "کُ")
    text = text.replace("ُُ", "ُ")
    text = text.replace("ََ", "َ")
    text = text.replace("ِِ", "ِ")

    # حذف سکون در انتهای کلمات
    text = re.sub(r"ْ(?=\s|[.!؟،,:؛]|$)", "", text)

    # حذف سکون قبل از علائم نگارشی
    text = re.sub(r"ْ([.!؟،,:؛])", r"\1", text)

    # حذف فاصله‌های اضافی
    text = re.sub(r"\s+", " ", text).strip()

    return text
