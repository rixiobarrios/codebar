# Write your code here!
class Member:
    def __init__(self, full_name):
        self.full_name = full_name
        # print('(Member: {})'.format(self.full_name))

    def introduce(self):
        return f'Hello, my name is {self.full_name}'
        # print('Name:"{}"'.format(self.full_name), end=" ")


class Student(Member):
    def __init__(self, full_name, reason):
        Member.__init__(self, full_name)
        self.reason = reason
        # print('(Student: {})'.format(self.full_name))


class Instructor(Member):
    def __init__(self, full_name, bio):
        Member.__init__(self, full_name)
        self.bio = bio
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)


class Workshop():
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.instructors = []
        self.students = []

    def add_participant(self, member):
        if member.__class__.__name__ == 'Student':
            self.students.append(member)
        else:
            self.instructors.append(member)

    def print_details(self):
        print(f'Workshop-{self.date}-{self.subject}')
        i = 1
        print('Students')
        for student in self.students:
            print(f'{i}. {student.full_name}, {student.reason}')
            i += 1
        print('Instructors')
        j = 1
        for instructor in self.instructors:
            skills_arr = ''
            for skill in instructor.skills:
                if len(skills_arr) == 0:
                    skills_arr += skill
                else:
                    skills_arr += (", " + skill)
            print(
                f'{j}. {instructor.full_name}, {skills_arr}, {instructor.bio}')
            j += 1


workshop = Workshop("12/03/2014", "Shutl")

jane = Student(
    "Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor(
    "Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()
