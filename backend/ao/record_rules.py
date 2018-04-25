# -*- coding: utf-8 -*-
import re
class RecordRules:

    seq = u""
    def __init__(self,seq):
        self.seq = str(seq).decode('utf-8')

    # hello(你好)
    def en_zh(self):
        if self.seq.find('(')!=-1 and self.seq.find(')')!=-1 and self.seq.index('(')<self.seq.index(')'):
            word = self.seq[:self.seq.index('(')]
            content = " "+self.seq[self.seq.index('(')+1:self.seq.index(')')]
            return word,content
        else:
            return self.seq , ""
