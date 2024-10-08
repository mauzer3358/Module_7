from pprint import pprint

# Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл
# с продуктами.
#
# Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables')
# и обладать следующими свойствами:
# Атрибут name - название продукта (строка).
# Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
# Атрибут category - категория товара (строка).
# Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
# Все данные в строке разделены запятой с пробелами.
#


class Product:
    def __init__(self, name, weight, category=''):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f' {self.name}, {self.weight}, {self.category}'

# Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
# Инкапсулированный атрибут __file_name = 'products.txt'.

# Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
# Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
# Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        self.a = ''

    # Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его и
    # возвращает единую строку со всеми товарами из файла __file_name.

    def get_products(self):
        file = open(self.__file_name,'r')
        self.a = file.read()
        file.close()
        return self.a

    # Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
    # Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
    # Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .

    def add(self,*products):
        self.products = products
        self.text = self.get_products()
        file = open(self.__file_name, 'a')

        for i in self.products:
            self.name = str(i).split(',')[0]

            if self.name in self.text:
                print(f'Продукт{str(i)} уже есть в магазине')
            else:
                file.write(f'{str(i)}\n')
        file.close()




s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())