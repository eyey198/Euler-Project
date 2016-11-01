import logging

#num = 13195
num = 600851475143

def fast_main():
    result = -1
    for i in xrange(100,1000):
        for j in xrange(100,1000):
            if is_polindrom(i*j) and result < i*j:
                logging.info('{}*{}={} is polindrom'.format(i, j, i*j))
                result = i*j
    print 'result={}'.format(result)

def is_polindrom(num):
    return str(num) == str(num)[::-1]




if __name__=="__main__":
    logging.basicConfig(level=logging.DEBUG)
    fast_main()
    
