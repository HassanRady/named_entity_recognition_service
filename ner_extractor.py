import spacy

nlp = spacy.load("en_core_web_sm")
nlp.max_length = 1170000

def preprocess(json_data):
  text = json_data['text']
  return " ".join(text)

def get_ner(text):
  doc = nlp(text)
  return [ent.text for ent in doc.ents]

def pipeline(text) -> dict:
  return {"output": get_ner(text)}

