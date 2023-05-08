from abc import ABC, abstractmethod
"""
파이썬에서 abc는 추상 베이스 클래스(ABC)를 정의하기 위한 기반 구조를 제공합니다.
추상 클래스는 메서드의 목록만 가진 클래스이며,
클래스에서 메서드 구현을 강제하기 위해 사용합니다.
추상 클래스를 만들기 위해선 import로 abc모듈을 가져와야 합니다.
abstract base class의 약자 
(metaclass=ABCMeta)를 지정하고, 메서드를 만들 때 위에
@abstractmethid를 붙여서 추상 메서드로 지정합니다.
"""

# Abstract Product
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
# Concrete Products
class Dog(Animal):
    def speak(self):
        return "AWOO~"
class Cat(Animal):
    def speak(self):
        return "Myaa~"

#Creator Interface
class AnimalHome(ABC):
    @abstractmethod
    def breed_animal(self):
        pass
class brd_Dog(AnimalHome):
    def breed_animal(self):
        return Dog()
class brd_Cat(AnimalHome):
    def breed_animal(self):
        return Cat()

class Client:
    def __init__(self, animal_home):
        self.animal_home = animal_home
    def make_sound(self):
        animal = self.animal_home.breed_animal()
        return animal.speak()

# Usage
if __name__ == "__main__":
    dog_factory = brd_Dog()
    cat_factory = brd_Cat()

    dog_client = Client(dog_factory)
    cat_client = Client(cat_factory)

    print(dog_client.make_sound()) # Output: Woof
    print(cat_client.make_sound()) # Output: Meow
