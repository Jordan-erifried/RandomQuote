import json
import random


def read_values_from_json(path, key):
    values = []
    with open(path) as f:
        data = json.load(f)
        for entry in data:
            values.append(entry[key])
        return values


def clean_strings(sentences):
    cleanned = []
    for sentence in sentences:
        clean_sentence = sentence.strip()
        cleanned.append(clean_sentence)
    return cleanned


def random_item_in(object_list):
    rand_numb = random.randint(0, len(object_list) - 1)
    return object_list[rand_numb]


def random_values(source_path, key):
    all_values = read_values_from_json(source_path, key)
    clean_values = clean_strings(all_values)
    return random_item_in(clean_values)


def random_quote():
    return random_values('quotes.json', 'quote')


def random_names():
    return random_values('names.json', 'name')


def print_random_sentences():
    rand_quote = random_quote()
    rand_name = random_names()
    print('>>> {} a dit {}'.format(rand_name, rand_quote))


def main_loop():
    while True:
        print_random_sentences()
        message = ('Pour connaitre plus d citation tapez [entree].',
                   'Pour sortir du programme tapez [B] ou [b]')
        choice = input(message).upper()

        if choice == "B":
            break


if __name__ == '__main__':
    main_loop()
