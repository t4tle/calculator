import sys
import re


#user_input = sys.argv[1]
user_input = input('Enter the problem:')

    
def doMath(user_input):
    print('User Input: {}\n'.format(user_input))
    

    
    saved_operation = []

    
    tup = re.findall('\d+',user_input)
    saved_operation = tup.copy()
    count = -1
    for x in user_input:
        if x.isdigit():
            continue

        else:
            
            count += 2
            saved_operation.insert(count,x)

            
        
    print('Ready Input: {}\n'.format(tup))
    print('Ready operation: {}\n'.format(saved_operation))
   
   
    
    
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