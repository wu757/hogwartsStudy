import yaml


class Animal():
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def call(self):
        print(f"{self.name} 会叫")

    def run(self):
        print(f"{self.name} 会跑")


class Cat(Animal):
    def __init__(self, name, color, age, gender, hair="short hair"):
        Animal.__init__(self, name, color, age, gender)
        self.hair = hair

    def catch_mouse(self):
        print(f"{self.name} 会捉老鼠")

    def call(self):
        print(f"{self.name} 喵喵叫")


class Dog(Animal):
    def __init__(self, name, color, age, gender, hair="long hair"):
        Animal.__init__(self, name, color, age, gender)
        self.hair = hair

    def look_after_house(self):
        print(f"{self.name} 会看家")

    def call(self):
        print(f"{self.name} 汪汪叫")


with open("python实战二/animal_data.yaml", "rb") as f:
    animalData = yaml.safe_load(f)

if __name__ == '__main__':
    cat_info = animalData["cat"]
    cat_name = cat_info["name"]
    cat_color = cat_info["color"]
    cat_age = cat_info["age"]
    cat_gender = cat_info["gender"]
    cat_hair = cat_info["hair"]
    dog_info = animalData["dog"]
    dog_name = dog_info["name"]
    dog_color = dog_info["color"]
    dog_age = dog_info["age"]
    dog_gender = dog_info["gender"]
    dog_hair = dog_info["hair"]

    littleCat = Cat(cat_name, cat_color, cat_age, cat_gender, cat_hair)
    print(littleCat.name)
    print(littleCat.color)
    print(littleCat.age)
    print(littleCat.gender)
    print(littleCat.hair)
    littleCat.catch_mouse()

    littleDog = Dog(dog_name, dog_color, dog_age, dog_gender, dog_hair)
    print(littleDog.name)
    print(littleDog.color)
    print(littleDog.age)
    print(littleDog.gender)
    print(littleDog.hair)
    littleDog.call()
