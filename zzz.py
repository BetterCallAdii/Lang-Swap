from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load the model
model_name = "AI4Bharat/indictrans2-en-hi"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Input text
text = "Attack on Titan is a Japanese dark fantasy anime television series."

# Tokenize and translate
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
output = model.generate(**inputs, max_length=256)
translated = tokenizer.decode(output[0], skip_special_tokens=True)

print(translated)
