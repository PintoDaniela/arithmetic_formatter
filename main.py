
from arithmetic_arranger import arithmetic_arranger
argument1 = ["32 + 6987", "3801 - 2", "45 + 43", "123 + 49"]
print('\n------------------------------------------------------------')
print('---------------------  FORMATTER TEST  ---------------------')
print('------------------------------------------------------------\n\n')
print("Problems 1: ",argument1,"\nFormatted:")
print(arithmetic_arranger(argument1))
print('\n----------------------------------------------------------\n\n')
print("Problems 1: ",argument1,"\nFormatted + Answers:")
print(arithmetic_arranger(argument1,True))
print('\n----------------------------------------------------------\n\n')

'''

'''
#Error tests:
argument2 = ["32 + 69874", "3801 - 2", "45 + 43", "123 + 49"]
argument3 = ["32 * 6987", "3801 - 2", "45 + 43", "123 + 49"]
argument4 = ["32 + 69874", "3801 - 2", "45 + 43", "123 + 49", "3801 - 2", "45 + 43"]
argument5 = ["a32 * 6987", "3801 - 2", "45 + 43", "123 + 49"]
print('\n------------------------------------------------------------')
print('----------------------- ERROR TESTS ------------------------')
print('------------------------------------------------------------\n\n')
print("Problems 2: ",argument2,"\nFormatted:")
print(arithmetic_arranger(argument2))
print('\n----------------------------------------------------------\n\n')
print("Problems 3: ",argument3,"\nFormatted:")
print(arithmetic_arranger(argument3))
print('\n----------------------------------------------------------\n\n')
print("Problems 4: ",argument4,"\nFormatted:")
print(arithmetic_arranger(argument4))
print('\n----------------------------------------------------------\n\n')
print("Problems 5: ",argument5,"\nFormatted:")
print(arithmetic_arranger(argument5))
print('\n----------------------------------------------------------\n\n')





# Run unit tests automatically
#main(['-vv'])
