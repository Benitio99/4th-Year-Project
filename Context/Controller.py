###

###
import sklearn
import transformers
import joblib
from nltk.corpus import wordnet

MODELNAME = "bert-based-uncased"
MODELPATH = "data/model.joblib"
PIPELINETYPE = "fill-mask"
class Controller:
    

    def __init__(self, input: str):
        self.input = input
        self.model
        self.tokenizer
        self.pipeline
        self.modelResults
        self.worNet = wordnet
        self.modelResults
        self.modelGuessSynset 
        self.editDistances 
        classifier = transformers.pipelines
        model = loadBaseModel()
        pipeline = createPipeline()
        processData(input)

    
    def loadTokenizer():
        pass

    def loadBaseTokenizer():
        tokenizer = transformers.BertTokenizer.from_pretrained(MODELNAME)
        return tokenizer

    def loadModel(path):
        return joblib.load(path)

    def loadBaseModel():
        classifier = transformers.BertForMaskedLM.from_pretrained(MODELNAME)
        return classifier

    def createPipeline():
        pipeline = transformers.pipeline(PIPELINETYPE)
        return pipeline

    def fitData(input):
        pass

    def getError(input):
        pass

    def getSynset(input):
        wordList = wordnet.synsets(input)
        return wordList

    def inputText(input: str):
        pass

    def processData(self, input):
        self.modelResults = getModelGuesses(input)
        self.modelGuessSynset = getSynset(contextError)
        self.editDistances = getEditDistanceList(contextError)
        modelResults = model.fit(input)
        for result in modelResults:
            if result.idfoundIn(editDistances):
                return modelResult
            else:
                for item in contextErrorSynset:
                    if item.isFoundIn(editDistances):
                        return item
