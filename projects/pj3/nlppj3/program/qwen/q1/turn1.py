
def count_word_in_file(file_path, word):
    word_count = 0

    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().split()
            word_count += words.count(word)

    return word_count


# 使用方法：
file_path = 'path_to_your_text_file.txt'  # 替换为你的文本文件路径
word = 'example'  # 替换为你想要计数的单词
print(count_word_in_file(file_path, word))
