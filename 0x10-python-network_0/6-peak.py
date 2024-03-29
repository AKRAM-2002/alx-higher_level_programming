#!/usr/bin/python3

def find_peak(list_of_integers):

    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
    
    