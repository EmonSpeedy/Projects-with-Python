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
        self.total_sell_product = 0
        self.total_sell_amount = 0
        self.total_profit_amount = 0
        super().__init__(email, password)
    
    def shop_info(self, store):
        all_seller_id = store.total_product.keys()
        # print(all_seller_id)
        for seller_id in all_seller_id:
            sell_info = store.total_product[seller_id][0]
            # print(sell_info)
            self.total_sell_product += sell_info['Total sell products']
            self.total_sell_amount += sell_info['Total sell amount']
            self.total_profit_amount += sell_info['Total profit amount']

        sell_info = {
            "Total sold" : self.total_sell_product,
            "Total amount" : self.total_sell_amount,
            "Total profit amount" : self.total_profit_amount
        }
        return sell_info
    

class Customer(Person):
    def __init__(self, email, password) -> None:
        self.total_buy_amount = 0
        self.total_buy_products = 0
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
                
    def buy_product(self, store, seller_id, product_name, quantity):
        flag = 0
        for index in range(1, len(store.total_product[seller_id])):
            product = store.total_product[seller_id][index]
            if product['product_name'] == product_name:
                flag = 1
                if product['product_quantity'] >= quantity:
                    product["product_quantity"] -= quantity
                    self.total_buy_products += quantity
                    self.total_buy_amount += (quantity * product["product_price"])
                    seller = store.total_product[seller_id][0]
                    seller['Total sell products'] += quantity
                    seller['Total sell amount'] += (quantity * product["product_price"])
                    seller['Total profit amount'] += ((quantity * product["product_price"]) * 10)/100
                else:
                    print('Insufficiant quantity')

        if flag == 0:
            print('Product not found')
        # print(store.total_product[seller_id])    


class Seller(Person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)

    def add_product(self, store, name, price, quantity):
        product = Product(name, price, quantity)
        store.add_to_store(self.user_id, product)

    def sell_info(self, store):
        print(store.total_product[self.user_id][0])
        
        

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

# customer1.show_products(store)
# print(customer1.total_buy_amount, customer1.total_buy_products)
customer1.buy_product(store, 100, "Iphone X", 4)
# print()
# print()
# customer1.show_products(store)
# print(customer1.total_buy_amount, customer1.total_buy_products)
# store.show_details()

# seller1.sell_info(store)
# seller2.sell_info(store)
# seller3.sell_info(store)
customer1.buy_product(store, 101, 'Samsung S9', 5)
# print('\n')
# seller1.sell_info(store)
# seller2.sell_info(store)
# seller3.sell_info(store)

owner = Owner('owner@gmail.com', 11223)
print(owner.shop_info(store))
