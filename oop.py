from random import randint

class Student:
    def __init__(self, first_name, last_name, _zipcode, _classesNum, grade):  # Constructor
        self.first_name = first_name
        self.last_name = last_name
        self.id = hex(randint(16 ^ 10, (16 ^ 11) - 1))
        self.grade = grade
        self._zipcode = _zipcode  # Protected class variable
        self._classesNum = _classesNum  # Same here

        """
        Types of access modifiers:

        1) protected-available to child classes and that class(you can get around this)
        2) private-available only to that class, child classes not allowed(you can also get around this)
        3) public-available anywhere in the program
        """

    def years_till_grad(self):  # Normal class method
        return 12 - self.grade

    # In this simulation of school, here is how you would keep them from secretly skipping class.(unless you know the secret syntax)
    # The reason is this can't be accessed in main.py, but the go_to_school function can
    # So you go to school the whole time or for no time, no skipping in this simulation.
    def _attendClass(self, id):
        print(f"{self.first_name} attended class {id}.")

    def go_to_school(self):
        # Just note that random class IDs will be generated each time function is called.
        for c in range(self._classesNum):
            _class = randint(65536,1048575)
            self._attendClass(hex(_class))

    def __repr__(self):  # Doesn't really help with anything front end, but helps programmers see if class is working with ease
        """
        Example when this dunder method is activated:

        u = Student(Askar,Akayev,73659,11)
        print(u)
        """
        return "%s %s with ID %s is in %s grade and lives at %s. They attend %s classes" % (self.first_name, self.last_name, self.id, self.grade, self._zipcode, self._classesNum)


class Senior(Student):  # Child class for senior
    def __init__(self, first_name, last_name,_zipcode,_classesNum, grade=12):
        super().__init__(first_name, last_name,_zipcode,_classesNum,grade)  # This already does all the self.___ due to all the variables being inherited.
        self.colleges = []

    def apply_for_colleges(self, *colleges):
        print(f"{self.first_name}, you have applied for the following colleges:")
        for college in colleges:
            print(f' - {college}')

        self.colleges.extend(colleges)


class Junior(Student):  # Child class for junior
    def __init__(self, first_name, last_name, _zipcode,_classesNum, grade=11):
        super().__init__(first_name, last_name,_zipcode,_classesNum, grade)
        self.satScore = None

    def completeSAT(self,studyHrs):
        self.satScore = (studyHrs * 10) ** 2
        if self.satScore > 1600:
            self.satScore = 1600
        print(f"{self.first_name}, you got a {self.satScore} on the SAT")

    def visitColleges(self, *colleges):
        print(f"{self.first_name}, you just signed up to visit these colleges")
        for college in colleges:
            print(f' - {college}')