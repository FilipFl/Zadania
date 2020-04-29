from decimal import *

# zadanie 1.
def postal_codes(s1,s2):
    list_of_codes = []
    sep_s1 = s1.split("-")
    sep_s2 = s2.split("-")
    start1 = int(sep_s1[0])
    start2 = int(sep_s1[1])
    end1 = int(sep_s2[0])
    end2 = int(sep_s2[1])
    curr1 = start1
    curr2 = start2+1
    is_finished = False
    while not is_finished:
        if curr2 == 1000:
            curr1 += 1
            curr2 = 0
        code = str("{0:02}".format(curr1))+"-"+str("{0:03}".format(curr2))
        list_of_codes.append(code)
        curr2 += 1
        if curr1 == end1 and curr2 == end2:
            is_finished = True
    return list_of_codes

# zadanie 2.
def missing_element(given_list, n):
    # W ogłoszeniu nie było sprecyzowane czy elementy mogą się powtarzać
    # więc usuwam duplikaty
    working_on = given_list.copy()
    working_on = list(dict.fromkeys(working_on))
    working_on.sort()
    how_many_to_find = n-len(working_on)
    missing = []
    all_found = False
    found = 0
    i = 1
    iterator = 0
    while not all_found:
        if working_on[iterator] != i:
            missing.append(i)
            found += 1
        else:
            iterator += 1
        if found == how_many_to_find:
            all_found = True
        if iterator == len(working_on):
            all_found = True
            for x in range(i, n+1):
                missing.append(x)
        i += 1
    return missing

# zadanie 3.
def decimal_list():
    start = 2
    end = 5.5
    number = start
    dec_list = []
    getcontext().prec = 1
    while number <= end:
        dec_list.append(Decimal(number))
        number += 0.5
    return dec_list

