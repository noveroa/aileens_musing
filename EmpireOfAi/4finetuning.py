"""
Step 4: Fine-Tuning the Model

Fine-tuning involves adapting a pre-trained model (like GPT) to a specific task, such as text generation, summarization, or classification.

* NOTE VERSION OF TRANSFORMERS and the back compatible keras 
Benefits:
    Saves time and resources by leveraging pre-trained knowledge.
    Achieves high performance on specific tasks with minimal labeled data.
Libraries for Fine-Tuning
    Hugging Face Transformers: Provides tools for working with pre-trained models and datasets.
    Datasets: A dataset specific to the task is required for fine-tuning.
"""

from transformers import GPT2Tokenizer, GPT2LMHeadModel 
from transformers import Trainer, TrainingArguments
import torch

# Step 1: Load the tokenizer and model #  load GPT-2's tokenizer and model.
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
tokenizer.add_special_tokens({'pad_token': '[PAD]'})
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Step 2: Prepare the dataset (replace `my_dataset` with your dataset)
# Ensure `my_dataset` is a PyTorch dataset with tokenized input
# Example tokenization
texts = ["Hello, how are you?", "Fine-tuning is fun!"]
encodings = tokenizer(texts, truncation=True, padding=True, return_tensors="pt")
labels = encodings.input_ids.clone()

dataset = torch.utils.data.TensorDataset(encodings.input_ids, labels)

# Step 3: Define training arguments
train_args = TrainingArguments(
    output_dir='./results',        # Directory to save the model
    per_device_train_batch_size=4, # Batch size
    num_train_epochs=1,            # Number of epochs
    save_steps=10_000,             # Steps to save checkpoints
    save_total_limit=2,            # Maximum number of saved checkpoints
    logging_dir='./logs',          # Directory for logs
    logging_steps=500,             # Log every 500 steps
)

# Step 4: Create Trainer and train the model
trainer = Trainer(
    model=model,
    args=train_args,
    train_dataset=dataset,
)

trainer.train()