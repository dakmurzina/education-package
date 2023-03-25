class Human:
    def __init__(self, name, familyname, age, gender, nationality):
        self.__name__ = name
        self.__familyname__ = familyname
        self.__age__ = age
        self.__gender__ = gender
        self.__nationality__ = nationality

    def set_name(self, name):
        self.__name__ = name

    def set_familyname(self, familyname):
        self.__familyname__ = familyname

    def set_age(self, age):
        self.__age__ = age

    def set_gender(self, gender):
        self.__gender__ = gender

    def set_nationality(self, nationality):
        self.__nationality__ = nationality

    def get_info(self):
        information = {"name": self.__name__, "familyname": self.__familyname__, "age": self.__age__, "gender": self.__gender__, "nationality": self.__nationality__}
        return information


class Student(Human):
    def __init__(self, id, name, familyname, age, gender, nationality, school, subjects):
        super().__init__(name, familyname, age, gender, nationality)
        self.__id__ = id
        self.__school__ = school
        self.__subjects__ = set()
        if type(subjects) == str:
            self.__subjects__.add(subjects)
        elif type(subjects) == list:
            for subject in subjects:
                self.__subjects__.add(subject)

    def set_school(self, school):
        self.__school__ = school

    def add_subject(self, *subjects):
        for subject in subjects:
            self.__subjects__.add(subject)

    def get_info(self):
        information = super().get_info()
        information["id"] = self.__id__
        information["school"] = self.__school__
        information["subjects"] = self.__subjects__
        return information


class Teacher(Human):
    def __init__(self, id, name, familyname, age, gender, nationality, school, subjects):
        super().__init__(name, familyname, age, gender, nationality)
        self.__id__ = id
        self.__school__ = school
        self.__subjects__ = set()
        if type(subjects) == str:
            self.__subjects__.add(subjects)
        elif type(subjects) == list:
            for subject in subjects:
                self.__subjects__.add(subject)

    def set_school(self, school):
        self.__school__ = school

    def add_subject(self, *subjects):
        for subject in subjects:
            self.__subjects__.add(subject)

    def get_info(self):
        information = super().get_info()
        information["id"] = self.__id__
        information["school"] = self.__school__
        information["subjects"] = self.__subjects__
        return information


print("The module Users was successfully imported.")
