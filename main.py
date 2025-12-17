from car_class import *
from functions import *

car_list = dict()

fid = open('data.txt','r')
for line in fid:
    line.rstrip()
    list = line.split("\t")
    car_list[list[0]] = (Car(list[0],list[1],list[2],list[3],list[4],list[5]))
fid.close()

print('Welcome to the cars inventory system')
while True:
    option = show_menu()
    match option:
        case 1:
            run_add(car_list)
        case 2:
            run_search(car_list)
        case 3:
            run_edit(car_list)
        case 4:
            run_remove(car_list)
        case 5:
            print_list(car_list)
        case 6:
            save_data(car_list)
        case 0:
            break
    