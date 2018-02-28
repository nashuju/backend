# -*- coding: utf-8 -*-
import codecs

def create_dictionary(file):
    for line in file:
        list = line.split()
        for word in list:
            node = dictionary.get(word)
            if node is None:
                dictionary[word] = []
    print(dictionary)
    for line in file:
        list = line.split()
        first = list[0]
        for word in list[1:]:
            dictionary[first].append(word)
            first = word
    print(dictionary)

def max_match(sam):
    result = [0]
    words = sam.split()
    next = dictionary[words[0]]
    for word in words[1:]:
        if dictionary.__contains__(word) == False:
            result.append(-1)
            continue
        if word in next:
            result.append(1)
        else:
            result.append(0)
        next = dictionary[word]
    match = []
    i = 0
    while i<len(result):
        new_match = []
        new_match.append(words[i])
        if result[i] == -1:
            match.append(new_match)
            i += 1
            continue
        if result[i] == 0:
            i += 1
            while i < len(result) and result[i]==1:
                new_match.append(words[i])
                i += 1
            match.append(new_match)
    print("match:%s"%match)
    return match

def format_result(match):
    format_res = ''
    for i in match:
        format_res = format_res + (' [' + ' '.join(i) + '] ')
    return format_res

txt = codecs.open('test.txt','r','utf-8_sig')
dictionary = {}
file = txt.readlines()
create_dictionary(file)
txt.close()
sample = ['小明 是 复旦 大学 的 学生', '他 今年 是 大学 的 学生 了']
for sam in sample:
    print("输入：" + sam)
    print("输出：" + format_result(max_match(sam)))

