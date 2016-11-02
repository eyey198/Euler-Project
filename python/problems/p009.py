import logging

correct_answer = 31875000

SUM_UP = 1000

def p009():
    p009_a()
    p009_b()

def p009_a():
    for a in range(SUM_UP):
        for b in range(a, SUM_UP):
            c = SUM_UP - a - b
            logging.info('a={}, b={}, c={}'.format(a,b,c))
            if (a**2 + b**2 == c**2) and (a != c) and (b != c):
                print('p009={}'.format(a*b*c))
                return a*b*c
    raise Exception()

def p009_b(): 
    for m_int in range(1, int(SUM_UP**0.5)):
        m = m_int * 1.0
        n = (1000-2*(m**2))/(2*m)
        a = m**2-n**2
        b = 2*m*n
        c = m**2+n**2
        logging.info('a={}, b={}, c={}, m={}, n={}'.format(a,b,c,m,n))

        is_all_integers = a.is_integer() and b.is_integer() and c.is_integer()
        is_all_in_range = (0<a<1000) and (0<b<1000) and (0<c<1000)
        if is_all_in_range and is_all_integers:
            print('p009={}'.format(a*b*c))
            return a*b*c
    
    #print('p009={}'.format(max_prod))
    #return max_prod


if __name__=="__main__":
    logging.basicConfig()
    p009_a()
    p009_b()
    
