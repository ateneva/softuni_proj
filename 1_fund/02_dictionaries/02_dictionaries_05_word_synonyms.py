
# ========================05.word synonyms -------------------------------------

'''
Write a program, which keeps a dictionary with synonyms.
The key of the dictionary will be the word.
The value will be a list of all the synonyms of that word.
You will be given a number n – the count of the words.
After each word, you will be given a synonym,
    so the count of lines you have to read from the console is 2 * n.
You will be receiving a word and a synonym each on a separate line like this:
    • {word}
    • {synonym}
If you get the same word twice, just add the new synonym to the list.
Print the words in the following format:
{word} - {synonym1, synonym2… synonymN}
'''

word_count = int(input())
synonyms = {}

for i in range(1, word_count + 1):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []             # create a list within a dictionary
    synonyms[word].append(synonym)


for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")
