

def convert_number(value):

            value = value.strip().lower()
            parts = value.split()

            if len(parts) != 0 and parts[0] in neg_signs:
                converted_value = convert_number(" ".join(parts[1:]))
                if converted_value is None:
                    return None

                return -converted_value


            if len(parts) == 2 and parts[0] in tens and parts[1] in ones:
                return tens[parts[0]] + ones[parts[1]]
            
            if len(parts) == 1 and parts[0] in tens:
                return tens[parts[0]]


            if value in word_to_num:
                return word_to_num[value]
            try:
                return float(value)
            except ValueError:
                return None

def calculator(num1, num2):

    while True:
        print(f'Please choose the operation you want to perform with the numbers provided: {num1} and {num2}')

        print(' ')
        print('1, +, addition, add')
        print('2, -,subtraction, sub')
        print('3, *, multiplication, mul')
        print('4, /, division, div')
        print('5, %, percentage, perc')
        print('6, ^, exponent/power, exp/pwr')
        print('7, //, floor division, floordiv')
        print('8, m%, modulus, mod')
        print(f"IF you want to EXIT type '9', 'exit' or 'e' ")

        selection = input('choose the operation you want to perform: ').strip().lower()

        if selection in ('1', '+', 'addition', 'add'):
            result = num1 + num2
            

        elif selection in ('2', '-', 'subtraction', 'sub'):
            result = num1 - num2
            

        elif selection in ('3', '*', 'multiplication', 'mul'):
            result = num1 * num2
            

        elif selection in ('4', '/', 'division', 'div'):
            if num2 == 0:
                result = 'Undefined'
            else:
                result = num1 / num2
                # print(f'The result of {num1} / {num2} is: {result}')

        elif selection in ('5', '%', 'percentage', 'perc'):
            result = (num1 / num2) * 100 if num2 != 0 else 'Undefined'
            

        elif selection in ('6', '^', 'exponentiation', 'power', 'exp', 'pwr'):
            if num1 == 0 and num2 < 0:
                result = 'Undefined' 
            else:
                result = num1 ** num2
            

        elif selection in ('7', '//', 'floor division', 'floordiv'):
            if num2 == 0:
                result ='Undefined'
            else:
                result = num1 // num2
                

        elif selection in ('8', 'm%', 'modulus', 'mod'):
            if num2 == 0:
                result = 'Undefined'
            else:
                result = num1 % num2
                

        elif selection in ('9', 'exit', 'e'):
            return 'exit'
        
        
        else:
            print('Invalid selection. Please choose a valid operation.')
            continue

        print(f'The result is: {result}')
        return result
        
if __name__ == "__main__":
    
    print('Hello')
        
    #decimal_words = ['point', 'and','dot', 'decimal', 'fraction', 'decimal point', 'decimal fraction', 'decimal dot', 'decimal and', 'decimal and point', 'decimal and fraction', 'decimal and dot', 'decimal and decimal', 'decimal and decimal point', 'decimal and decimal fraction', 'decimal and decimal dot', 'decimal and decimal and', 'decimal and decimal and point', 'decimal and decimal and fraction', 'decimal and decimal and dot','tenths', 'hundredths', 'thousandths']
    word_to_num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19}
    neg_signs = {'minus', 'negative', 'neg'}    
    ones = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    tens = {'twenty' : 20, 'thirty' : 30,'forty' : 40, 'fifty' : 50, 'sixty' : 60, 'seventy' : 70, 'eighty' : 80, 'ninety' : 90}
    

    while True:

        num_1_input = input("Enter the first number: ").strip().lower()
        if num_1_input in ('exit', 'e'):
            break
        num_1 = convert_number(num_1_input)
        if num_1 is None:
            print('Invalid input. Please enter a valid input.')
            continue

        num_2_input = input("Enter the second number: ").strip().lower()
        if num_2_input in ('exit', 'e'):
            break
        num_2 = convert_number(num_2_input)
        if num_2 is None:
            print('Invalid input. Please enter a valid input.')
            continue

        print(f" iF YOU WANT TO EXIT TYPE 'exit' ")
        
        
        result = calculator(num_1, num_2)
 

        if result == 'exit':
            break

        elif result == 'Undefined':
            continue

        show_current_result = False

        while True:

            if show_current_result:
                print(f'                The current result is: {result}')
                show_current_result = False
            
            action = input(

                """
                Choose:
                1. 'Continue with result' (r)
                2. 'Input new numbers' (n)
                3. 'Exit' (e)
                Selection """
                ).strip().lower()

            if action in ('result', '1', 'continue', 'r'):
                next_num_input = input("Enter the next number: ").strip().lower()
                if next_num_input in ('exit', 'e'):
                    action = 'exit'
                    break
                next_num = convert_number(next_num_input)
                if next_num is None:
                    print('Invalid input. Please enter a valid input.')
                    show_current_result = True
                    continue

                result = calculator(result, next_num)
                if result == 'Undefined':
                    break
                if result == 'exit':
                    break
            elif action in ('new', '2', 'n'):
                break
            elif action in ('exit', '3', 'e'):
                break
            else:
                show_current_result = True
                print('Invalid input. Please enter a valid input.')
        

        if result == 'exit':
            break

        if action in ('exit', '3', 'e'):
            break
        else:
            continue


print('You Are Now Exiting The Program! GOODBYE!')

    
    #Done
    # learn what if name is for when running a script aka the file im in but if i import that file into another script then its a module which would allow me to run the imported script in the other script/module.another operation is basicaaly when u do a diff operaation from what u were already doing.
    # automate so that the user can choose to perform another operation with the same numbers or input new numbers
    # add an option to exit the program
    # add error handling for invalid inputs (e.g., non-numeric values, division by zero)
    # Add exponentiation and modulus operations(aka power), integer division, and percentage to the calculator
    # add a feature to allow the user to perform multiple operations in one go (e.g., chaining operations)

    #Do list
    #make it possible to turn a string into a number and vice versa while still being able to perform operations on them
    #make the calculator more user-friendly by adding a menu system to choose operations
    # add a delete option to remove a number from the list of numbers used in the operations
    # add a feature to allow the user to perform operations on a list of numbers (e.g., sum, average, etc.)
    # Learn what the user wants to do next (e.g., perform another operation, input new numbers, exit the program)
    #if 2nd number input is invalid it forces user to restart the input process form the first number input and not 2nd input number
   