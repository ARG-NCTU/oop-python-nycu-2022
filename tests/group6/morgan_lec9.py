import pytest

# 類別定義
class Animal:
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return f"Animal: {self.name}:{self.age}"

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Rabbit(Animal):
    def __add__(self, other):
        return Rabbit(self.age + other.age)

    def __str__(self):
        return f"Rabbit age: {self.age}"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_friends(self):
        return self.friends

    def speak(self):
        print(f"{self.name} says hello!")

    def add_friend(self, friend):
        self.friends.append(friend)

    def age_diff(self, other):
        print(f"Age difference between {self.name} and {other.get_name()} is {abs(self.age - other.get_age())} years.")

class Student(Person):
    def __init__(self, name, age, major="Undeclared"):
        super().__init__(name, age)
        self.major = major

    def change_major(self, new_major):
        self.major = new_major

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, Major: {self.major}"

# 測試函式
def test_animal():
    a = Animal(4)
    a.set_name("fluffy")
    assert a.get_name() == "fluffy"
    assert a.get_age() == 4

def test_cat():
    c = Cat(5)
    c.set_name("Dog")
    c.speak()
    assert c.get_name() == "Dog"
    assert c.get_age() == 5

def test_rabbit():
    p1 = Rabbit(2)
    p2 = Rabbit(3)
    r1 = p1 + p2
    assert isinstance(r1, Rabbit)
    assert r1.get_age() == 5

def test_person():
    p = Person("Johnson", 18)
    p.add_friend("AI")
    p.add_friend("GPT")
    assert "AI" in p.get_friends()
    assert not "John" in p.get_friends()
    assert p.get_name() == "Johnson"
    assert p.get_age() == 18

    p2 = Person("AI", 30)
    p.age_diff(p2)

def test_student():
    s1 = Student("Ella", 22, "Nano")
    s1.change_major("ECE")
    s1.set_name("Johnson")
    assert s1.get_name() == "Johnson"
    assert s1.major == "ECE"

    s2 = Student("Sana", 25, "Twice")
    s2.add_friend("Momo")
    s2.add_friend("Mina")
    assert s2.get_friends() == ["Momo", "Mina"]

# 如果直接執行檔案，運行 pytest 測試
if __name__ == "__main__":
    pytest.main()

