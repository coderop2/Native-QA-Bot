import numpy as np
from nltk.corpus import stopwords
from nltk import pos_tag,ne_chunk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, SnowballStemmer

class ProcessContext:
    def __init__(self, contextParas, remove_stopwords = True):
        self.sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        self.remove_stopwords = remove_stopwords
        self.stopwords = stopwords.words('english')
        self.stemmer = PorterStemmer()
        self.numOfParas = len(contextParas)
        self.paraInfo, self.vocab, self.processed_vocab = self.processParas(contextParas)
        self.contextIDF = {}
        del contextParas
    
    def processParas(self, paras):
        docs = {}
        vocab = set()
        processed_vocab = set()
        for index in range(self.numOfParas):
            docs[index] = {}
            docs[index]['para'] = paras[index]
            docs[index]['paraWords'] = word_tokenize(paras[index])
            vocab.update(docs[index]['paraWords'])
            docs[index]['paraSentences'] = self.sent_tokenizer.tokenize(paras[index])
            wf, processed_sentences, pv = self.processSentences(docs[index]['paraSentences'])
            docs[index]['paraWF'] = wf
            docs[index]['paraProcessedSentences'] = processed_sentences
            docs[index]['paraPV'] = pv
            processed_vocab.update(pv)
            
        idf = {}
        for index in range(self.numOfParas):
            for word in docs[index]['paraPV']:
                if idf.get(word,0) == 0:
                    idf[word] = 1
                else:
                    idf[word] += 1
        return docs, vocab, processed_vocab
    
    def processSentences(self, sentences):
        wf = {}
        processed_sentences = []
        processed_vocab = set()
        for sent in sentences:
            processed_sentence = []
            words = word_tokenize(sent)
            for word in words:
                if not self.remove_stopwords:
                    continue
                else:
                    if word in self.stopwords:
                        continue
                word = self.stemmer.stem(word)
                if wf.get(word, 0) == 0:
                    wf[word] = 1
                else:
                    wf[word] += 1
                processed_sentence.append(word)
            processed_vocab.update(processed_sentence)
            processed_sentences.append(" ".join(processed_sentence))
        return wf, processed_sentence, processed_vocab