import logging

def fast_main():
   result = sum(get_next_even_fib())
   print result
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
    logging.basicConfig(level=logging.DEBUG)
    fast_main()
    
