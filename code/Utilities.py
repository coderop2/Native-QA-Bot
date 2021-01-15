import math

class Utilities:
    def __init__(self, msg):
        self.message = msg
        
    def getSimilarParagraph(self, wf, idf):    
        VectorDistance = 0
        for word in wf.keys():
            if word in idf.keys():
                VectorDistance += math.pow(wf[word]*idf[word],2)
        VectorDistance = math.pow(VectorDistance,0.5)
        return VectorDistance