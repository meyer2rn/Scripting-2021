#Calculator
import emoji
def welcome():
    print('''Welcome to Python Calculator''')
welcome()
your_name = input("What is your name?: ")
print("Hello", your_name)
print(emoji.emojize(':winking_face:'))
def calculate():
    while True:
                operation = input('''Please enter what math operation you would like to use: 
                + for addition 
                - for subtraction 
                * for multiplication
                / for division 
                ** for power 
                % for modulo 
                ''')
                if operation in ('+', '-', '*', '/', '**', '%'):
                        number_1 = int(input('Enter the first integer:  '))
                        number_2 = int(input('Enter the second integer:  '))

                        if operation == '+':
                                print('{} + {} = '.format(number_1, number_2))
                                print(number_1 + number_2)

                        elif operation == '-':
                                print('{} - {} = '.format(number_1, number_2))
                                print(number_1 - number_2)  
                                        
                        elif operation == '*':
                                print('{} * {} = '.format(number_1, number_2))
                                print(number_1 * number_2)
                                        
                        elif operation == '/':
                                if number_2 == 0: 
                                        print('YOU CANNOT DIVIDE BY ZERO')
                                print('{} / {} = '.format(number_1, number_2))
                                print(number_1 / number_2)
                                

                        elif operation == '**':
                                print('{} ** {} = '.format(number_1, number_2))
                                print(number_1 ** number_2)
                                        
                        elif operation == '%':
                                print('{} % {} = '.format(number_1, number_2))
                                print(number_1 % number_2)

                        try_again = input("Do you want to use the Python Calculator again?(y/n) ")
                        if try_again == "n":
                                print(emoji.emojize('Have a good day. Goodbye! :grinning_face:'))
                                break
                else:
                        print("Invalid input. Please try again and enter valid input")               
calculate()
        

