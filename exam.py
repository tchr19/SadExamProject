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
        

    