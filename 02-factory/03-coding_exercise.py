class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    person_idx = 0
    
    def create_person(self, name):
        # todo
        new_person = Person(self.person_idx, name)
        self.person_idx += 1 
        return new_person


def main():
    person = PersonFactory().create_person("Bogdan")


if __name__ == "__main__":
    main()