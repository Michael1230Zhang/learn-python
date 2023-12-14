from enum import Enum
from dataclasses import dataclass

class Gender(Enum):
    MALE = 1
    FEMALE = 2
    HELICOPTER = 3
    WALMART_SHOPPING_BAG = 4


class Classroom(Enum):
    A = 1
    B = 2
    C = 3
    D = 4


@dataclass
class Class:
    grade: int
    classroom: Classroom


@dataclass
class Student:
    # fields
    name: str
    age: int
    gender: Gender
    clazz: Class

    def cheat(self, other: 'Student'):
        print(f'{self.name} was caught cheating with {other.name}!')


class Dog:
    def bark(self):
        print('Bark Bark Bark!')


def main():
    pass
    # adam = Student(name='Adam Smith', age=-1, gender=Gender.HELICOPTER, clazz=Class(grade=1, classroom=Classroom.C))
    # michael = Student(name='Zhang Jiusi', age=-2, gender=Gender.HELICOPTER, clazz=Class(grade=3, classroom=Classroom.D))

    # adam.cheat(michael)


if __name__ == '__main__':
    main()
