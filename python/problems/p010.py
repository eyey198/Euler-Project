import logging

correct_answer = 142913828922

MAX_PRIME = 2*10**6

def p010():
    prime_sum = 2
    for i in range(3, MAX_PRIME, 2):
        print i
        if is_prime(i):
            logging.info('{} is prime'.format(i))
            prime_sum += i
    print('p010={}'.format(prime_sum))
    return prime_sum

def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

if __name__=="__main__":
    logging.basicConfig()
    p010()
