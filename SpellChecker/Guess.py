

class Guess:
    def __init__(self, modelPath):
        self.modelPath = modelPath

    def print(self):
        print("modelSuggestor: " + self.modelName)
        print("fileName: " + self.fileName)