import RandomCharacter

NUMBER_OF_CHARS = 175  # 去随机生成的字符的个数
CHARS_PER_LINE = 25  # 每一行去展示的字符的个数


for i in range(NUMBER_OF_CHARS):
    print(RandomCharacter.getRandomLowerCaseLetter(), end = " ")
    if(i + 1) % CHARS_PER_LINE == 0:
        print()  # 跳到下一行

