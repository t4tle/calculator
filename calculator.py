


#user_input = sys.argv[1]
user_input = input('Enter the problem:')

    
def doMath(user_input):
    print('User Input: {}\n'.format(user_input))
    
    saved_operation = []
    tup = []
    
    num= []
    for x in user_input:
        if x.isdigit():
            num.append(x)
                

        else:
            tup.append(''.join(num))
            tup.append(x)
            num.clear()
    tup.append(''.join(num))        
        
    print('Ready Inputs: {}\n'.format(tup))
    saved_operation = tup.copy()
    
   
   
    
    
    while len(saved_operation) != 1:

        if '*' in saved_operation: 
            p = saved_operation.index('*')
            operand1 = saved_operation[p-1]
            operand2 = saved_operation[p+1]
            total = float(operand1) * float(operand2) 

        elif '/'in saved_operation:
            p = saved_operation.index('/')
            operand1 = saved_operation[p-1]
            operand2 = saved_operation[p+1]
            total = float(operand1) / float(operand2)

        elif '+'in saved_operation:
            p = saved_operation.index('+')
            operand1 = saved_operation[p-1]
            operand2 = saved_operation[p+1]
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