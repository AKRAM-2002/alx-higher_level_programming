#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    list_res = []
    for val in range(list_length):

        try:
            res = my_list_1[val] / my_list_2[val]

        except (ZeroDivisionError):
            print("division by 0")
            res = 0

        except (TypeError):
            print("wrong type")
            res = 0

        except IndexError:
            print("index out of range")
            res = 0

        finally:
            list_res.append(res)

    return (list_res)
