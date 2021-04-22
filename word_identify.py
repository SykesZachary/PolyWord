### Core poly-word decipher
### 19.03.2021

from collections import Counter
import re, os


def table_builder(id_words):
    pass


# Trims the identified words to the broader poly-word rules
def rules_trim(id_words):
    
    with open('disallowed_words.txt', 'r') as file:
        for line in file:
            line = line.strip()
            line = line.lower()

            for idx,item in enumerate(id_words):
                if line == item:
                   id_words[idx] = (item, 'possible invalid')

            for idx, item in enumerate(id_words):
                if line == item:
                    id_words[idx] = (item, 'possible invalid')

            
        print(id_words)
        print(len(id_words))
        

# Finds the possible words for the day
def poly_words(key_word, peripheral):

    word_match = []
    nine_letter = []

    all_letts = list(peripheral + key_word)

    with open('words.txt', 'r') as file:
        for line in file:
            line = line.strip()
            line = line.lower()
            if len(line) >= 4 and '\'' not in line:
                if Counter(key_word + peripheral) == Counter(line):
                    nine_letter.append(line)
                
                potential_word = ''
                c1, c2 = Counter(list(line)), Counter(all_letts)
                for k, n in c1.items():
                    if k in c2.keys() and c1[k] <= c2[k]:
                        potential_word += k
                    else:
                        continue
                if set(potential_word).issuperset(set(line)):

                    if key_word in set(potential_word):
                        word_match.append(line)
                            
    file.close()

            if key_word in set(potential_word) and line not in word_match:
                word_match.append(line)

    rules_trim(word_match)


# Will eventually be filled with the image processing return
poly_words('b', 'ryittalu')
