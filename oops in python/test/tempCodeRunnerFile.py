class Password:
    __password=123

    def set_password(self,np):
        self.np=np
        if(np:=(int(input("Enter new password"))) == self.__password):
            self.__password = np
            print("New password is set successfully ")
        else:
            print("Enter the right password Try again")

    def get_password(self):
        return f'The new password is {self.__password}'
    
p=Password()
p.get_password()

p.set_password()
p.get_password
