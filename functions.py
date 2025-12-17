from car_class import *

def show_menu():
    print("What would you like to do today?")
    print("-Add a car? enter 1")
    print("-Search for car 2")
    print("-Edit car info? enter 3")
    print("-Remove a car? enter 4")
    print("-Print the car list? enter 5")
    print("-Save the data to a file? enter 6")
    print("-Exit? enter 0.")
    return int(input())

def add(cars,id,name,make,body,year,value):
    cars[id] = Car(id,name,make,body,year,value)

def remove(cars,id):
    cars.pop(id)

def edit_car(cars,id):
    name = input("Name:\n")
    make = input("make:\n")
    body = input("Body:\n")
    year = input("year:\n")
    value = float(input("value:\n"))

    cars[id].set_name(name)
    cars[id].set_make(make)
    cars[id].set_body(body)
    cars[id].set_year(year)
    cars[id].set_value(value)


def search(cars, choice):
    if choice == "1":
        id = input("Please Enter the id of the car:\n")
        if id in cars:
            return id
    elif  choice == "2":
        name = input("Please Enter the name of the car:\n")
        for car in cars:
            if name == cars[car].get_name():
                id = car
                return id

    return None

def run_search(cars):
    while True:
        choice = input("To search using the Id enter 1. To search using the name of the car enter 2. Enter -1 to return to the previous menu\n" )
        if  choice == "-1":
            return
        elif choice == "1" or choice == "2":
            id = search(cars, choice)
            if id != None:
                print("Car found  ", cars[id].get_all_attributes())
            else:
                print("Car not found")

def run_edit(cars):
    while True:
        id = input("Enter the id of the car. Enter -1 to return to the previous menu\n")
        if id == "-1":
            return
        elif id in cars:
            edit_car(cars, id)
            print("Car's new info is ",cars[id].get_all_attributes())
        else:
            print("No car found")
    
def same_name(cars,name):
    for car in cars:
        if name == cars[car].get_name():
            return True
    return False

def run_add(cars):
    choice = "y"
    while choice == "y" or choice == "yes":
        print("Enter id of the car, followed by the car's information.")
        id = input("Id:\n")
        name = input("name:\n")
        make = input("make:\n")
        body = input("Body:\n")
        year = input("year:\n")
        value = float(input("value:\n"))
        if same_name(cars,name):
            print("The car is already in the inventory. No action is required.")
        elif id in cars:
            print("Incorrect Id. Id already exist in the system.")
        else:
            add(cars,id,name,make,body,year,value)
            print("car added to inventory")
            print(cars[id].get_all_attributes())
        choice = input("Do you want to add more cars? y(yes)/n(no)\n").lower()


def run_remove(cars):
    choice = "y"
    while choice == "y" or choice == "yes":
        print("Enter id of the car that you want to remove from the inventory.")
        id = input("id:\n")
        if id in cars:
            remove(cars, id)
            print("car removed")
        else:
            print("No car found")
        choice = input("Do you want to remove more cars?y(yes)/n(no)\n").lower()

def print_list(cars):
    for car in cars:
        print(cars[car].get_all_attributes())

def save_data(cars):
    fid = open('data.txt','w')
    for car in cars:
        fid.write(cars[car].get_all_attributes())
        fid.write('\n')
    fid.close
    print("Data saved to local file successfully!")