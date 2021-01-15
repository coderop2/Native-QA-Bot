import numpy as np
from nltk.corpus import stopwords

class ProcessContext:
    def __init__(self, stemmer, contextParas, word_tokenizer, sent_tokenizer):
        self.word_tokenizer