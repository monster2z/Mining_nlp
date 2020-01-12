#!/usr/bin/env python
# coding: utf-8

# In[51]:


from konlpy.tag import Komoran
from konlpy.utils import pprint
from collections import Counter
import csv
from matplotlib import pyplot


# In[52]:


def draw_zipf(count_list, filename, color='blue', marker='o'):
    sorted_list = sorted(count_list, reverse=True)
    pyplot.plot(sorted_list, color=color, marker=marker)
    pyplot.xscale('log')
    pyplot.yscale('log')
    pyplot.savefig(filename)


# In[56]:


komoran = Komoran()
doc=''
with open('D:\\work\\nlp\\test.csv','r',encoding='utf-8') as f :
    rdr = csv.reader(f) 
    r = list(rdr)#csv.reader객체를 리스트로

for line in r :
    #print(line)
    doc +="".join(line)+","#line이 각각 list인데, 멤버가 1개 밖에 없어서 join을 어떤형태로 해도 같음.
tagged_word = komoran.nouns(doc)
cnt = Counter(tagged_word) #dictionary 값으로 만들어줌.

print('nchars : ',len(doc))
print('ntokens : ',len(tagged_word))
print(cnt.most_common(100))
#pprint(cnt.most_common(50))
draw_zipf(cnt.values(), 'zipf.png')
print(sorted(cnt.values(),reverse =True))


# In[ ]:




