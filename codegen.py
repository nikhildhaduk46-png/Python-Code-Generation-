import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load model and tokenizer
model_name = "Salesforce/codegen-350M-mono"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Move to GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Prompt for code generation
prompt = """
# Python function to check if a number is prime
"""

inputs = tokenizer(prompt, return_tensors="pt").to(device)

# Generate code
outputs = model.generate(
    **inputs,
    max_length=150,
    temperature=0.2,
    top_p=0.95,
    do_sample=True
)

# Decode output
generated_code = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated_code)

from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="Salesforce/codegen-350M-mono",
    device=0 if torch.cuda.is_available() else -1
)

prompt = "# Python function to reverse a string\n"

result = generator(
    prompt,
    max_length=120,
    temperature=0.2,
    top_p=0.95
)

print(result[0]["generated_text"])

