# Паттерн Фасад

class Builder:
    def build(self):
        print('build....')

class Vendor:
    def give(self):
        print('giving the materials....')

class Investor:

    def invest(self):
        print('invest money....')

    def decline(self):
        print('no invest.....')



class BuildProject:
    
    def __init__(self):

        self.builder = Builder()
        self.vendor = Vendor()
        self.investor = Investor()

    def build_project(self):
        self.builder.build()



    


    

if __name__ == "__main__":
    for i in range(5):

        builder = Builder()
        builder.build()