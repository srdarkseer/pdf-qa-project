from transformers import pipeline

def load_model(model_name="distilbert-base-uncased-distilled-squad"):
    nlp = pipeline("question-answering", model=model_name, tokenizer=model_name)
    return nlp

def answer_query(question, context, nlp):
    result = nlp(question=question, context=context)
    return result['answer']
