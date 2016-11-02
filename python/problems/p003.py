import logging

correct_answer = 6857

#num_from_example = 13195
num = 600851475143

def p003():
    global num
    max_div = 1
    while num != 1:
        smallest_div = get_smallest_div(num)
        num = num/smallest_div
        logging.info('smallest_div={}, new num={}'.format(smallest_div, num))
        if (max_div < smallest_div):
            logging.info('update: old_max={}, new_max={}'.format(max_div, smallest_div))
            max_div = smallest_div
    print('p003={}'.format(max_div))
    return max_div

def get_smallest_div(num):
    for i in xrange(2, num):
        if num%i == 0:
            return i
    return num

def is_prime(num):
    if get_smallest_div(num) == num:
        return True
    return False

if __name__=="__main__":
    logging.basicConfig()
    p003()
    
