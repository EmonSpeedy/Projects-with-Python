class User:
    def __init__(self, name, password) -> None:
        self.name = name
        self.password = password

class Bus:
    def __init__(self, coach, driver, arrival_time, departure_time, destination, to) -> None:
        self.coach = coach
        self.driver = driver
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.destination = destination
        self.to =to
        self.seat = ['empty' for i in range(20)]

class Marsa:
    total_bus = 5
    bus_lists = []
    
    def add_bus(self):
        coach_no = int(input('Enter the bus No : '))
        flag = 1
        for w in self.bus_lists:
            if coach_no == w['coach']:
                print('Bus already added\n')
                flag = 0
                break
        if flag:
            print('Fulfill the following information\n')
            bus_no = int(input('Enter the bus No : '))
            bus_driver = input('Enter the drivers name : ')
            arr_time = input('Enter the arrival time : ')
            dept_time = input('Enter the departure time : ')
            bus_from = input('Enter the starting point : ')
            to = input('Enter the destination : ')
            self.new_bus = Bus(bus_no, bus_driver, arr_time, dept_time, bus_from, to)
            self.bus_lists.append(vars(self.new_bus))
            print('Bus added succesfully\n')

class Counter(Marsa):
    user_lists = []
    def booking_ticket(self):
        bus_no = int(input('Enter the bus No : '))
        dec = False
        for w in self.bus_lists:
            if bus_no == w['coach']:
                dec = True
                pass_name = input('Enter the name : ')
                seat_no = int(input('Enter the seat no : '))

                if seat_no > 20:
                    print('Seat is not available\n')
                elif w['seat'][seat_no-1] != 'empty':
                    print('Seat already booked\n')
                else:
                    w['seat'][seat_no-1] = pass_name
                    print(f'Congress!! {seat_no} no. seat has been booked for you\n')
        if dec == False:
            print('Bus not found\n')

        # for w in self.bus_lists:
        #     print(w['seat'])

    def show_ticket(self):
        bus_no = int(input('Enter the bus No : '))

        for w in self.bus_lists:
            if w['coach'] == bus_no:
                print('*' * 50)
                print()
                print(f"{' ' * 10}{'#' * 10} BUS INFO {'#' * 10}")
                print(f"Bus Number : {bus_no} \t\t\t Driver : {w['driver']}")
                print(f"Arrival time : {w['arrival_time']} \t\t\t Departure time : {w['departure_time']}")
                print(f"From : {w['destination']} \t\t\t To : {w['to']}")

                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f" {a}. {w['seat'][a-1]}", end = "\t")
                        a += 1
                    for j in range(2):
                        print(f" {a}. {w['seat'][a-1]}", end = "\t")
                        a += 1

                    print()
                print('*' * 50)
            else:
                print('Bus not found\n')

    def get_userlist(self):
        return self.user_lists

    def create_account(self):
        username = input('Enter username : ')
        password = input('Enter password : ')
        self.new_user = User(username, password)
        self.user_lists.append(vars(self.new_user))

    def available_bus(self):
        if len(self.bus_lists) == 0:
            print('No buses are available\n')
        else:
            print('*' * 50)
            for bus in self.bus_lists:
                print()
                print(f"{' ' * 10}{'#' * 10} BUS {bus['coach']} INFO {'#' * 10}")
                print(f"Bus Number : {bus['coach']} \t Driver = {bus['driver']}")
                print(f"Arrival time : {bus['arrival_time']} \t Departure time : {bus['departure_time']}")
                print(f"From : {bus['destination']} \t To : {bus['to']}")
            print('*' * 50)


while True:
    comp = Marsa()
    c = Counter()
    print('1. Create an account\n')
    print('2. Login\n')
    print('3. Exit')
    user_input = int(input('Enter the choice : '))
    if user_input == 3:
        break
    elif user_input == 1:
        c.create_account()
    elif user_input == 2:
        name = input('Enter username : ')
        passw = input('Enter password : ')

        isAdmin = False
        flag = 0
        if name == 'Admin' and passw == '123':
            isAdmin = True
        if isAdmin == False:
            for user in c.get_userlist():
                if user['name'] == name and user['password'] == passw:
                    flag = 1
                    break
            if flag:
                while True:
                    print(f"{'*'*10}Welcome to MARSA TICKET BOOKING SYSTEM{'*'*10}")
                    print('1. Available buses\n 2. Show bus Info \n 3. Book a ticket\n 4. Exit\n')
                    choice = int(input('Enter the choice : '))
                    if choice == 4:
                        break
                    elif choice == 1:
                        c.available_bus()
                    elif choice == 2:
                        c.show_ticket()
                    elif choice == 3:
                        c.booking_ticket()
            else:
                print('Invalid username or password\n')

        else:
            while True:
                print(f"{'*'*10}Hello Admin, Welcome to MARSA TICKET BOOKING SYSTEM{'*'*10}")
                print('1. Add bus\n 2. Available buses\n 3. Show bus Info\n 4.Exit\n')
                choice = int(input('Enter the choice : '))
                if choice == 4:
                    break
                elif choice == 1:
                    comp.add_bus()
                elif choice == 2:
                    c.available_bus()
                elif choice == 3:
                    c.show_ticket()

    