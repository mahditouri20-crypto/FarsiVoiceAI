import re


def normalize_numbers(text):
    numbers = {
        "0": "۰",
        "1": "۱",
        "2": "۲",
        "3": "۳",
        "4": "۴",
        "5": "۵",
        "6": "۶",
        "7": "۷",
        "8": "۸",
        "9": "۹",
    }

    for en, fa in numbers.items():
        text = text.replace(en, fa)

    return text


def clean_text(text):
    # یکسان‌سازی فاصله‌های معمولی
    text = re.sub(r"[ \t]+", " ", text)

    # تبدیل سه نقطه به علامت مکث
    text = text.replace("...", "…")

    # حذف فاصله قبل از علائم نگارشی
    text = re.sub(r"\s+([،؛؟!.:])", r"\1", text)

    # افزودن فاصله بعد از علائم نگارشی
    text = re.sub(r"([،؛؟!])(?=\S)", r"\1 ", text)

    # تبدیل اعداد انگلیسی به فارسی
    text = normalize_numbers(text)

    # فاصله بعد از نقطه در صورت چسبیدن جمله بعدی
    text = re.sub(r"\.(?=\S)", ". ", text)

    # حذف فاصله‌های تکراری
    text = re.sub(r" {2,}", " ", text)

    # حذف فاصله ابتدای خطوط
    text = re.sub(r"\n[ \t]+", "\n", text)

    # حذف خطوط خالی اضافی
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def prepare_text(text):
    return clean_text(text)


if __name__ == "__main__":
    sample = """
    ایران امروز با ایران دیروز فرق کرده است...
    در سال 1357 اتفاقات بزرگی رخ داد.
    """

    print(clean_text(sample))
