
class login:
   def dec(f):
      def wrap(self,u,p):
         print('Login start')
         f(self,u,p)
         print('Login End')
      return wrap

   @dec
   def userlogin(self,u,p):
      if(u=='abc'and p=='123'):
         print('Login success')
      else:
         print('Invalid Login')

l=login()
l.userlogin('abc','123')
l.userlogin(p='123',u='abc')
