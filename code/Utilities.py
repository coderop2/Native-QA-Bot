import math

class Utilities:
    # def __init__(self, msg):
    #     self.message = msg
        
    def ComputeVector(self, wf, idf):    
        VectorDistance = 0
        for word in wf.keys():
            if word in idf.keys():
                VectorDistance += math.pow(wf[word]*idf[word],2)
        VectorDistance = math.pow(VectorDistance,0.5)
        return VectorDistance
    
    def GetClosestContextFile(self, question):
        closestvector = 0
        obj = 1
        return closestvector, obj
