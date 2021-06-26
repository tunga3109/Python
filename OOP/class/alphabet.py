import string
#russkij alphabet
class Alphabet():
    def __init__(self, lang, letters_str):
        self.lang = lang
        self.letters = list(letters_str)
    # Печатаем все буквы алфавита
    def print(self):
        print(self.letters)
    # Возвращаем количество букв в алфавите
    def letters_num(self):
        print(len(self.letters))


a = Alphabet('rus','ahhdjhdfhfdjdfsjkjfdsjsdfjkdfsdjkfs')
a.print()
a.letters_num()

#english alphabet
class EngAlphabet(Alphabet):

    __letters_num = 26 # статическое свойство __letters_num

    def __init__(self):
        super().__init__('en', string.ascii_uppercase)

    # Проверяем, относится ли буква к английскому алфавиту
    def is_en_letter(self,letter):
        if letter.upper() in self.letters:
            return True
        return False

    # Возвращаем количество букв в алфавите #Переопределения метода letters_num()
    def letters_num(self):
        return EngAlphabet.__letters_num
        
    # Печатаем пример текста на английском языке
    @staticmethod
    def example():
        print("English Example:\nDon't judge a book by it's cover.")
    
if __name__ == '__main__':
    eng_alphabet = EngAlphabet()
    eng_alphabet.print()
    print(eng_alphabet.letters_num())
    print(eng_alphabet.is_en_letter('F'))
    print(eng_alphabet.is_en_letter('Щ'))
    EngAlphabet.example()