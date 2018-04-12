#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import string
import huffman
import collections

abs = string.ascii_lowercase

def readText():
    plainText = ''
    with open('strText', 'r') as f:
        for line in f:
            plainText += line
    return plainText

def charsRepeatReduce():
    return "".join(set(readText()))

def charsRepeatCount():
    plainText = readText()
    return {i: plainText.count(i) for i in sorted(set(plainText))}

print(dict(collections.Counter(readText()).most_common()))
print(dict(collections.Counter(readText()).most_common()[::-1]))

print("\"{}\" equals to: {}".format(charsRepeatReduce(),len(charsRepeatReduce())))
print(charsRepeatCount())

dictionaryHuffman = huffman.codebook(collections.Counter(readText()).items())
print(dictionaryHuffman)

hufm = 0
for c in charsRepeatReduce():
    hufm += len(dictionaryHuffman[c]) * charsRepeatCount()[c]
print("for huffmans: {}".format(hufm))

sum2 = 0
for c in charsRepeatReduce():
    sum2 += charsRepeatCount()[c]
norm = sum2 * 8
print("for normal: {}".format(norm))

print("compression: ~{}x".format(round(norm / hufm, 2)))
