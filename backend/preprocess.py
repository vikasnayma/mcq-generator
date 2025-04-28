from transformers import AutoTokenizer

def preprocess_data(dataset, tokenizer, max_input_length=128, max_target_length=32):  # Reduced sequence length
    def preprocess_function(examples):
        inputs = [doc for doc in examples["article"]]
        targets = [doc for doc in examples["highlights"]]
        model_inputs = tokenizer(inputs, max_length=max_input_length, truncation=True, padding="max_length")
        labels = tokenizer(targets, max_length=max_target_length, truncation=True, padding="max_length")
        model_inputs["labels"] = labels["input_ids"]
        return model_inputs
    
    tokenized_datasets = dataset.map(preprocess_function, batched=True)
    return tokenized_datasets
