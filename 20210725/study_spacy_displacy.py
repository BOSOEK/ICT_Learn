import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_md")
# doc = nlp("I own a ginger cat.")
doc = nlp("Bill Gates is the CEO of Microsoft.")

# displacy.serve(doc, style="dep", port=5005)
# dependency parse를 시각화

displacy.serve(doc, style="ent")
# entity parse 시각화