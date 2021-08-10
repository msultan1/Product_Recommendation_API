from Model import ModelLoader

class ModelHandler :
    ModelFilePath = "..\\Model\\trained_model.sav"
    MyModelLoader = None
    def __init__(self):
        self.MyModelLoader = ModelLoader.ModelLoader(self.ModelFilePath)

    def Predict (self, myCustmorInfo):
        return self.MyModelLoader.Exec(myCustmorInfo)

