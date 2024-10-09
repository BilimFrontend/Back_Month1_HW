word = input("Введите любое слово: ")
letters = 0

consonants = "bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ"
vowels = "aeiouyаиоуыэ"

consonants_count = 0
vowels_count = 0

for letter in word.lower():
    letters += 1
    for consonant in consonants:
        if consonant in letter:
            consonants_count += 1
    for vowel in vowels:
        if vowel in letter:
            vowels_count += 1

percent_consonants = (consonants_count / letters) * 100
percent_vowels = (vowels_count / letters) * 100

print(f"Слово: {word}\nКоличество букв: {letters}\nСогласных букв: {consonants_count}\nГласных букв: {vowels_count}\nГласные/Согласные: {percent_vowels}%/{percent_consonants}%")
