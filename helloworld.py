#!/usr/bin/python3
import random
import re
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
         ("ran", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("began", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("broke", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("brought", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("bought", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("built", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("chose", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("came", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("cost", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("cut", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("did", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("drew", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("drove", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("ate", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("felt", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("found", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("got", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("gave", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("went", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("had", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("heard", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("held", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("kept", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("knew", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("left", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("led", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("let", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("lay", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("lost", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("made", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("meant", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("met", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("paid", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("put", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("ran", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("said", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("sold", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("sent", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("set", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("sat", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("spoke", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("spent", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("stood", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("took", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("taught", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("told", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("thought", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("understood", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("wore", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("won", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("wrote", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("accepted", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("achieved", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("added", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("admired", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("admitted", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("adopted", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("advised", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("agreed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("allowed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("announced", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("appreciated", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("approved", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("argued", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("arrived", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("asked", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("assisted", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("attacked", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("baked", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("begged", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("behaved", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("boiled", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("borrowed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("brushed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("buried", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("called", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("challenged", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("changed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("chased", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("cheated", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("cheered", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("chewed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("clapped", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("cleaned", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("collected", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("compared", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("complained", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("confessed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("constructed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("controlled", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("copied", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("counted", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("created", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("cried", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("cycled", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("damaged", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("danced", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("delivered", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("destroyed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("divided", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("dragged", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("earned", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("employed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("encouraged", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("enjoyed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("established", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("estimated", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("exercised", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("expanded", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("explained", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("fried", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("gathered", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("greeted", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("guessed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("harassed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("hated", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("helped", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("hoped", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("identified", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("interrupted", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("introduced", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("irritated", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("joked", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("jumped", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("kicked", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("killed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("kissed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("laughed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("lied", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("liked", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("listened", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("loved", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("married", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("measured", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("moved", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("murdered", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("needed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("obeyed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("offended", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("offered", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("opened", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("painted", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("parked", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("phoned", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("picked", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("played", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("prayed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("printed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("pulled", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("punched", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("punished", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("purchased", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("pushed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("questioned", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("raced", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("relaxed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("remembered", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("replied", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("retired", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("returned", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("rubbed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("scolded", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("selected", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("smoked", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("snored", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("stared", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("started", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("studied", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("talked", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("thanked", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("travelled", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("troubled", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("typed", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("used", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("visited", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("waited", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("walked", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("wanted", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("warned", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("winked", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("worried", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("yelled", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_]),
         ("", Verb_Type.inanimate, [Prepositions.on_, Prepositions.in_])]


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

    return "{} {} {} {} {} {}".format(article[0], noun[0], verb[0], preposition, article2[0], noun2[0])

def capitalise(string):
    a = string[0].upper()+string[1:]+"."
    a2 = re.sub("  ", " ", a)
    return re.sub("^ ", "", a2)


for i in range(100):
    print(capitalise(sentence_1()))

