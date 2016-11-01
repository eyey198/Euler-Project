import logging

def fast_main():
    three_multi = 3
    five_multi = 5
    sum = 0
    while three_multi < 1000:
        logging.info('three={}, five={}'.format(three_multi, five_multi))
        if three_multi<five_multi:
            sum += three_multi
            three_multi += 3
        elif five_multi<three_multi:
            sum +=five_multi
            five_multi += 5
        elif three_multi == five_multi:
            three_multi += 3
        else:
            raise Exception('not possible')
    print sum

def short_main():
    num_list = [i for i in range(1, 1000) if (i%3 == 0) or (i%5 == 0)]
    print sum(num_list)

def short_main2():
    mult_sum = 0
    for i in xrange(1000):
        if (i%3 == 0) or (i%5 == 0):
            mult_sum += i
    print mult_sum
    return mult_sum
if __name__=="__main__":
    logging.basicConfig(level=logging.DEBUG)
    fast_main()
    short_main()
    short_main2()
    
