import logging

correct_answer = 232792560

divisors_list = [2,3,5,7,11,13,17,19]

def p005():
    gcd = 1
    for i in range(1,21):
        gcd *= i
    print('p005={}'.format(gcd))
    print "asdasdas"
    return gcd

if __name__=="__main__":
    logging.basicConfig()
    p005()
    
