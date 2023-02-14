import string

sentence = "I am@Python@senior^pomidor"
list_with_words = sentence.split()
new_list = []
def old_function():
    for word in list_with_words:
        if not word in string.punctuation:
            new_list.append(word)
    return new_list

def filter_option():
    filtered = list(filter(lambda x: x not in string.punctuation, list_with_words))
    return filtered

def cherez_map(sentence):
    pure_sentence = "".join(list(map(lambda x: x if x not in string.punctuation else " ", sentence)))
    return pure_sentence

def new_option():
    return sentence.split()


print(f"Initial output: {old_function()}")
# #print(string.punctuation)
print(f"Another output: {new_option()}")
print(f"Another output with filter: {filter_option()}")
print(f"Our joint effort looks like this: {cherez_map(sentence)}")
