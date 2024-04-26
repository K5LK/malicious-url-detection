# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import numpy as np
import torch

# Check if CUDA is available
if torch.cuda.is_available():
    # Choose a specific GPU or use the default
    device = torch.device("cuda:0")
else:
# Or CPU
    device = torch.device("cpu")

tokenizer = AutoTokenizer.from_pretrained("kmack/malicious-url-detection")
model = AutoModelForSequenceClassification.from_pretrained("kmack/malicious-url-detection")

# set Model to cude
model = model.to(device)

# predict function
def get_predit(input_text: str) -> dict:
    label2id = model.config.label2id
    inputs = tokenizer(input_text, return_tensors='pt', truncation=True)
    inputs = inputs.to(device)
    outputs = model(**inputs)
    logits = outputs.logits
    sigmoid = torch.nn.Sigmoid()
    probs = sigmoid(logits.squeeze().cpu())
    probs = probs.detach().numpy()
    for i, k in enumerate(label2id.keys()):
        label2id[k] = probs[i]
    label2id = {k: float(v) for k, v in sorted(label2id.items(), key=lambda item: item[1].item(), reverse=True)}
    return label2id


