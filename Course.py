class Course:
    def __init__(self, courseName):
        self.__courseName = courseName
        self.__students = []

    def addStudent(self, student):
        self.__students.append(student)

    def getStudents(self):
        return self.__students

    def getNumberOfStudents(self):
        return len(self.__students)

    def getCourseName(self):
        return self.__courseName

    def showStudentsName(self):
        print(self.__students)

    def dropStudent(self, student):
        for i in range(0, len(self.__students)):
            if self.__students[i] == student:
                print("删除%s成功" % self.__students[i])
                del self.__students[i]
                break
        else:
            print("没有找到这个元素")



        # i = 0
        # totalnum = len(self.__students)
        # while i < totalnum:
        #     if(self.__students[i] == student):
        #         print("删除%s成功" %self.__students[i])
        #         del self.__students[i]
        #         break;
        #     i = i + 1
        #
        # if(i == totalnum):
        #     print("没有找到这个元素")
        #     return
        # else:
        #     return





