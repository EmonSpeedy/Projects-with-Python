class Person:
    id = 100
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password
        self.user_id = Person.generate_id() 
    @classmethod
    def generate_id(self):
        iD = self.id
        self.id += 1
        return iD
    
    def __repr__(self) -> str:
        return f'Seller Id : {self.user_id} || Email : {self.email}'
    
class Product:
    def __init__(self, name, price, quantity) -> None:
        self.product_name = name
        self.product_price = price
        self.product_quantity = quantity

    def __repr__(self) -> str:
        return f'Product name : {self.product_name}, Product price: {self.product_price}, Product quantity: {self.product_quantity}'


class Store:
    def __init__(self) -> None:
        self.total_product = {}

    def add_to_store(self, seller_id, product):
        productdict = vars(product)
        # print(productdict)
        if seller_id not in self.total_product:
            self.total_product[seller_id] = []
            seller_info = {}
            seller_info['Total sell products'] = 0
            seller_info['Total sell amount'] = 0
            seller_info['Total profit amount'] = 0
            self.total_product[seller_id].append(seller_info)
            

        self.total_product[seller_id].append(productdict)

    def show_details(self):
        print(self.total_product)


class Owner(Person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)

class Customer(Person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)

    def show_products(self, store):
        all_ids = store.total_product.keys()
        for sellerId in all_ids:
            print('Seller ID : ', sellerId)
            print('-------------')
            for product in range(1, len(store.total_product[sellerId])):
                Product = store.total_product[sellerId][product]
                # print(Product['product_name'])
                print(f"Product Name: {Product['product_name']}, Price: {Product['product_price']}, Quantity: {Product['product_quantity']}")
                


class Seller(Person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)

    def add_product(self, store, name, price, quantity):
        product = Product(name, price, quantity)
        store.add_to_store(self.user_id, product)
        

store = Store()

seller1 = Seller('one@gmail.com', 1234)
seller2 = Seller('two@gmail.com', 1265)
seller3 = Seller('three@gmail.com', 1233)

seller1.add_product(store, 'Iphone X', 90000, 12)
seller1.add_product(store, 'Iphone 11', 100000, 10)

seller2.add_product(store, 'Samsung S10', 90000, 12)
seller2.add_product(store, 'Samsung S9', 70000, 16)

seller3.add_product(store, 'Oppo Reno 5', 35000, 17)
seller3.add_product(store, 'Poco M20 Pro', 25000, 18)

customer1 = Customer('buyer@gmail.com', 7855)

customer1.show_products(store)

# store.show_details()
