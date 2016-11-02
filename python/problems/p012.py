import logging
from math import sqrt

correct_answer = 76576500

DIVISORS_MAX = 500
def p012():
    for cur_triangle in get_next_triangle():
        if DIVISORS_MAX < len(get_divisors(cur_triangle)):
            break
    print('p012={}'.format(cur_triangle))
    return cur_triangle

def get_next_triangle():
    i = 0
    cur_triangle = 0
    while True:
        i += 1
        cur_triangle += i
        yield cur_triangle

def get_divisors(num):
    divisor_list = []
    for i in range(1,int(sqrt(num*1.0))+1):
        if num%i == 0:
            divisor_list += [i, num/i]
    return sorted(divisor_list)

if __name__=="__main__":
    logging.basicConfig()
    p012()
    

