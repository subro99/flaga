import random
import string

# liczba_punct=2
# liczba_dig=2
# liczba_upper=2
# liczba_lower=2
def generator_hasla(liczba_znakow):
    znaki=[2,2,2,2]
    while sum(znaki)<liczba_znakow:
        i=random.randint(0,3)
        znaki[i]+=1
    punct=string.punctuation
    dig=string.digits
    uppercase=string.ascii_uppercase
    lowercase=string.ascii_lowercase
    haslo=random.sample(punct,znaki[0])+random.sample(dig,znaki[1])+random.sample(uppercase,znaki[2])+random.sample(lowercase,znaki[3])
    haslo=random.sample(haslo,len(haslo))
    haslo="".join(haslo)
    return haslo