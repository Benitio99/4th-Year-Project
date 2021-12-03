###

###
import sklearn
import transformers

class Controller:
    

    def __init__(self, input: str):
        self.input = input
        self.modelPath = ""
        self.piplineType = ""
        classifier = transformers.pipelines
        loadModel(modelPath)
        createPipeline(pipelineType)
        loadWordNet(filePath)
        processData(input)

    def fitData(input):
        
        pass

    def getError(input):
        pass

    def getSynset(contextError):
        pass

    def inputText(input: str):
        pass

    def loadModel():
        pass

    def processData(self, input):
        self.contextError = getContextError(input)
        self.contextErrorSynset = getSynset(contextError)
        self.editDistances = getEditDistanceList(contextError)
        self.model = loadModel(modelFilepath)
        modelResults = model.fit(input)
        for result in modelResults:
            if result.idfoundIn(editDistances):
                return modelResult
            else:
                for item in contextErrorSynset:
                    if item.isFoundIn(editDistances):
                        return item
