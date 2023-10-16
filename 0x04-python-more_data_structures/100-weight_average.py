#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) is None:
        return 0 
    res =  0

    for i in range(len(my_list)):
        res += my_list[i][0] * (my_list[i][1])
    avg = res / sum([x[1] for x in my_list])

    return avg
