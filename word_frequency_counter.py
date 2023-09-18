import string

def word_frequency(sentence):
    # Eliminate punctuation and split the sentence into individual words
    translator = str.maketrans('', '', string.punctuation)
    words = sentence.translate(translator).split()

    # Establish a dictionary to record word frequencies
    word_freq = {}

    # Tally the occurrence of each word while disregarding letter case
    for word in words:
        word = word.lower()
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq

# Test case 1
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
# Expected Output: {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'sentence': 2}
