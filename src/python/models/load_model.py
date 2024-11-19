from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering

model_name = "lfcc/bert-portuguese-squad2"

def load_model():
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
    return model, tokenizer, nlp