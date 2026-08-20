print('===========================================Login Class===================================================')

class login:

   username1={'Anand','cheetan'}
   
   def user_input(self,name,password):
    #   self.name=name
    #   self.password=password

      if name in self.username1:
        print('user already exits try again')
      else:
         print('username is valid enter password')

                
      while True:
            has_space = ' ' in password
            is_too_short = len(password) < 10 
            lacks_special = password.isalnum() 

            if has_space or is_too_short or lacks_special:
                print("Invalid password. Try again.")
                print("- Must be at least 10 characters long.")
                print("- Cannot contain spaces.")
                print("- Must include at least one special character.")
            else:
                print("Successfully logged in!")
                
            break
        
        

l=login()
l.user_input('anand','123456@781212')
