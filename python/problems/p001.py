import logging

correct_answer = 233168

def p001():
    return p001_c()

#first attemp
def p001_a():
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
    print('p001={}'.format(sum))
    return sum

#sec attemp
def p001_b():
    num_list = [i for i in range(1, 1000) if (i%3 == 0) or (i%5 == 0)]
    print('p001={}'.format(sum(num_list)))
    return num_list

#best solution!
def p001_c():
    mult_sum = 0
    for i in xrange(1000):
        if (i%3 == 0) or (i%5 == 0):
            mult_sum += i
    print('p001={}'.format(mult_sum))
    return mult_sum



if __name__=="__main__":
    logging.basicConfig(level=logging.DEBUG)
    p001_a()
    p001_b()
    p001_c()
    
