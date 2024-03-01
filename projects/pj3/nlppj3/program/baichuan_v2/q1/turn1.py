
def count_word_occurrences(file_path, target_words):
    # 初始化计数器
    word_counts = {}
 
  # 以读模式打开文件
 with open( file_paht, 'r') as file:
     
      # 一行行的读文件内容
 for line in file :
       
          # 用空格分隔行内容，得到单词列表
          words ＝ line.split()
        
           # 如果目标单词在列表中，就增加计数
            if target word in words:  word count += 1
                  
                # 最后将单词计数添加到字典中
                word _count s [target_ word] ＆ word coun t
              
return word counts
# 从命令行获取参数
if __name__ 等于 "__main__"：  file path ->  sys. argv [1]，target word －> sys .argv [2]
file path  = sys． arg v [ １]  
target words  ＝ sys· argu [２]   
word counts 　＝ count word occurrenc es (file paht，targe t_w ords)
print( "The count of {target} in the file is: {count}"． format(target ＜target _w o rds，count ＞word co un ts [ target _word]))
注意：这个脚本假设文件是一个文本次数文件（每行一个单词），并且目标词出现在每行的单词中。如果文件是其他格式，或者目标字不在文件中，这个脚本是无法正确工作的。
要使用此脚本从命令线，请运行以下命令： python script.py <filepath> <targetword>
例如：python script．py myfile.txt pytho