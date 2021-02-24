from app.utils.naming_algo import NamingAlgo 

class GenerateNames:
    stringList = []
    appIndex = 0
    phraseIndex = 0
    descriptionPhrases = []
    appDescription = ''
    
    def __init__(self, app_concept):
        self.app_concept = app_concept
        
    def split_to_list(self):
        string_list = self.app_concept.split(" ")
        GenerateNames.stringList = list(filter(None, string_list))
        app_index = 0
        try:
            app_index = GenerateNames.stringList.index("app")
        except ValueError:
            app_index = GenerateNames.stringList.index("business")
        
        app_description = GenerateNames.stringList[app_index-1:app_index]
        
        GenerateNames.appIndex = app_index
        GenerateNames.appDescription = app_description
        
        return app_description
    
    def get_phrase_index(self):
        ws_list = ['where', 'that', 'that/where']
        
        ws_index = 0
        
        for ws in ws_list:
            try:
                ws_index = GenerateNames.stringList.index(ws)
            except:
                pass
        
        GenerateNames.phraseIndex = ws_index
        return GenerateNames.phraseIndex
    
    def get_description_phrase(self):
        if GenerateNames.phraseIndex  != 0:
            description_phrase = GenerateNames.stringList[GenerateNames.phraseIndex+1:]
            GenerateNames.descriptionPhrases = description_phrase
        else:
            description_phrase = GenerateNames.stringList[GenerateNames.appIndex+1:]
            GenerateNames.descriptionPhrases = description_phrase
        
        return GenerateNames.descriptionPhrases
    
    def run_algo(self, name_length):
        self.split_to_list()
        self.get_phrase_index()
        self.get_description_phrase()
        length = 10
        generated_names = NamingAlgo.AlgoEntry(self.descriptionPhrases, self.appDescription, length)
        
        return generated_names
        
    