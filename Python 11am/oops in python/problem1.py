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
        lacks_special = password.isalnum()  # True if NO special chars

        # Flag to track if any error occurred
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
