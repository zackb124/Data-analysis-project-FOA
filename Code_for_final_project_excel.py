#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import io
#Dependencies
import gensim #the library for Topic modelling
from gensim.models.ldamulticore import LdaMulticore
from gensim import corpora, models

from nltk.corpus import stopwords
import string
from nltk.stem.wordnet import WordNetLemmatizer

import warnings
warnings.simplefilter('ignore')
from itertools import chain


df=pd.read_excel('Example for data base.xlsx')


# In[2]:


df=df.replace({'Category' : { 'Y' : "Antisemitic", 'W' : "Non-Antisemitic", 'U' : "Anti-Zionist" }})
df


# In[3]:


df = df.replace(r'\n',' ', regex=True) 

post_description=df["A short summary of the content- write briefly in your own words"]


# In[7]:
df


# In[5]:


from nltk import ngrams


# In[6]:


post_description.value_counts()


# In[ ]:


from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist


# In[ ]:


tokenized_word=word_tokenize(post_description)

fdist = FreqDist(tokenized_word)

print(fdist(head=10))


# In[ ]:




