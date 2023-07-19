from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

tokenizer = AutoTokenizer.from_pretrained("ronoys/PyRX", model_max_length=10000000)
model = AutoModelForTokenClassification.from_pretrained("ronoys/PyRX")

def get(sentence):
    ner_model = pipeline(task="ner", model=model, tokenizer=tokenizer)
    val = ner_model(sentence)
    result = []
    currentWord = ""

    for x in val:
        if x["entity"] == "LABEL_1":
            currentWord = x["word"]
        elif x["entity"] == "LABEL_2":
            currentWord += x["word"][2:]
        else:
            result.append(currentWord)
            currentWord = ""
    
    output = [*set(result)]
    while("" in output):
        output.remove("")
    return (output)