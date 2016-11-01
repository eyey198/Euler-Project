import logging

nth_prime = 10001 + 1

def fast_main():
    prime_counter = 1
    num = 2
    while prime_counter < nth_prime:
        if is_prime(num):
            logging.info('#{} prime is {}'.format(prime_counter, num))
            prime_counter += 1
        num += 1

def is_prime(num):
    for i in xrange(2,num):
        if num%i == 0:
            return False
    return True

if __name__=="__main__":
    logging.basicConfig(level=logging.DEBUG)
    fast_main()
    
