#! /usr/bin/python3

def reverse_word(string):

    dictionar_of_words=[]
    list_of_words=string.split()
    for word in list_of_words:
        name= ""
        for letter in word:
            name=letter+name
        dictionar_of_words.append(name)
    dictionar_of_words=" ".join(dictionar_of_words)
    return dictionar_of_words




string="my name is ali"
result=reverse_word(string)
print(result)
