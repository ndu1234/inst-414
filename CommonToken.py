#!/usr/bin/env python
# coding: utf-8

# # NLTK

# In[19]:


import pandas as pd 
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer
from nltk.probability import FreqDist
import string

def freq(text, top):
    words = text.split()  # Split the text into words
    freq_dist = FreqDist(words)
    return freq_dist.most_common(top)

def main():
    filepath = "test01.txt"
    top = 10
    with open(filepath, "r", encoding='utf-8') as file:
        text = file.read()
    top_words = freq(text, top)
    
    print("Top 10 most common words and their counts:")
    for word, count in top_words:
        print(f"{word}: {count}")

if __name__ == '__main__':
    main()


# # A different approach 

# In[29]:


import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
nltk.download('punkt')
from nltk.probability import FreqDist
text = """Creative Commons Deed
This is a human-readable summary of the full license.
You are free:

to Share - to copy, distribute and transmit the work, and
to Remix - to adapt the work
for any purpose, even commercially.

Under the following conditions:

Attribution - You must attribute the work in the manner specified by the author or licensor (but not in any way that suggests that they endorse you or your use of the work.)
Share Alike - If you alter, transform, or build upon this work, you may distribute the resulting work only under the same, similar or a compatible license.
With the understanding that:

Waiver - Any of the above conditions can be waived if you get permission from the copyright holder.
Other Rights - In no way are any of the following rights affected by the license:
your fair dealing or fair use rights;
the author's moral rights; and
rights other persons may have either in the work itself or in how the work is used, such as publicity or privacy rights.
Notice - For any reuse or distribution, you must make clear to others the license terms of this work. The best way to do that is with a link to https://creativecommons.org/licenses/by-sa/3.0/"""

word = word_tokenize(text)

fd = FreqDist(word)
print("Top 10 most common words and their counts")
for words, count in fd.most_common(10):
    print(f"{words}:{count}")


# In[30]:


import pandas as pd 
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer
from nltk.probability import FreqDist
import string

def freq(text, top):
    words = text.split()  # Split the text into words
    freq_dist = FreqDist(words)
    return freq_dist.most_common(top)

def main():
    filepath = "test02.txt"
    top = 10
    with open(filepath, "r", encoding='utf-8') as file:
        text = file.read()
    top_words = freq(text, top)
    
    print("Top 10 most common words and their counts:")
    for word, count in top_words:
        print(f"{word}: {count}")

if __name__ == '__main__':
    main()


# In[ ]:




