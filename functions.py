from car_class import *

def show_menu():
    print("What would you like to do today?")
    print("-Add a car? enter 1")
    print("-Search for car 2")
    print("-Edit car info? enter 3")
    print("-Remove a car? enter 4")
    print("-Print the car list? enter 5")
    print("-Save the data to a file? enter 6")
    return int(input())

def add(cars,id,name,make,body,year,value):
    cars[id] = Car(id,name,make,body,year,value)

def remove(cars,id):
    cars.pop(id)

def edit_name(cars,id,new_name):
    pass

def search(cars, id):
    pass

def run_search(cars):
    pass

def run_edit(cars):
    pass
    
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
        value = input("value:\n")
        if same_name(cars,name):
            print("The car is already in the inventory. No action is required.")
        elif id in cars:
            print("Incorrect Id. Id already exist in the system.")
        else:
            add(cars,id,name,make,body,year,value)
            print("car Enrolled in the system")
            print(id,name,make,body,year,value)
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