import sys

user_input = sys.argv[1]
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

    tup = []
    saved_operation = []
    # 4+3/2
    for x in user_input:
        if x.isdigit():
            tup.append(x)

        else:
            try:
                c = saved_operation[-1]

                if power(c) < power(x):
                    saved_operation.append(x)
                else:
                    saved_operation[-1] = x
                    saved_operation.append(c)
            except:
                saved_operation.append(x)
                
    

    # ['4','3','2','/','+']         
    print('Ready Input: {}\n'.format(tup))
    print('Ready operation: {}\n'.format(saved_operation))
    while len(tup) != 1:
        operand2 = tup.pop() # 1
        operand1 = tup.pop() # 1  
        operation = saved_operation.pop() # +
        
        if operation == '+':
            total = float(operand1) + float(operand2)
        elif operation == '-':
            total = float(operand1) - float(operand2)
        elif operation == '*':
            total = float(operand1) * float(operand2)
        elif operation == '/':
            total = float(operand1) / float(operand2)       
        tup.insert(0, total)
        print('Next List: {}'.format(tup))
    
    print('\nTotal: {}'.format(tup[0]))
                



doMath(user_input)