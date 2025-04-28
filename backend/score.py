import pandas as pd
from evaluate import load

# Load ROUGE Metric
rouge = load("rouge")

# Read the CSV File
df = pd.read_csv('output.csv')

# Calculate ROUGE Score for Summarization
rouge_scores = rouge.compute(
    predictions=df['Generated Summary'].tolist(),
    references=df['Actual Text'].tolist()
)

# Display ROUGE Scores
print("----- Text Summarization Scores -----")
print("ROUGE-1 Score:", round(rouge_scores['rouge1'], 2))
print("ROUGE-2 Score:", round(rouge_scores['rouge2'], 2))
print("ROUGE-L Score:", round(rouge_scores['rougeL'], 2))
