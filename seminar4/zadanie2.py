# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.
from string import punctuation
line = """She. sells sea shells on the sea shore 
The shells that. she sells are sea shells) Im sure So if:
 she sells sea shells/ on the sea shore Im sure that the shells are sea shore shells"""
for x in punctuation:
    line = line.replace(x, '')
line = line.lower().split()
print(len(set(line)))