
class AnonymousSurvey():

    def __init__(self,question):
        self.question = question
        self.response = []
    
    def show_question(self):
        print(f'{self.question}')
    
    def add_response(self,new_response):
        self.response.append(new_response)
    
    def show_response(self):
        for response in self.response:
            print(f' - {response}')



