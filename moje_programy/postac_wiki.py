import wikipedia
wikipedia.set_lang("pl")
def description_wiki(postac):
    return wikipedia.summary(postac)
def sort_description(e):
    return e[2]