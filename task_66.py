# Для данной буквы английского алфавита нужно вывести справа стоящую букву
# на стандартной клавиатуре. При этом клавиатура замкнута,
# т.е. справа от буквы «p» стоит буква «a»,
# от буквы «l» стоит буква «z», а от буквы «m» — буква «q».
# В выходной файл следует вывести букву стоящую справа от заданной буквы, с учетом замкнутости клавиатуры.

# def search_word(word: str):
    #string = "qwertyuiopasdfghjklzxcvbnm"
    #index = string.index(word)
    #return string[(index + 1) % len(string)]

    # for element in range(0, len(string)):
    #     if string[element] == word:
    #             return string[0]
    #     if element != len(string):
    #         if string[element] == word:
    #             return string[element + 1]
    # return None


# print(search_word('x'))


# elem = input()
# string = "qwertyuiopasdfghjklzxcvbnm"
#
# for element in range(0, len(string)):
#     string = "qwertyuiopasdfghjklzxcvbnm"
#     if element == element:
#         print(string[0])
#     if element != len(string):
#         if string[element] == elem:
#             print(string[element - 1])


# Этот вариант решения приняли автотесты
my_el = input()
string = "qwertyuiopasdfghjklzxcvbnm"
index = string.index(my_el)
print(string[(index + 1) % len(string)])