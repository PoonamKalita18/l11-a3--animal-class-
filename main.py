from abc import ABC, abstractmethod
class Animal (ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
       print('i can walk')
class Snail(Animal):
    def move(self):
        print('i can slide and swift')
class Dog(Animal):
    def move(self):
        print('i can bark')
class Cat (Animal):
     def move(self):
         print('i can meow')
R = Human()
R.move()
S = Snail()
S.move()
T = Dog()
T.move()
P = Cat()
P.move()