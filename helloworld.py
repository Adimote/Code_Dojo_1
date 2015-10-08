import random
from enum import Enum
class Noun_Type(Enum):
    unspecified = 0
    animal = 1
    human = 2
    inanimate = 3

class Article_Type(Enum):
    improper = 0
    human = 2
    inanimate = 3


# Word before the noun

nouns = [("cat", Noun_Type.animal), ("mat", Noun_Type.inanimate), ("banana", Noun_Type.inanimate), ("code dojo", Noun_Type.inanimate), ("Tom", Noun_Type.human)]

verbs = ["cat", "mat", "banana", "code dojo", "Tom"]
articles = [("The", Article_Type.improper), ("Their", Article_Type.improper), ("My", Article_Type.improper), ("A", Article_Type.improper), ("", Article_Type.human), ("Sir", Article_Type.human)]

def pick_article_from_noun(noun_type):
    if noun_type is not Noun_Type.human:
        return random.choice([x for x in articles if x[1] is Article_Type.improper])
    else:
        return random.choice([x for x in articles if x[1] is Article_Type.human])


noun = random.choice(nouns)
article = pick_article_from_noun(noun[1])
print("{0} {1}!".format(article[0], noun[0]))