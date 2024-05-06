"""
I add another fuction to print out the out put.
I also added the preposition to the make_sentance. 

"""
import random


def main():
    # quantity = int(input('Single or plural? (Use 1 or 0 for your answers.) '))
    # tense = input('Past, present or future tense.? ')
    # sentence = make_sentence(quantity, tense)

    printing_sentences()

def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    sentence = (f'{get_determiner(quantity)} {get_noun(quantity)} {get_prepositional_phrase(quantity)} {get_verb(quantity, tense)} {get_prepositional_phrase(quantity)}')
    return sentence

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like 'the', 'a', 'one', 'some', 'many'.
    If quantity is 1, this function will return either 'a',
    'one', or 'the'. Otherwise this function will return
    either ['some', 'many', 'the'].

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ['a', 'one', 'the']
    else:
        words = ['some', 'many', 'the']

    # Randomly choose and return a determiner.
    word = random.choice(words)
    word = word.capitalize()
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        ['bird', 'boy', 'car', 'cat', 'child',
        'dog', 'girl', 'man', 'rabbit', 'woman']
    Otherwise, this function will return one of
    these ten plural nouns:
        ['birds', 'boys', 'cars', 'cats', 'childs',
        'dogs', 'girls', 'mans', 'rabbits', 'womans']

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """

    if quantity == 1:
        words = ['bird', 'boy', 'car', 'cat', 'child',
        'dog', 'girl', 'man', 'rabbit', 'woman']
    else:
        words = ['birds', 'boys', 'cars', 'cats', 'childs',
        'dogs', 'girls', 'mans', 'rabbits', 'womans']
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == 'past'.lower():
        words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense == 'present'.lower() and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == 'present'.lower() and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    elif tense == 'future'.lower():
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    word = random.choice(words)
    return word

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        'about', 'above', 'across', 'after', 'along',
        'around', 'at', 'before', 'behind', 'below',
        'beyond', 'by', 'despite', 'except', 'for',
        'from', 'in', 'into', 'near', 'of',
        'off', 'on', 'onto', 'out', 'over',
        'past', 'to', 'under', 'with', 'without'

    Return: a randomly chosen preposition.
    """
    words = ['about', 'above', 'across', 'after', 'along',
        'around', 'at', 'before', 'behind', 'below',
        'beyond', 'by', 'despite', 'except', 'for',
        'from', 'in', 'into', 'near', 'of',
        'off', 'on', 'onto', 'out', 'over',
        'past', 'to', 'under', 'with', 'without']
    word = random.choice(words) 
    return word


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    sentence = (f'{get_preposition()} {get_determiner(quantity).lower()} {get_noun(quantity)}')
    return sentence

def printing_sentences():
    count = 0
    while count != 1:
        output = print(f'{make_sentence(1, 'past')} \n{make_sentence(1, 'present')}, \n{make_sentence(1, 'future')} \n{make_sentence(0, 'past')}, \n{make_sentence(0, 'present')} \n{make_sentence(0, 'future')}')
        count += 1
    return output

    
# calling the main function.
main()
