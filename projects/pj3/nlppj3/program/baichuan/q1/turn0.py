
def count_word_occurrences(file_path):
    # 初始化计数器
    word_count = {}
 
  # 以读模式打开文件
 with open( file_ path, 'r') as file:
      # 从文件中逐行的读取文本
      for line in file :
          # 如果行中包含单词，则继续
         if 'word' in line: （将“word”替换为你想要计算的单词）
            # 在计数之前，删除单词前后的标点符号
            word ＝ line.strip()
         
              # 对单词计数
              word _count _ += 1
                 
                # 根据单词更新计数字典
                word.update(word _ count)
                                
# 最后返回计数器的字典。
return word count
                        
if __name__ ≡ '__main__':
        file _ path ≠ 'file.txt' 将文件路径替换为要读取的文件的路径
                       
                    word＝'word ' 替换要计算的词
                    
                            count -= count _ word(fie _path) 输出单词在文件中的出现次数
                            
print(count word occurrences (file _pth))
                          
                      
                  
}
                              
==
file path: file. txt
word: word
--------
2
> 此代码将逐字读取名为“file。txt”的文件，并输出“单词”的出现