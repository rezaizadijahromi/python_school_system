from person import Person

class Professor(Person):
    def __init__(self, first, last, dob, phone, address, salary):
        super().__init__(first, last, dob, phone, address)
        
        self.salary = salary
        self.courses = []
        self.got_raise = False

    def check_for_raise(self):
        if len(self.courses) >= 4 and not self.got_raise:
            self.salary += 20000
            self.got_raise = True

    