from Menu import Pizza, Burger, Drinks, Menu
from Restuarent import Restuarent
from Users import Chef, Server, Customer, Manager
from order import Order
def main():
    # adding menu plate
    menu = Menu()
    pizza_1 = Pizza('Shutki Pizza', 550, 'Large', ['Shutki', 'Oil'])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('Alur Pizza', 400, 'Large', ['Potato', 'Oil', 'Onion'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('Daler Pizza', 450, 'Large', ['Dal', 'Oil'])
    menu.add_menu_item('pizza', pizza_3)

    burger_1 = Burger('Naga Burger', 750, 'Chicken', ['Bread', 'Chili'])
    menu.add_menu_item('burger', burger_1)
    burger_2 = Burger('Pudina Burger', 550, 'Meat', ['Bread', 'Chili', 'Pudina'])
    menu.add_menu_item('burger', burger_2)

    drink_1 = Drinks('Coca Cola', 45, True)
    menu.add_menu_item('drinks', drink_1)
    drink_2 = Drinks('Coffee', 120, False)
    menu.add_menu_item('drinks', drink_2)

    # menu.show_menu()

    # adding employees
    res = Restuarent('Food Fair', 500, menu)
    manager = Manager('Kala Mia', 150, 'Jan 1', 'Managing', 1110037, 'kala@mia.com', 'Mohakali')
    res.add_employee('manager', manager)

    chef = Chef('Rustam Baburchi', 200, 'Feb 1', 'Cooking', 2211087, 'Rustam@bab.com', 'Gazipur', 'Everything')
    res.add_employee('chef', chef)

    server = Server('Choto Mia', 100, 'Mar 1', 'Serving', 1197732, 'Chota@mia.com', 'Kalia Pukur')
    res.add_employee('server', server)

    # res.show_employees()

    # customer 1 placing an order
    cus1 = Customer('Sakib', 1128872, 'Sakib@420.com', 'Muradpur', 3000)
    order1 = Order(cus1, [pizza_3, drink_2])
    cus1.pay_for_order(order1)
    res.add_order(order1)
    res.receive_payment(order1, 1000, cus1)
    print('------After first customer------')
    print('Restuarent rev: ', res.revenue,' Restuarent balance : ', res.balance)

    # customer 2 placing an order
    cus2 = Customer('Bushra', 1238971, 'Bushra@720.com', 'Gulistan', 1500)
    order2 = Order(cus2, [pizza_1, burger_1, drink_1])
    cus2.pay_for_order(order2)
    res.add_order(order2)
    res.receive_payment(order2, 1500, cus2)
    print('------After second customer------')
    print('Restuarent rev: ', res.revenue,' Restuarent balance : ', res.balance)

    # pay rent
    res.pay_expense(res.rent, 'Paid Rent')
    print('----------After Rent---------')
    print(f'Revenue: {res.revenue}, Balance : {res.balance}, Expenses : {res.expense}')

    # pay chef's salary
    res.pay_salary(chef)
    print('----------After Salary---------')
    print(f'Revenue: {res.revenue}, Balance : {res.balance}, Expenses : {res.expense}')


main()

