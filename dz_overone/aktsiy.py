stock_1 = ['Adidas','Nike','Apple','Samsung']
stock_2 = ['Nokia','LG','Tesla','Amazon']
price_1 = [100,200,300,400]
price_2 = [200,250,500,450]

stock_1.extend(stock_2)
price_1.extend(price_2)

d = dict(zip(stock_1,price_1))
stock_list_1 = list(d.items())
stock_list_1.sort(key=lambda i: i[1])

for i in stock_list_1:
    print('Стоимость акции ',i[0],':',i[1], 'долларов')


