import csv
import os


def write_school_data_to_csv(school, filename):
    dict_school = school.get_info()
    f = open(filename, "w", newline="")
    w = csv.DictWriter(f, dict_school.keys())
    w.writeheader()
    w.writerow(dict_school)
    w = csv.DictWriter(f, ["name", "familyname", "age", "gender", "nationality", "id", "school", "subjects", "person_role"])
    w.writeheader()
    for student in school.__students__:
        dict_stud = student.get_info()
        dict_stud['person_role'] = 'student'
        w.writerow(dict_stud)
    for teacher in school.__teachers__:
        dict_teacher = teacher.get_info()
        dict_teacher['person_role'] = 'teacher'
        w = csv.DictWriter(f, dict_teacher.keys())
        w.writerow(dict_teacher)
    f.close()


class School:
    def __init__(self, name=None, address=None, phone=None, email=None):
        self.__name__ = name
        self.__address__ = address
        self.__phone__ = phone
        self.__email__ = email
        self.__num_stud__ = 0
        self.__num_teachers__ = 0
        self.__students__ = []
        self.__teachers__ = []

    def set_name(self, name):
        self.__name__ = name

    def set_address(self, address):
        self.__address__ = address

    def set_phone(self, phone):
        self.__phone__ = phone

    def set_email(self, email):
        self.__email__ = email

    def set_num_stud(self, num_stud):
        self.__num_stud__ = num_stud

    def set_num_teachers(self, num_teachers):
        self.__num_teachers__ = num_teachers

    def add_student(self, student):
        ids = [student.__id__ for student in self.__students__]
        if student.__id__ not in ids:
            self.__students__.append(student)
            self.__num_stud__ += 1

    def add_teacher(self, teacher):
        ids = [teacher.__id__ for teacher in self.__teachers__]
        if teacher.__id__ not in ids:
            self.__teachers__.append(teacher)
            self.__num_teachers__ += 1

    def get_info(self):
        school_info = {"school_name": self.__name__,
                       "address": self.__address__,
                       "phone": self.__phone__,
                       "email": self.__email__,
                       "num_stud": self.__num_stud__,
                       "num_teachers": self.__num_teachers__}
        return school_info

    def get_report(self):
        cur_dir = os.getcwd()
        path_to_report = os.path.join(cur_dir, "report.csv")
        if os.path.exists(path_to_report):
            f = open("report.csv", "a", newline="")
            for student in self.__students__:
                dict_stud = student.get_info()
                dict_stud['person_role'] = 'student'
                w = csv.DictWriter(f, dict_stud.keys())
                w.writerow(dict_stud)
            for teacher in self.__teachers__:
                dict_teacher = teacher.get_info()
                dict_teacher['person_role'] = 'teacher'
                w = csv.DictWriter(f, dict_teacher.keys())
                w.writerow(dict_teacher)
            f.close()
        else:
            dict_school = self.get_info()
            f = open("report.csv", "w", newline="")
            w = csv.DictWriter(f, dict_school.keys())
            w.writeheader()
            w.writerow(dict_school)
            w = csv.DictWriter(f, ["id", "name", "familyname", "age", "gender", "nationality", "school", "subjects",
                                   "person_role"])
            w.writeheader()
            for student in self.__students__:
                dict_stud = student.get_info()
                dict_stud['person_role'] = 'student'
                w.writerow(dict_stud)
            for teacher in self.__teachers__:
                dict_teacher = teacher.get_info()
                dict_teacher['person_role'] = 'teacher'
                w = csv.DictWriter(f, dict_teacher.keys())
                w.writerow(dict_teacher)
            f.close()
        print("Report was successfully created")
        pass


print("The module Organizations was successfully imported.")
