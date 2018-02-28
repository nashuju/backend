# -*- coding: utf-8 -*-
Word_Map = {}
corpus = ['小明 今年 二十 岁', '复旦 大学 的 学生 参加 了 歌唱 表演', '他 是 交通 大学 的 老师']
def init_Word_Map(corpus):
    for l in corpus:
        word_array = l.replace("\n", "").split(" ")
        for w in word_array:
            node = Word_Map.get(w)
            if node is None:
                Word_Map[w] = []

def create_Corpus(corpus):
    for l in corpus:
        word_array = l.replace("\n", "").split(" ")
        pre = word_array[0]
        for w in word_array[1:]:
            Word_Map[pre].append(w)
            pre = w

init_Word_Map(corpus)
create_Corpus(corpus)
print(Word_Map)

def max_Match(sentence):
    result = [0]
    wd = sentence.split()
    next_word = Word_Map[wd[0]]
    for w in wd[1:]:
        if Word_Map.__contains__(w) == False:
            result.append(-1)
            continue
        if w in next_word:
            result.append(1)
        else:
            result.append(0)
        next_word = Word_Map[w]
    matchs = []
    i = 0
    while i<len(result):
        new_match = []
        new_match.append(wd[i])
        if result[i] == -1:
            matchs.append(new_match)
            i += 1
            continue
        if result[i] == 0:
            i += 1
            while i < len(result) and result[i]==1:
                new_match.append(wd[i])
                i += 1
            matchs.append(new_match)
    return matchs

def show_Res(match):
    res = ''
    for i in match:
        res = res + (' [' + ' '.join(i) + '] ')
    return res

sentence = ['小明 是 复旦 大学 的 学生', '他 今年 是 大学 的 学生 了']
for sen in sentence:
    print("输入：" + sen)
    print("输出：" + show_Res(max_Match(sen)))



