import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

def summarizer(rawdocs):
    nlp = spacy.load('en_core_web_sm')
    stopwords = list(STOP_WORDS)
    doc = nlp(rawdocs)
    
    word_dict = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            word_dict[word.text.lower()] = word_dict.get(word.text.lower(), 0) + 1

    max_freq = max(word_dict.values())
    word_dict = {word: freq / max_freq for word, freq in word_dict.items()}

    sent_tokens = [sent for sent in doc.sents]
    sent_scores = {}
    for sent in sent_tokens:
        for word in sent:
            if word.text.lower() in word_dict:
                sent_scores[sent] = sent_scores.get(sent, 0) + word_dict[word.text.lower()]

    select_len = int(len(sent_tokens) * 0.3)
    summary = nlargest(select_len, sent_scores, key=sent_scores.get)
    final_summary = [sent.text for sent in summary]
    summary = ' '.join(final_summary)

    original_length = len(rawdocs.split())
    summary_length = len(summary.split())

    return summary, original_length, summary_length
