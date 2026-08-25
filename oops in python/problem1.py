print('===========================================Login Class===================================================')

class Login:
    # Using a set to store registered usernames
    registered_users = {'Anand', 'Cheetan'}

    def user_input(self, name, password):
        # 1. Check if username already exists
        if name in self.registered_users:
            print('User already exists. Login instead of registering.')
            return
        
        # If username is new, proceed to password validation
        print(f'Username "{name}" is available.')
        
        is_valid = False
        
        # Loop until a valid password is entered
        while not is_valid:
            # Re-check conditions based on the CURRENT password
            has_space = ' ' in password
            is_too_short = len(password) < 10 
            lacks_special = password.isalnum()  # True if it ONLY has letters/numbers (missing special char)

            # Validate
            if is_too_short:
                print(" Error: Password must be greater than 10 characters.")
                is_valid = False
            elif has_space:
                print(" Error: Password cannot contain spaces.")
                is_valid = False
            elif lacks_special:
                print(" Error: Password must include at least one special character (e.g., @, #, $).")
                is_valid = False
            else:
                # All checks passed
                is_valid = True
                self.registered_users.add(name)
                print(" Successfully registered and logged in!")
                return

            # If we are here, validation failed. Ask for password again.
            # Note: In a real app, you'd use input() here. 
            # For this example, we break to avoid infinite loop if called programmatically
            print("\n Please try again with a valid password.")
            
            # Since this is a function call with arguments, we can't easily ask for new input 
            # without changing the function signature. 
            # If you want to simulate a retry, you would need to call input() inside the loop.
            # password = input("Enter new password: ") 
            break # Breaking here for the example call to avoid infinite loop


l = Login()
l.user_input('Rohit', '1234567890!')

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


# u=input('Enter user= ')
# if(' 'not in u):
#     p=input('Enter your Password= ')
#     l=len(p)>10
#     s=' 'in p
#     sp=p.isalnum()
#     print(sp)
# else:
#     print('invalid User')

print('==========================================================function3=============================================================')

username_list = list()
u = input('Enter user= ')

if ' ' not in u:
    p = input('Enter your Password= ')
    l = len(p)
    s = ' ' in p
    sp = p.isalnum()
    
    # Check if username already exists
    if u in username_set:
        print('invalid user')
    else:
        # Validate password requirements
        has_space = ' ' in p
        is_too_short = l <= 10
        is_alphanumeric = p.isalnum()  # True if ONLY letters and numbers
        has_special = not is_alphanumeric  # True if contains special chars
        
        if has_space:
            print('Password cannot contain spaces')
        elif is_too_short:
            print('Password must be greater than 10 characters')
        elif is_alphanumeric:
            print('Password must contain at least one special character')
        else:
            # All conditions met
            username_set.add(u)
            print(f'User {u} added successfully!')
            print(f'Password length: {l}')
            print(f'Password is alphanumeric: {sp}')
else:
    print('invalid User')

# Optional: Display current registered users
print(f'Currently registered users: {username_list}')

