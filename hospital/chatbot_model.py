from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("medalpaca/medalpaca-13b")
model = AutoModelForCausalLM.from_pretrained("medalpaca/medalpaca-13b")