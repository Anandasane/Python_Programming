print('===========================================Login Class===================================================')

class login:
    username1 = {'Anand', 'cheetan'}

    def user_input(self, name, password):
        if name in self.username1:
            print('User already exists, try again.')
            return
        else:
            print('Username is valid. Enter password.')

        # Check specific password rules
        has_space = ' ' in password
        is_too_short = len(password) < 10 
        lacks_special = password.isalnum()  

        
        is_valid = True

        if is_too_short:
            print(" Error: Password must be at least 10 characters long.")
            is_valid = False
            
        if has_space:
            print(" Error: Password cannot contain spaces.")
            is_valid = False
            
        if lacks_special:
            print(" Error: Password must include at least one special character (e.g., @, #, $).")
            is_valid = False

        if is_valid:
            print(" Successfully logged in!")
            self.username1.add(name)
        else:
            print("\n  Please try again with a valid password.")
        
        

l=login()
l.user_input('anand','1234512@4212346812')

print('=================================================function2==============================================================')

def number_pattern(n):
    # Check if n is an integer (excluding booleans which are a subclass of int)
    if not isinstance(n, int) or isinstance(n, bool):
        return 'Argument must be an integer value.'
    
    # Check if n is less than 1
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    
    # Build the string of numbers
    result = []
    for i in range(1, n + 1):
        result.append(str(i))
    
    # Join the list into a single string separated by spaces
    return " ".join(result)   

print(number_pattern(12))