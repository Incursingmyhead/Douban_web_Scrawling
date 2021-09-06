#!/usr/bin/env python
# coding: utf-8

# In[35]:


import requests 
import bs4
def connect_to_url(url):
    
    hd = {

        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    try:
        resp = requests.get(url, headers= hd)
    except:
        print("Can not get the url.")
    #print(resp.status_code)
    #print(resp.text)
    return resp


# In[36]:


def make_soup(resp):
    soup = bs4.BeautifulSoup(resp.text)
    print(type(soup))
    return soup 
def get_onepage_reviewlist(soup):
    item = soup.findAll('div', attrs = {"class":"review-list"})
    review_list = []
    for link in item[0]:
        if (type(link)) is bs4.element.Tag:
            a = link.find('h2')
            if a:
                a = a.find('a')
                review_list.append(a.get('href'))
                
                
    return review_list


# In[37]:


url = "https://movie.douban.com/subject/1959877/"+"reviews"
resp = connect_to_url(url)
soup = make_soup(resp)
review_l = get_onepage_reviewlist(soup)
print(review_l)


# In[41]:


def get_content(url):
    hd = {

        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    try:
        resp = requests.get(url, headers = hd)
    except:
        #print("here")
        return ""
    soup = bs4.BeautifulSoup(resp.text)
    item = soup.find('div', attrs = {'class':'review-content clearfix'})
    if not item:
        #print("here")
        return ""
    #print("here")
    #print(len(item))
    return item.text


    


# In[45]:


def get_content_list(review_l):
    content_list = []
    #print(review_l)
    for url in review_l:
        content_list.append(get_content(url))
    print(content_list[0])
    return content_list


# In[46]:


pip install jieba


# In[47]:


import jieba


# In[48]:


def process_review(content):
    seglist = list(jieba.cut(content))
    
    return seglist
review = []
for content in content_list:
    
    review.extend(process_review(content))
print(len(review))

    


# In[50]:


from collections import Counter
words_count = Counter(review)
print(len(words_count))


# In[51]:


d = dict()
for k in words_count:
    if len(k) > 3:
        d[k] = words_count[k]
        
print(len(d))


# In[55]:


pip install wordcloud


# In[59]:


#pip install wordcloud
import wordcloud
import matplotlib.pyplot as plt
wc = wordcloud.WordCloud(font_path = "style.ttf")
wc.fit_words(d)
plt.figure()
plt.imshow(wc)


# In[ ]:




