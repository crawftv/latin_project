#!/usr/bin/env python3
from enum import Enum, auto


class Mood(Enum):
    INDICATIVE = 1
    IMPERATIVE = 2
    SUBJUNCTIVE = 3
    OPTATIVE = 4


class Voice(Enum):
    ACTIVE = 1
    MIDDLE = 2
    PASSIVE = 3


class Person(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3


class Number(Enum):
    SINGULAR = 1
    DUAL = 2
    PLURAL = 3


class Tense(Enum):
    PRESENT = 1
    IMPERFECT = 2
    FUTURE = 3
    AORIST = 4
    PERFECT = 5
    PLUPERFECT = 6
    FUTURE_PERFECT = 7


class Case(Enum):
    NOMINATIVE = 1
    GENITIVE = 2
    DATIVE = 3
    ACCUSATIVE = 4
    VOCATIVE = 5


class Declension(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3


class Gender(Enum):
    MASCULINE = 1
    FEMININE = 2
    NEUTERED = 3


class WordMixin:
    def __init__(self, *, greek, english, root):
        self.greek = greek
        self.english = english
        self.root = root
        super().__init__()


class Noun(WordMixin):
    def __init__(self, number, gender, case):
        self.number = number
        self.gender = gender
        self.case = case

class Pronoun(Noun):
    def __init__(self):
        super().__init__()


class Adjective(Noun):
    def __init__(self):
        super().__init__()


class Conjunction(WordMixin):
    def __init__(self, part):
        self.part = part


class Article(WordMixin):
    def __init__(self, number, gender, case, declension):
        self.number = number
        self.gender = gender
        self.case = case
        self.declension = declension


class Verb(WordMixin):
    def __init__(
        self, person: Person, number: Number, tense: Tense, voice: Voice, mood: Mood
    ):
        self.person = person
        self.number = number
        self.tense = tense
        self.voice = voice
        self.mood = mood


class Participle(WordMixin):
    def __init__(self,):
        self.number = number
        self.gender = gender
        self.voice = voice
        self.case = case
        self.tense = tense
