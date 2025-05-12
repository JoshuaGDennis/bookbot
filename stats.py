def count_words(text):
    num_words = len(text.split())
    return f"{num_words} words found in the document"


def get_character_dict(text):
    dict = {}

    for char in text:
        lowered = char.lower()
        if lowered not in dict:
            dict[lowered] = 1
        else:
            dict[lowered] += 1

    return dict


def get_sorted_list(dict):
    list = []

    def sort_on(dict):
        return dict["num"]

    for item in dict:
        list.append({"char": item, "num": dict[item]})

    list.sort(reverse=True, key=sort_on)

    return list
