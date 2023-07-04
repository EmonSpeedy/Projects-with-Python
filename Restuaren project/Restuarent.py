class Restuarent:
    def __init__(self, name, rent, menu = []) -> None:
        self.name =name
        self.rent = rent
        self.orders = []
        self.chef = None
        self.server = None
        self.manager = None
        self.menu = menu
        self.expense = 0
        self.revenue = 0
        self.balance = 0
        self.profit = 0

    def add_employee(self, employee_type, employee):
        if employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'server':
            self.server = employee
        elif employee_type == 'manager':
            self.manager = employee

    def show_employees(self):
        if self.chef is not None:
            print(f'---------Chef Details--------\nName : {self.chef.name}, Salary : {self.chef.salary}')
        if self.server is not None:
            print(f'-------Server Details-------\n Name : {self.server.name}, Salary : {self.server.salary}')
        if self.manager is not None:
            print(f'-------Manager Details-------\n Name : {self.manager.name}, Salary : {self.manager.salary}')

    def receive_payment(self, order, amount, customer):
        if amount >= order.bill:
            self.revenue += order.bill
            self.balance += order.bill
            customer.due_amount = 0
            return amount - order.bill
        else:
            print('Not enough money')

        
    def add_order(self, order):
        self.orders.append(order)

    def pay_expense(self, amount, description):
        if amount < self.balance:
            self.expense += amount
            self.balance -= amount
            print(f'Expense {amount} for {description}')
        else:
            print(f'Not enough money to pay {amount}')

    def pay_salary(self, employee):
        print(f'Paying salary for {employee.name}, Salary : {employee.salary}')
        if employee.salary < self.balance:
            self.balance -= employee.salary
            self.expense += employee.salary
            employee.receive_salary()
        else:
            print('Not able to pay salary')

