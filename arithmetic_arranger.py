import re

def arithmetic_arranger(problems, op=False):
    count_problems = len(problems)
    invalid_operators = False
    letters = False
    large_number = False

    for problem in problems:
        if  re.findall('[*/x%]', problem):
            invalid_operators = True
        if re.findall('[a-zA-Z]+', problem):
            letters = True
        numbers = re.findall('[0-9]+', problem)
        if len(numbers[0])>4 or len(numbers[1])>4:        
            large_number = True
        
    if(letters):
        return("Error: Numbers must only contain digits.")
    if(invalid_operators):
        return("Error: Operator must be '+' or '-'.")  
    if(count_problems > 5):
        return("Error: Too many problems.") 
    if(large_number):
        return('Error: Numbers cannot be more than four digits.')
    
    numbers_above = ''
    numbers_below = ''
    dashes = ''
    answers = ''
    x = 0
    for problem in problems:
        x+=1
        problem_numbers = re.findall('[0-9]+', problem)
        problem_operators = re.findall('[+-]', problem)

        if len(problem_numbers[0]) - len(problem_numbers[1]) == 1:
            problem_numbers[1] = ' '+problem_numbers[1]
        if len(problem_numbers[0]) - len(problem_numbers[1]) == -1:
            problem_numbers[0] = ' '+problem_numbers[0]
        if len(problem_numbers[0]) - len(problem_numbers[1]) == 2:
            problem_numbers[1] = '  '+problem_numbers[1]
        if len(problem_numbers[0]) - len(problem_numbers[1]) == -2:
            problem_numbers[0] = '  '+problem_numbers[0]
        if len(problem_numbers[0]) - len(problem_numbers[1]) == 3:
            problem_numbers[1] = '   '+problem_numbers[1]
        if len(problem_numbers[0]) - len(problem_numbers[1]) == -3:
            problem_numbers[0] = '   '+problem_numbers[0]
        
        count_dashes = 0
        if len(problem_numbers[0]) > len(problem_numbers[0]):
            for i in range(0,len(problem_numbers[0])+2):
                dashes+='-'
                count_dashes +=1
        else:
            for i in range(0,len(problem_numbers[1])+2):
                dashes+='-'
                count_dashes +=1
        if x < count_problems:
            dashes+='    '
        
        #Optional argument
        if op:
            if problem_operators[0] == '+':
                answer = int(problem_numbers[0])+int(problem_numbers[1])
            else: 
                answer = int(problem_numbers[0])-int(problem_numbers[1])            
            answer = str(answer)
            diff_spaces =  count_dashes-len(answer)
            if diff_spaces == 1:
                answers+=' '
            if diff_spaces == 2:
                answers+='  '
            if diff_spaces == 3:
                answers+='   '
            if diff_spaces == 4:
                answers+='    '
            if diff_spaces == 5:
                answers+='     '
            
            answers+=answer 
            if x < count_problems:
                answers+='    '    

        numbers_above+='  '
        numbers_above+=problem_numbers[0]
        if x < count_problems:
            numbers_above+='    '
        numbers_below+=problem_operators[0]
        numbers_below+=' '
        numbers_below+=problem_numbers[1]  
        if x < count_problems: 
            numbers_below+='    '    
    if op:
        arranged_problems = (f'{numbers_above}\n{numbers_below}\n{dashes}\n{answers}')
    else:
        arranged_problems = (f'{numbers_above}\n{numbers_below}\n{dashes}')


    
      
      
    return arranged_problems