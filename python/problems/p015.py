import logging
import operator

correct_answer = 837799

MAX_START_NUMBER = 1000000
collatz_dic = {1:1}
def p014():
    for i in range(MAX_START_NUMBER, 1, -1):
        if i not in collatz_dic:
            collatz_rec(i)
    
    result_start_number = max(collatz_dic.iteritems(), key= lambda (k,v):v)
    print('p014={}'.format(result_start_number[0]))
    return result_start_number[0]

def collatz_rec(num):
    if num not in collatz_dic:
        if num%2 == 0: 
            new_num = num/2
        else:
            new_num = 3*num + 1
        collatz_dic[num] = collatz_rec(new_num)+1
    
    return collatz_dic[num]

if __name__=="__main__":
    logging.basicConfig()
    p014()
