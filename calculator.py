


#user_input = sys.argv[1]
user_input = input('Enter the problem:')
def power(operand):

    if operand == '*' or operand == '/':
        return 5

    elif operand == '+' or operand == '-': 
        return 3


def doMath(user_input):
    print('User Input: {}\n'.format(user_input))
    # 1+1 = 2
    # PREFIX: +11 -> [+, 1, 1] = 2
    # POSTFIX: 11+ -> [1, 1, +] = 2

    tup = [0]
    saved_operation = []
    join = []
    i = 0
    # 4+3/2
    for x in user_input:
        
        if x.isdigit():
            
            join.append(x)
            

        else:          
            tup[i] = ''.join(join)
            join.clear()
            tup.append(0)
            i += 1
            try:
                c = saved_operation[-1]

                if power(c) < power(x):
                    saved_operation.append(x)
                else:
                    saved_operation[-1] = x
                    saved_operation.append(c)
            except:
                saved_operation.append(x)
            
                
    tup[i] = ''.join(join)    

    # ['4','3','2','/','+']         
    print('Ready Input: {}\n'.format(tup))
    print('Ready operation: {}\n'.format(saved_operation))
    while len(tup) != 1:
        operand2 = tup.pop() # 1
        operand1 = tup.pop() # 1  
        operation = saved_operation.pop() # +
        
        if operation == '+':
            total = float(operand1) + float(operand2)
                
        elif '-'in saved_operation:
            p = saved_operation.index('-')
            operand1 = saved_operation[p-1]
            operand2 = saved_operation[p+1]
            total = float(operand1) - float(operand2) 
        
        saved_operation.insert(p, total)
        saved_operation.pop(p+1)
        saved_operation.pop(p+1)
        saved_operation.pop(p-1)
        print('Next List: {}'.format(saved_operation))        
      



doMath(user_input)