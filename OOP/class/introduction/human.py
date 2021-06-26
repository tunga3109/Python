class Human:
    #Статические поля - то,что под классом
    default_name = 'No name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        #Динамические свойства - то,что под объектом(методом)
        #Публичные атрибуты
        self.name = name
        self.age = age
        #Привытные атрибуты(с 2-мя нижними подчеркиваниями __ )
        self.__money = 0
        self.__house = None

    #Метод объекта
    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Money: {self.__money}')
        print(f'House: {self.__house}')

    #Статический метод
    @staticmethod
    def default_info():
        print(f'Default_name: {Human.default_name}')
        print(f'Default_age: {Human.default_age}')
    
    def earn_money(self, amount):
        self.__money += amount
        print(f'Earned {amount} money! Current value {self.__money}')

    def buy_house(self,house,discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house,price)
        else:
            print('Not enough money')

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house



class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price
    
    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f'final price:{final_price}')
        return final_price


if __name__ == "__main__":
    print(Human.default_name)

    fedor = Human('Fedor',22)
    fedor.info()

    fedor.earn_money(10000)
    fedor.info()

    house = House(100, 14000)
    fedor.buy_house(house,10)










if __name__ == "__main__":
    # Запуск статического поля
    print(Human.default_name)

    
    # Запуск метода объекта
    fedor = Human('Федор',32)
    fedor.info()
    
    # Запуск статического метода
    Human.default_info()