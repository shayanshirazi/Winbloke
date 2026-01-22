import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("jeff richardson is being too rich in last 3 months")

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)