import re

word1 = input("Introduceti primul cuvant: ")
word2 = input("Introduceti al doilea cuvant: ")

sentence = input("Introduceti propozitia: ")

result = re.sub(r'\b' + re.escape(word1) + r'\b', word2, sentence)

print("Modified sentence: ", result)
