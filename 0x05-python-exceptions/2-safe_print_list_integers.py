#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    count = 0
    for i in my_list[:x]:
        try:
            print("{:d}".format(int(i)), end="")
            count +=1
        except (ValueError, TypeError):
            continue
    
    print()
    return count

