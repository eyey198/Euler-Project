import logging

correct_answer = 25164150

num = 100

def p006():
    sum_of_squares = sum([i*i for i in range(num+1)])
    square_of_sum = (sum(range(num+1)))**2
    my_diff = square_of_sum - sum_of_squares
    logging.info('s_of_sum={}, sum_of_s)={}'.format(square_of_sum,sum_of_squares))
    print('p006={}'.format(my_diff))
    return my_diff

if __name__=="__main__":
    logging.basicConfig()
    p006()
    
