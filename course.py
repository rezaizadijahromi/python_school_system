from professor import Professor
from enrol import Enroll


class Course:
    def __init__(self, name, code, max_, min_, porfessor):
        self.name = name
        self.code = code
        self.max = max_
        self.min = min_
        self.porfessores = []
        self.enrollments = []

        if isinstance(porfessor, Professor):
            self.porfessores.append(porfessor)
        elif isinstance(porfessor, list):
            for entry in porfessor:
                if not isinstance(entry, porfessor):
                    raise Error("Invalid professor...")

            self.porfessores = porfessor

        else:
            raise Error("Invalid professor")


    def add_professor(self, professor):
        if not isinstance(professor, Professor):
            raise Error("invalid professor...")

        self.porfessores.append(professor)

    def add_enrollments(self, enroll):
        if not isinstance(enroll, Enroll):
            raise Error("Invalid Enroll...")

        if len(enrollments) == self.max:
            raise Error("Cannot enroll, course is full")

        self.enrollments.append(enroll)

    def is_cancelled(self):
        return len(self.enrollments) < self.min




        