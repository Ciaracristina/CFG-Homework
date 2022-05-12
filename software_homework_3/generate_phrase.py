"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you cab generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""

def generate_phrase(characters, phrase):
    pass



class GeneratePhrase:

    characters = 'lymgyatoirl'
    phrase = 'margotlily'

# we want function to create a dictionary to represent the character count in a phrase
# e.g eabcedd
# {a:1, b:1, c:1, d:2, e:2}

def transform_to_dict(characters):

    character_count = {}
    for character in characters:
        add_or_increment(character_count, character)
    return character_count

# if character is not in dictionary, add and set to 1. If
# character is in dictionary, increment count by 1.
def add_or_increment(character_count, character):
    if character not in character_count:
        character_count[character] = 1
    else:
        character_count[character] = character_count[character] + 1

def test_phrase(characters, phrase):
    character_count = transform_to_dict(characters)
    for letter in phrase:
        if letter in character_count:
            count = character_count[letter]
            if count >= 1:
                character_count[letter] = count - 1
            else:
                return False
        else:
            return False
    return True

test_phrase('abc', 'cbad')







