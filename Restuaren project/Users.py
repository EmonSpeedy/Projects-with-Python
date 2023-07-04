from abc import ABC, abstractmethod
class User:
    def __init__(self, name, phone, email, address) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address,money) -> None:
        self.wallet = money
        self.__order = None
        self.due_amount = 0
        super().__init__(name, phone, email, address)

    @property
    def order(self):
        return self.__order
    

    @order.setter
    def order(self, order):
        self.__order = order

    def place_order(self, order):
        self.order = order
        self.bill_due = order.bill
        print(f'{self.name} placed an order with bill {order.bill}')

    def pay_for_order(self, amount):
        pass

    def give_tips(self, tips_amount):
        pass

    def write_review(self, stars):
        pass

class Employee(User):
    def __init__(self, name, salary, joining_date, dept, phone, email, address) -> None:
        super().__init__(name, phone, email, address)
        self.joining_date = joining_date
        self.dept = dept
        self.salary = salary
        self.due = salary

    def receive_salary(self):
        self.due = 0

class Chef(Employee):
    def __init__(self, name, salary, joining_date, dept, phone, email, address, cooking_item) -> None:
        super().__init__(name, salary, joining_date, dept, phone, email, address)
        self.cooking_item = cooking_item

class Server(Employee):
    def __init__(self, name, salary, joining_date, dept, phone, email, address) -> None:
        super().__init__(name, salary, joining_date, dept, phone, email, address)
        self.tips_earn = 0

    def take_order(self, order):
        pass

    def transfer_order(self, order):
        pass

    def serve_food(self, order):
        pass

    def receive_tips(self, tips_amount):
        self.tips_earn += tips_amount

class Manager(Employee):
    def __init__(self, name, salary, joining_date, dept, phone, email, address) -> None:
        super().__init__(name, salary, joining_date, dept, phone, email, address)

        