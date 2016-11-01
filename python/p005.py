import logging

divisors_list = [2,3,5,7,11,13,17,19]


'''
def fast_main():
    num = 20
    while True:
        num += 2
        is_num_evenly_divisible = True
        for divisor in divisors_list:
            if num%divisor != 0:
                is_num_evenly_divisible = False
                logging.info('{}%{}!=0'.format(num, divisor))
                break
        if is_num_evenly_divisible:
            print 'result={}'.format(num)
            return num
'''

def fast_main():
    gcd = 1
    for i in divisors_list:
        gcd *= i
    print gcd
    return gcd

if __name__=="__main__":
    logging.basicConfig(level=logging.DEBUG)
    fast_main()
    
