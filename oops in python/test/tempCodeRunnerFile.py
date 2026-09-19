
class Book:
    def show(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
        print(f"{self.title} book with author {self.author} and price {self.price}")


a=Book()
b=Book()
c=Book()
d=Book()
e=Book()

a.show('bhagvat gita', 'krishna',200)
b.show("harry potter",'harry',2000)
c.show('english book','english sir',2300)
d.show('math book', 'math sir',400)
e.show('history book', 'history sir', 300)