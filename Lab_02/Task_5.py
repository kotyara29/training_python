import string

sentence = list("I am@Python@senior^pomidor")
new_list = []
for i in range(len(sentence)):
    if sentence[i] in string.punctuation:
        sentence[i] = ' '
        new_list.append(sentence[i])
    else:
        new_list.append(sentence[i])
output = "".join(new_list)


# for word in list_with_words:
#     if not word in string.punctuation:
#         new_list.append(word)


print(output)