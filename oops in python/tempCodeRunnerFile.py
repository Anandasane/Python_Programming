class Father:
   def skills(self):
     Mother.hobbies('cooking')
     print("Gardening and coding")


class Mother:
   def hobbies(self):
      print("Cooking and painting")


class Child(Father, Mother):
   def own_skill(self):
      print("Playing guitar")
      super().skills()
      


class Grandchild(Child):
   def sports(self):
      print("Playing cricket")
      super().own_skill()


g=Grandchild()
g.sports()
g.own_skill()
g.hobbies()
g.skills()
