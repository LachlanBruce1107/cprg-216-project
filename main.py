from car_class import *
from functions import *

car_list = dict()

fid = open('data.txt','r')
for line in fid:
    line.rstrip()
    list = line.split("\t")
    car_list[list[0]] = (Car(list[0],list[1],list[2],list[3],list[4],list[5]))
fid.close()
