import logging

correct_answer = 906609

#num_from_example = 13195
num = 600851475143

def p004():
    result = -1
    for i in xrange(100,1000):
        for j in xrange(100,1000):
            if is_polindrom(i*j) and result < i*j:
                logging.info('{}*{}={} is polindrom'.format(i, j, i*j))
                result = i*j
    print 'p004={}'.format(result)
    return result

def is_polindrom(num):
    return str(num) == str(num)[::-1]




if __name__=="__main__":
    logging.basicConfig()
    p004()
    
