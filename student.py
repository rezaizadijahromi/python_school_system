from person import Person
from enroll import Enroll

class Student(Person):
    def __init__(self, first, last, dob, phone, address, international=False):
        super().__init__(self, first, last, dob, phone, address)
        self.internation = international
        self.enrolled = []

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise Error("Invalid Enroll...")
        self.enrolled.append(enroll)

    def is_on_probation(self):
        pass

    def is_part_time(self):
        pass