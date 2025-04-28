from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, Trainer, TrainingArguments, DataCollatorForSeq2Seq
from backend.data_loader import load_data
from backend.preprocess import preprocess_data

def train_model():
    model_name = "t5-small"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    
    dataset = load_data()
    tokenized_datasets = preprocess_data(dataset, tokenizer)
    
    # Set minimal batch size and epochs
    training_args = TrainingArguments(
        output_dir="./results",
        save_strategy="epoch",
        per_device_train_batch_size=2,  # Very small batch size
        per_device_eval_batch_size=2,  # Very small batch size
        num_train_epochs=5,  # Only 5 epoch for minimal training
        weight_decay=0.01,
        logging_dir="./logs",
        fp16=True,  # Using mixed precision for faster training
    )
    
    data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["validation"],
        tokenizer=tokenizer,
        data_collator=data_collator,
    )
    
    trainer.train()
    model.save_pretrained("./text_summarization_model")
    tokenizer.save_pretrained("./text_summarization_model")
     