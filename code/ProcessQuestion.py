import math, nltk
import numpy as np
from Utilities import Utilities
from nltk.corpus import stopwords, wordnet
from nltk import pos_tag,ne_chunk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, SnowballStemmer

class ProcessQuestion:
    def __init__(self, question, remove_stopwords = True):
        self.question = question
        self.Atype = self.determineAnswerType(question)
    def determineAnswerType(self, question):
        questionTaggers = ['WP','WDT','WP$','WRB']
        qPOS = pos_tag(word_tokenize(question))
        qTag = None

        for token in qPOS:
            if token[1] in questionTaggers:
                qTag = token[0].lower()
                break
        
        if(qTag == None):
            if len(qPOS) > 1:
                if qPOS[1][1].lower() in ['is','are','can','should']:
                    qTag = "YESNO"
        #who/where/what/why/when/is/are/can/should
        if qTag == "who":
            return "PERSON"
        elif qTag == "where":
            return "LOCATION"
        elif qTag == "when":
            return "DATE"
        elif qTag == "what":
            # Defination type question
            # If question of type whd modal noun? its a defination question
            qTok = self.getContinuousChunk(question)
            #print(qTok)
            if(len(qTok) == 4):
                if qTok[1][1] in ['is','are','was','were'] and qTok[2][0] in ["NN","NNS","NNP","NNPS"]:
                    self.question = " ".join([qTok[0][1],qTok[2][1],qTok[1][1]])
                    #print("Type of question","Definition",self.question)
                    return "DEFINITION"

            # ELSE USE FIRST HEAD WORD
            for token in qPOS:
                if token[0].lower() in ["city","place","country"]:
                    return "LOCATION"
                elif token[0].lower() in ["company","industry","organization"]:
                    return "ORGANIZATION"
                elif token[1] in ["NN","NNS"]:
                    return "FULL"
                elif token[1] in ["NNP","NNPS"]:
                    return "FULL"
            return "FULL"
        elif qTag == "how":
            if len(qPOS)>1:
                t2 = qPOS[2]
                if t2[0].lower() in ["few","great","little","many","much"]:
                    return "QUANTITY"
                elif t2[0].lower() in ["tall","wide","big","far"]:
                    return "LINEAR_MEASURE"
            return "FULL"
        else:
            return "FULL"