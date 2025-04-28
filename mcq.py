import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk import pos_tag
import random
from inference import extract_keywords

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Helper functions
def get_sentence_with_keyword(keyword, sentences, used_sentences):
    for sent in sentences:
        if keyword in sent.lower() and sent not in used_sentences:
            return sent
    return None

def make_question(sentence):
    words = word_tokenize(sentence)
    tagged = pos_tag(words)

    for tag_type in ['NN', 'NNS', 'NNP', 'VB', 'VBD', 'JJ']:
        for i, (word, tag) in enumerate(tagged):
            if tag.startswith(tag_type) and word.lower() not in ['is', 'are', 'was', 'were']:
                question = sentence.replace(word, '______', 1)
                return question, word
    word = random.choice(words)
    return sentence.replace(word, '______', 1), word

def get_distractors(correct_word):
    distractors = set()
    synsets = wordnet.synsets(correct_word)
    for syn in synsets:
        for lemma in syn.lemmas():
            word = lemma.name().replace('_', ' ')
            if word.lower() != correct_word.lower():
                distractors.add(word)
            if len(distractors) >= 3:
                break
        if len(distractors) >= 3:
            break
    return list(distractors)

# 🆕 Main function to generate MCQs
def generate_mcqs(text):
    sentences = sent_tokenize(text)
    keywords = extract_keywords(text)  # Ensure this returns the list of keywords
    used_sentences = set()  # Track used sentences
    mcqs = []

    for i, keyword in enumerate(keywords):
        sentence = get_sentence_with_keyword(keyword, sentences, used_sentences)
        if sentence:
            question, answer = make_question(sentence)
            distractors = get_distractors(answer)
            options = distractors + [answer]
            options = list(set(options))[:4]  # Ensure we have exactly 4 options
            random.shuffle(options)

            mcqs.append({
                "question": question,
                "options": options,
                "answer": answer
            })

            # Mark the sentence as used
            used_sentences.add(sentence)

    return mcqs
