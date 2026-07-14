# Classwork 09 - Spanish Verb Conjugator

# PROCESS - Define pronouns list and conjugation endings dictionary
subject_pronouns = ['Yo', 'Tu', 'El', 'Nosotros', 'Vosotros', 'Ellos']

conjugation_endings = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

# INPUT - Ask user for a Spanish verb
try:
    infinitive = input("Write a Spanish verb (ar/er/ir): ")

    if len(infinitive) < 3:
        raise ValueError("The verb is too short to be valid.")

    # PROCESS - Extract stem and ending, then look up conjugations
    verb_root = infinitive[:-2]
    verb_type = infinitive[-2:]

    if verb_type not in conjugation_endings:
        raise KeyError(verb_type)

    ending_list = conjugation_endings[verb_type]

    # OUTPUT - Print all six conjugations
    for position, subject in enumerate(subject_pronouns):
        print(f"{subject} {verb_root}{ending_list[position]}")

except ValueError as error:
    print(f"Error: {error}")
except KeyError as error:
    print(f"Error: '{error}' is not a valid Spanish verb ending. Only 'ar', 'er', and 'ir' are supported.")