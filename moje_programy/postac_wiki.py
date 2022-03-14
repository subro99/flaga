import wikipedia
wikipedia.set_lang("pl")
def opis_wiki(postac):
    return wikipedia.summary(postac)