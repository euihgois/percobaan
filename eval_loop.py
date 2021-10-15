import math

def eval_loop():
    while True:
        x=input('please input somthing\n')
        if x=='done':
            break
        print(eval(x))
    print('ok!')

eval_loop()