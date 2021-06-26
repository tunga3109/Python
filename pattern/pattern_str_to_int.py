# Паттерн - как из строки получить число

class Old:
    def get(self):
        return '1234'

class New:
    def get(self):
        return 456

class Adapter(New):
    def get(self):
        return str(super(Adapter, self).get())


def main(obj):
    print('result: ' + obj.get())

if __name__ == "__main__":
    obj = Adapter()
    main(obj)
    