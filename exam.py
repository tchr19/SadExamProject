# The exam class is responsible for containing all high level information about a registered exam.
# The constructor takes various arguments regarding practical information about the exam, which should be inputted when the exam is registered.
class exam:
    grade = None
    handIn = None
    attatchment = None
    censor = None
    studentID = None
    examDesc = None

    def __init__(self, examName, course, ECTS, date, teacher, gradingScale, examType):
        self.date = date
        self.teacher = teacher
        self.ECTS = ECTS
        self.gradingScale = gradingScale
        self.examType = examType
        self.examName = examName
        self.course = course
        

    