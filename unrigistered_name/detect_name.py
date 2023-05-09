import nltk
nltk.download('words')
print(type(nltk.corpus.words.words()))

# create 4-letter word txt file
# create 5-letter word txt file
four_letter_name = open('4_letter_name.txt', 'a')
five_letter_name = open('5_letter_name.txt', 'a')

for word in nltk.corpus.words.words():
    if len(word) == 4:
        four_letter_name.write(word + '\n')
    elif len(word) == 5:
        five_letter_name.write(word + '\n')

four_letter_name.close()
five_letter_name.close()