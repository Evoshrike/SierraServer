import random 
import torch
from transformers import BertTokenizer, BertForSequenceClassification

tokenizer = BertTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

model = BertForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

def get_category(question: str):
    with torch.no_grad():
        inputs = tokenizer(question, return_tensors="pt")
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits).item()

    labels = ['very negative', 'negative', 'neutral', 'positive', 'very positive']
    predicted_label = labels[predicted_class]
    return predicted_label
