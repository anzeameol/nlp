
def count_word_occurrences(file_path, word):
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            count += line.lower().split().count(word.lower())

    return count

file_path = 'your_file_path.txt'
word = 'your_word'

occurrences = count_word_occurrences(file_path, word)
print(f'The word "{word}" occurs {occurrences} times in the file.')
