class School:

    def __init__(self, first, last, pocket):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pocket = pocket

    def fullname(self):
        return f'my full name is {self.first} {self.last}'

    def email(self):
        return f'my email is {self.email}'

    def apply_raise(self):
        self.pocket = int(self.pocket)


student = School('Mustaffa ', 'Zack', str(7000))
teacher = School('Kamal ', 'Seth', str(60000))
print("Student:")
print("Full Name:" + student.first + student.last)
print("Email:" + student.email)
print("Pocket Money:" + student.pocket)
print("Teacher:")
print("Full Name:" + teacher.first + teacher.last)
print("Email:" + teacher.email)
print("Pocket Money:" + teacher.pocket)
