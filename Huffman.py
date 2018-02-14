#!/usr/bin/env python3
# -*-coding:utf-8-*-
import heapq
import json

class HuffmanTree:
    def __init__(self, key=None, value=0):
        self.value = value
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key) + ' ' + str(self.value)

    def __cmp__(self, s):
        if self.value < s.value:
            return -1
        if self.value > s.value:
            return 1
        return 0

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value


def Tree(line):
    h = {}
    for i in range(0,len(line)):
        if not line[i] in h:
            h[line[i]] = 1
        else:
            h[line[i]] += 1

    arr = []
    for k, v in h.items():
        heapq.heappush(arr, HuffmanTree(k, v))

    while len(arr) != 1:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        p = HuffmanTree(value=a.value + b.value)
        p.left = a
        p.right = b
        heapq.heappush(arr, p)
    return heapq.heappop(arr)

def build_Dict(tree,s,d):
    if tree.key is not None:
        d[tree.key]=s
    else:
        build_Dict(tree.left,s+'0',d)
        build_Dict(tree.right,s+'1',d)

def compress(line,d):
    s=''
    for i in range(0,len(line)):
        s+=d[line[i]]

    return s

def decompress(line,dic):
    d={}
    for key,value in dic.items():
        d[value]=key
    front=0
    end=0
    res=''
    while end<=len(line):
        s = line[front:end]
        if s in d:
            res+=d[s]
            front=end
        end+=1
    return res

