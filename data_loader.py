from datasets import load_dataset

def load_data():
    dataset = load_dataset("cnn_dailymail", "3.0.0")
    dataset["train"] = dataset["train"].select(range(80))  
    dataset["validation"] = dataset["validation"].select(range(50))  
    return dataset
