from transformers import CanineTokenizer, CanineForTokenClassification

MODEL = "PedramR/canine-fa-diacritizer"

MARKS = {
    "FATHA": "َ",
    "DAMMA": "ُ",
    "KASRA": "ِ",
    "SOKUN": "ْ",
    "SHADDA": "ّ",
    "SHADDA_FATHA": "َّ",
    "SHADDA_DAMMA": "ُّ",
    "SHADDA_KASRA": "ِّ",
    "FATHATAN": "ً",
}

tokenizer = CanineTokenizer.from_pretrained(MODEL)
model = CanineForTokenClassification.from_pretrained(MODEL).eval()

texts = [
    "مرد از خانه بیرون رفت.",
    "او مُرد و همه ناراحت شدند.",
    "شیر در جنگل زندگی می‌کند.",
    "شیر را در لیوان ریخت.",
    "علم و دانش بسیار ارزشمند است.",
    "او گُل را از باغ چید.",
    "کشاورز زمین را کِشت کرد.",
    "او دشمن خود را کُشت.",
]

for text in texts:
    enc = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=2048,
    )

    preds = model(**enc).logits.argmax(-1)[0].tolist()
    id2label = model.config.id2label
    char_preds = preds[1:1 + len(text)]

    output = []

    for ch, pid in zip(text, char_preds):
        output.append(ch)
        output.append(MARKS.get(id2label[pid], ""))

    print("INPUT :", text)
    print("OUTPUT:", "".join(output))
    print()
