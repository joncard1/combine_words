def combine_words(word1, word2):
    set_1 = set(word1)
    set_2 = set(word2)
    total_len = len(set_1) + len(set_2)
    set_1.update(set_2)
    if len(set_1) != total_len:
        return 0
    else:
        return len(word1) * len(word2)

def word_mapper(word):
    return (word.strip(), len(word.strip()))

def word_sorter(word_tuple):
    return word_tuple[1]


with open('words.txt') as f:
    words = f.readlines()

# This should be O(nlg(n)), as it operates in O(n) for the map, and O(nlg(n)) for
# the sort
word_collection = sorted(map(word_mapper, words), key=word_sorter, reverse=True)

score = 0
if len(word_collection) == 0:
    # Something bad, but can't think right now what it should be. Error,
    # because there were not words in the file, I suppose. I'd prefer to
    # throw an error and so unwrap the following, but I put this in a
    # script file instead of a function definition for some reason and so
    # that doesn't look right.
    pass
else:
    # An O(1) operation just to collect the indexes of the breaks between
    # word lengths. This can probably be collected as I iterate through
    # the collection, but I don't care to optimize it that much.
    max_length = word_collection[0][1]
    index_list = [0] * max_length
    i = 0
    for word_tuple in word_collection:
        if index_list[word_tuple[1] - 1] == 0:
            index_list[word_tuple[1] - 1] = i
        i += 1

    # The premise here is that the maximum area within a rectangle of 
    # given perimeter is when it is a square, and the square of a number
    # is going to be greater than the product of a number 1 greater and a
    # number 1 smaller [That is to say, n^2 - 1 = (n - 1)(n + 1), or 
    # n^2 = (n - 1)(n + 1) + 1]. Therefore, to search for the greatest
    # possible product in descending order amongst possible operands, we
    # have sorted the potential multipliers and muliplicands and only
    # need to check in order by decreasing the multiplicands one at a
    # time and checking the mulipliers in decreasing order against them.
    # For instance, if the largest word is 9 letters long, we search by
    # multiplying the 9 letter word with all of the 9 and 8 letter words,
    # but we do not need to search the 7 letter words until we have
    # exhausted the 8 letter words against each other. If no 8 letter
    # words in 9x8 letter combinations and 8x8 letter combinations work
    # together, we can check the 9x7, 8x7, and 7x7 letter combinations
    # before checking the 9x6, 8x6, etc.

    # I'm not sure about the efficiency here; it should not be O(n^2) in
    # the average case, since I do not scan the entire collection for
    # each long word.
    for beta_index in range(len(index_list) - 1, 0, -1):
        for beta in range(index_list[beta_index], index_list[beta_index - 1]):
            for alpha in range(0, beta):
                score = combine_words(word_collection[alpha][0], word_collection[beta][0])
                print "%s, %s, %s" % (word_collection[alpha][0], word_collection[beta][0], score)
                if score != 0:
                    break
            
            if score != 0:
                break

        if score != 0:
            break;
