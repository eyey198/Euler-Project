import logging

correct_answer = 4613732

def p002():
   result = sum(get_next_even_fib())
   print('p002={}'.format(result))
   return result


def get_next_even_fib():
    counter = 0
    a = 1
    b = 2
    while (b < 4000000):
        logging.info('fib[{}]= {}'.format(counter, b))
        if b%2 == 0:
            yield b
        a,b = b,a+b

if __name__=="__main__":
    logging.basicConfig()
    p002()
    
