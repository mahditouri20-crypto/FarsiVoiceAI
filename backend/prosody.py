import re

def add_prosody(text):
    # مکث کوتاه بعد از ویرگول
    text = text.replace("،", "، <break_short>")

    # مکث متوسط بعد از نقطه
    text = text.replace(".", ". <break_medium>")

    # مکث سوالی
    text = text.replace("؟", "؟ <break_long>")

    # مکث تعجبی
    text = text.replace("!", "! <break_medium>")

    # مکث طبیعی برای سه نقطه
    text = text.replace("…", "… <break_long>")

    return text


if __name__ == "__main__":
    sample = "ایران امروز، داستانی از تغییر و تحول است… اما آیا می‌توان گذشته را فراموش کرد؟"

    print(add_prosody(sample))
