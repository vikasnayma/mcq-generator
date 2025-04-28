from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from keybert import KeyBERT
import re

def summarize_text(text, model_path="./text_summarization_model"):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    
    inputs = tokenizer(text, return_tensors="pt", max_length=128, truncation=True)
    summary_ids = model.generate(
        inputs.input_ids,
        max_length=80,
        min_length=50,
        length_penalty=1.0,  
        repetition_penalty=2.0,  
        num_beams=5,  
        early_stopping=True
    )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    return summary

def extract_keywords(text, num_keywords=4):
    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(
        text, 
        keyphrase_ngram_range=(1,2),  
        stop_words='english',  
        top_n=num_keywords,  
        use_mmr=True,  
        diversity=0.3  
    )
    
    raw_keywords = [kw[0] for kw in keywords]
    cleaned_keywords = []
    for kw in raw_keywords:
        # Remove phrases that contain "like" or unwanted prepositions
        if "like" in kw.lower() or "such as" in kw.lower():
            continue
        
        # Remove too short words (less than 3 letters)
        if len(kw.split()) == 1 and len(kw) <= 2:
            continue
        
        # Remove keywords with too many non-alphabetic characters
        if re.search(r"[^a-zA-Z\s]", kw):
            continue

        cleaned_keywords.append(kw.strip())

    # Step 3: keep only the top 'num_keywords'
    extracted_keywords = cleaned_keywords[:num_keywords]
    return extracted_keywords

def find_keyword_sentences(text, keywords):
    sentences = re.split(r'(?<=[.!?]) +', text)  # Split text into sentences
    keyword_sentences = []

    for keyword in keywords:
        for sentence in sentences:
            if keyword.lower() in sentence.lower():
                keyword_sentences.append(sentence.strip())
                break  # Store only the first occurrence per keyword

    return keyword_sentences

def summarize_and_extract(text):
    summary = summarize_text(text)
    keywords = extract_keywords(text)
    keyword_sentences = find_keyword_sentences(text, keywords)
    
    return summary, keywords, keyword_sentences
