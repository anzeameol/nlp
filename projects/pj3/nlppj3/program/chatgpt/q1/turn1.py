
def count_word_occurrences(file_path, word):
    # 初始化计数器
    count = 0

    # 逐行读取文件
    with open(file_path, 'r') as file:
        for line in file:
            # 将每一行按空格拆分为单词列表
            words = line.strip().split()

            # 遍历单词列表，检查是否与给定单词相同
            for w in words:
                if w == word:
                    count += 1

    return count

file_path = "文本文件的路径"  # 将此替换为实际文本文件的路径
word = "特定单词"  # 将此替换为要搜索的特定单词

occurrences = count_word_occurrences(file_path, word)
print("单词 '{}' 在文件中出现了 {} 次。".format(word, occurrences))
