#!/usr/bin/python3
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

class Verb_Type(Enum):
    either = 0
    inanimate = 1
    animate = 2


class Prepositions(Enum):
    on_ = 0
    in_ = 1


# Word before the noun

nouns = [("cat", Noun_Type.animal), ("mat", Noun_Type.inanimate), ("banana", Noun_Type.inanimate),
         ("code dojo", Noun_Type.inanimate), ("Tom", Noun_Type.human)]

articles = [("the", Article_Type.improper), ("their", Article_Type.improper), ("my", Article_Type.improper),
            ("a", Article_Type.improper), ("", Article_Type.human), ("sir", Article_Type.human)]

verbs = [("sat", Verb_Type.either, [Prepositions.on_, Prepositions.in_]),
         ("jumped", Verb_Type.animate, [Prepositions.on_, Prepositions.in_]),
         ("ran", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_])]


def pick_article_from_noun(noun_type):
    if noun_type is not Noun_Type.human:
        return random.choice([x for x in articles if x[1] is Article_Type.improper])
    else:
        return random.choice([x for x in articles if x[1] is Article_Type.human])


def pick_verb_from_noun(noun_type):
    if noun_type is Noun_Type.inanimate:
        return random.choice([x for x in verbs if x[1] in [Verb_Type.inanimate, Verb_Type.either]])
    else:
        return random.choice([x for x in verbs if x[1] in [Verb_Type.animate, Verb_Type.either]])


def pick_preposition_from_verb(verb):
    chosen = random.choice(verb[2])
    if chosen is Prepositions.in_:
        return "in"
    elif chosen is Prepositions.on_:
        return "on"
    else:
        raise Exception("Oh No you forgot to set a string for a preposition value!! what a bummer.")


def sentence_1():
    noun = random.choice(nouns)
    article = pick_article_from_noun(noun[1])
    verb = pick_verb_from_noun(noun[1])
    preposition = pick_preposition_from_verb(verb)
    noun2 = random.choice(nouns)
    article2 = pick_article_from_noun(noun2[1])

    return "{} {} {} {} {} {}!".format(article[0], noun[0], verb[0], preposition, article2[0], noun2[0])

def sentence_2():
    noun = random.choice(nouns)
    article = pick_article_from_noun(noun[1])
    verb = pick_verb_from_noun(noun[1])
    preposition = pick_preposition_from_verb(verb)
    noun2 = random.choice(nouns)

    return "{} {} {} {} {}!".format(article[0], noun[0], verb[0], preposition, noun2[0])

print(sentence_1())

