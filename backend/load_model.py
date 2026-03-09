from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_PATH = "./final-mental-model"

#Used to Load the Tokenizer
tokenizer=AutoTokenizer.from_pretrained(MODEL_PATH)

#Used to load the fine tuned model
model=AutoModelForCausalLM.from_pretrained(MODEL_PATH,torch_dtype=torch.float16,device_map="auto")

#The Function Modulde to generate the output 
def generate_response(prompt):

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=120,
        temperature=0.7,
        top_p=0.9
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)