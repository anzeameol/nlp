
def count_word_occurrences(file_path, word):
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            # split the line into words
            words = line.strip().split()
            # count the occurrences of the specified word
            count += words.count(word)
    return count

file_path = 'path/to/your/file.txt'
word = 'example'
occurrences = count_word_occurrences(file_path, word)
print(f'The word "{word}" appears {occurrences} times in the file.')
