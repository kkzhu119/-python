# import RandomCharacter
#
# NUMBER_OF_CHARS = 175  # 去随机生成的字符的个数
# CHARS_PER_LINE = 25  # 每一行去展示的字符的个数
#
#
# for i in range(NUMBER_OF_CHARS):
#     print(RandomCharacter.getRandomLowerCaseLetter(), end = " ")
#     if(i + 1) % CHARS_PER_LINE == 0:
#         print()  # 跳到下一行

from Course import *

newco = Course("Chinese")


newco.addStudent("小李")

newco.addStudent("小张")

newco.addStudent("小王")

newco.addStudent("小明")

print(newco.getNumberOfStudents())

print(newco.getCourseName())

print(newco.dropStudent("小李"))
newco.showStudentsName()
print(newco.getNumberOfStudents())


