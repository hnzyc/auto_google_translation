import pyperclip
import time
import nltk
#nltk.download()
#from nltk.corpus import wordnet
from nltk.corpus import words as words_range

def alterfile(file):
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip()
            words=line.rsplit(' ',1)
            lastword=words[-1].lower()
            #if wordnet.synsets(words[-1]):    #a the that 返回 []
            if (lastword in words_range.words() or lastword.rstrip('s') in words_range.words() or lastword.rstrip('es') in words_range.words()):  #复数形式不在其中...
                line = line+" "    #分词衔接
            else:
                pass                     #断词衔接
                print(lastword)

            file_data += line    #逐行写入缓存

    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)    #缓存写入文件

def altercopy():
    tempBuff=''    #仅仅用于暂存判定
    while True:
        time.sleep(3)
        pasteText=pyperclip.paste()
        if tempBuff != pasteText:
            tempBuff=pasteText

            #改进之一 完善一下断词的处理
            #strBuff = strBuff.replace('\r\n', ' ')    #过于简单,如果是断词就出现词间空格
            strBuff=tempBuff
            while strBuff.find('\r\n') != -1:
                lines=strBuff.split('\r\n',1)
                line=lines[0]
                words=line.rsplit(' ',1)
                lastword=words[-1].lower()

                #if not wordnet.synsets(lastword):    a the that return []
                if (lastword in words_range.words() or lastword.rstrip('s') in words_range.words() or lastword.rstrip('es') in words_range.words()):  #复数形式不在其中...
                    #strBuff.replace('\r\n', ' ',1)    #死循环
                    strBuff = strBuff.replace('\r\n', ' ',1)    #正常换行
                else :
                    print(lastword)
                    #strBuff.replace('\r\n', '',1)    #死循环
                    strBuff = strBuff.replace('\r\n', '',1)    #断词换行

            pyperclip.copy(strBuff)
            tempBuff=strBuff    #避免循环

# byt="hello good"
# words=byt.rsplit(' ',1)
# print(words[-1])
# list=wordnet.synsets(words[-1])
# print(list)

# te="would" in words_range.words()
# print(te)

#alterfile("readme")
altercopy()
