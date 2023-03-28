import wikipedia


def wiki(name="War Goddess", length=1):
    """wiki fetcher"""
    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def wiki_search(name="War Goddess", length=1):
    """wiki search"""
    my_wiki = wikipedia.search(name, length)
    return my_wiki
