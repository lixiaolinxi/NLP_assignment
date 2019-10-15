#!/usr/bin/env python
# coding: utf-8

# ## Lesson-01 Assignment

# #### 今天是2019年9月28日，今天世界上又多了一名AI工程师 :) 

# `各位同学大家好，欢迎各位开始学习我们的人工智能课程。这门课程假设大家不具备机器学习和人工智能的知识，但是希望大家具备初级的Python编程能力。根据往期同学的实际反馈，我们课程的完结之后 能力能够超过80%的计算机人工智能/深度学习方向的硕士生的能力。`

# ## 本次作业的内容

# #### 1. 复现课堂代码
# 
# 在本部分，你需要参照我们给大家的GitHub地址里边的课堂代码，结合课堂内容，复现内容。

# #### 2. 请回答以下问题
# 
# 回答以下问题，并将问题发送至 minchiuan.gao@gmail.com 中：
# ```
#     2.1. what do you want to acquire in this course？
#     2.2. what problems do you want to solve？
#     2.3. what’s the advantages you have to finish you goal?
#     2.4. what’s the disadvantages you need to overcome to finish you goal?
#     2.5. How will you plan to study in this course period?
# ```

# #### 3. 如何提交
# 代码 + 此 jupyter 相关，提交至自己的 github 中(**所以请务必把GitHub按照班主任要求录入在Trello中**)；
# 第2问，请提交至minchiuan.gao@gmail.com邮箱。
# #### 4. 作业截止时间
# 此次作业截止时间为 2019.10.8日

# #### 5. 完成以下问答和编程练习

# >

# ## 基础理论部分

# > **评阅点**：每道题是否回答完整

# #### 0. Can you come up out 3 sceneraies which use AI methods? 

# Ans: {海底捞电话客服；支付宝自动客服机器人；支付宝刷脸支付}

# #### 1. How do we use Github; Why do we use Jupyter and Pycharm;

# Ans: 1.Github,注册github账号，创建repository,上传自己的code文件. 
#   2.使用Jupyter方便展示每一步代码的运行结果，Jupyter也可以智能提示代码的错误

# #### 2. What's the Probability Model?

# Ans:

# #### 3. Can you came up with some sceneraies at which we could use Probability Model?

# Ans:

# #### 4. Why do we use probability and what's the difficult points for programming based on parsing and pattern match?

# Ans:

# #### 5. What's the Language Model;

# Ans:一个句子出现的概率

# #### 6. Can you came up with some sceneraies at which we could use Language Model?
# 

# Ans:

# #### 7. What's the 1-gram language model;

# Ans:

# #### 8. What's the disadvantages and advantages of 1-gram language model;

# Ans:

# #### 9. What't the 2-gram models;

# Ans:

# ## 编程实践部分

# #### 1. 设计你自己的句子生成器

# 如何生成句子是一个很经典的问题，从1940s开始，图灵提出机器智能的时候，就使用的是人类能不能流畅和计算机进行对话。和计算机对话的一个前提是，计算机能够生成语言。
# 
# 计算机如何能生成语言是一个经典但是又很复杂的问题。 我们课程上为大家介绍的是一种基于规则（Rule Based）的生成方法。该方法虽然提出的时间早，但是现在依然在很多地方能够大显身手。值得说明的是，现在很多很实用的算法，都是很久之前提出的，例如，二分查找提出与1940s, Dijstra算法提出于1960s 等等。

# 在著名的电视剧，电影《西部世界》中，这些机器人们语言生成的方法就是使用的SyntaxTree生成语言的方法。
# 
# > 
# >
# 
# ![WstWorld](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1569578233461&di=4adfa7597fb380e7cc0e67190bbd7605&imgtype=0&src=http%3A%2F%2Fs1.sinaimg.cn%2Flarge%2F006eYYfyzy76cmpG3Yb1f)
# 
# > 
# >

# 在这一部分，需要各位同学首先定义自己的语言。 大家可以先想一个应用场景，然后在这个场景下，定义语法。例如：
# 
# 在西部世界里，一个”人类“的语言可以定义为：
# ``` 
# human = """
# human = 自己 寻找 活动
# 自己 = 我 | 俺 | 我们 
# 寻找 = 看看 | 找找 | 想找点
# 活动 = 乐子 | 玩的
# """
# ```
# 
# 一个“接待员”的语言可以定义为
# ```
# host = """
# host = 寒暄 报数 询问 业务相关 结尾 
# 报数 = 我是 数字 号 ,
# 数字 = 单个数字 | 数字 单个数字 
# 单个数字 = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
# 寒暄 = 称谓 打招呼 | 打招呼
# 称谓 = 人称 ,
# 人称 = 先生 | 女士 | 小朋友
# 打招呼 = 你好 | 您好 
# 询问 = 请问你要 | 您需要
# 业务相关 = 玩玩 具体业务
# 玩玩 = 耍一耍 | 玩一玩
# 具体业务 = 喝酒 | 打牌 | 打猎 | 赌博
# 结尾 = 吗？"""
# 
# ```
# 
# 
# 

# 请定义你自己的语法: 

# 第一个语法：

# In[10]:


沙僧 = """
沙僧 = 惊叹 称谓 某人 介词 妖怪 动作
惊叹 = 不好了！｜出事了！｜完蛋了！
称谓 = 大师兄|菩萨 
某人 = 师傅｜二师兄|八戒
介词 = 被｜让
妖怪 = 白骨精｜金角大王｜牛魔王
动作 = 抓走了！｜蒸吃了！"""


# > **评阅点**： 是否提出了和课程上区别较大的语法结构

# 第二个语法：

# In[ ]:


you_need_replace_this_with_name_you_given = '''
# you code here
'''


# > **评阅点**：是否和上一个语法区别比较大

# TODO: 然后，使用自己之前定义的generate函数，使用此函数生成句子。

# TODO: 然后，定义一个函数，generate_n，将generate扩展，使其能够生成n个句子:

# ## <font color=red> 个人作答：

# ## <font color=red>可以生成句子了,haha，没时间了，就先做了一个

# In[97]:


沙僧_rules = """
沙僧_say = 称谓 惊叹 某人 介词 妖怪 动作
惊叹 = 不好了！| 出事了！| 完蛋了！
称谓 = 大师兄, | 菩萨, 
某人 = 师傅 | 二师兄 | 八戒
介词 = 被 | 让
妖怪 = 白骨精 | 金角大王 | 牛魔王
动作 = 抓走了！ | 蒸吃了！"""


# In[98]:


import random


# In[99]:


def get_generation_by_gram(grammar_str: str, target, stmt_split='=', or_split='|'):
    
    rules = dict()# key is the @statement, value is @expression

    for line in 沙僧_rules.split('\n'):
        if not line: continue
        # skip the empty line
        stmt, expr = line.split(stmt_split)
    
        rules[stmt.strip()] = expr.split(or_split)
    
    generated = generate(rules, target=target)
    
    return generated


# In[100]:


def generate(grammar_rule, target):
    if target in grammar_rule: #names
        candidates = grammar_rule[target] #['name names', 'name']
        candidate = random.choice(candidates)#'name names', 'name'
        return ' '.join(generate(grammar_rule, target=c.strip()) for c in candidate.split())
    else:
        return target


# In[93]:


get_generation_by_gram(沙僧_rules, target='沙僧_say')


# In[10]:


def generate_n():
    # you code here 
    pass


# > **评阅点**; 运行代码，观察是否能够生成多个句子

# #### 2. 使用新数据源完成语言模型的训练

# 按照我们上文中定义的`prob_2`函数，我们更换一个文本数据源，获得新的Language Model:
# 
# 1. 下载文本数据集（你可以在以下数据集中任选一个，也可以两个都使用）
#     + 可选数据集1，保险行业问询对话集： https://github.com/Computing-Intelligence/insuranceqa-corpus-zh/raw/release/corpus/pool/train.txt.gz
#     + 可选数据集2：豆瓣评论数据集：https://github.com/Computing-Intelligence/datasource/raw/master/movie_comments.csv
# 2. 修改代码，获得新的**2-gram**语言模型
#     + 进行文本清洗，获得所有的纯文本
#     + 将这些文本进行切词
#     + 送入之前定义的语言模型中，判断文本的合理程度

# ## <font color=red> 个人作答：

# In[96]:


corpus = '/users/li/Downloads/train.txt'


# In[103]:


FILE = open(corpus).read()


# In[108]:


FILE[:100]


# In[110]:


len(FILE)


# In[114]:


import jieba


# In[115]:


def cut(string):
    return list(jieba.cut(string))


# In[116]:


TOKENS = cut(FILE)


# In[117]:


len(TOKENS)


# In[118]:


from collections import Counter


# In[119]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[120]:


words_count = Counter(TOKENS)


# In[125]:


words_with_fre = [f for w, f in words_count.most_common()]


# In[126]:


import matplotlib.pyplot as plt


# In[127]:


words_count.most_common(10)


# In[128]:


import numpy as np


# In[129]:


plt.plot(np.log(np.log(words_with_fre)))


# In[130]:


_2_gram_words =[
    TOKENS[i] + TOKENS[i+1] for i in range(len(TOKENS)-1)
]


# In[131]:


_2_gram_words[:10]


# In[132]:


_2_gram_word_counts = Counter(_2_gram_words)


# In[133]:


words_count.most_common()[-1][-1]


# In[134]:


def get_1_gram_count(word):
    if word in words_count: return words_count[word]
    else:
        return words_count.most_common()[-1][-1]


# In[135]:


def get_2_gram_count(word):
    if word in words_count: return words_count[word]
    else:
        return words_count.most_common()[-1][-1]


# In[136]:


def get_gram_count(word, wc):
    if word in wc: return wc[word]
    else:
        return wc.most_common()[-1][-1]


# In[137]:


get_gram_count('XXX',words_count)


# In[138]:


def two_gram_model(sentence):
    # 2-gram language model
    tokens = cut(sentence)
    
    probability = 1
    
    for i in range(len(tokens)-1):
        word = tokens[i]
        next_word = tokens[i+1]
        
        _two_gram_c = get_gram_count(word+next_word, _2_gram_word_counts)
        _one_gram_c = get_gram_count(next_word, words_count)
        pro = _two_gram_c / _one_gram_c
        
        probability *= pro
    
    return probability


# In[140]:


two_gram_model('你需要买保险吗')


# > **评阅点** 1. 是否使用了新的数据集； 2. csv(txt)数据是否正确解析

# #### 3. 获得最优质的的语言

# 当我们能够生成随机的语言并且能判断之后，我们就可以生成更加合理的语言了。请定义 generate_best 函数，该函数输入一个语法 + 语言模型，能够生成**n**个句子，并能选择一个最合理的句子: 
# 
# 

# 提示，要实现这个函数，你需要Python的sorted函数

# In[141]:


sorted([1, 3, 5, 2])


# 这个函数接受一个参数key，这个参数接受一个函数作为输入，例如

# In[142]:


sorted([(2, 5), (1, 4), (5, 0), (4, 4)], key=lambda x: x[0])


# 能够让list按照第0个元素进行排序.

# In[143]:


sorted([(2, 5), (1, 4), (5, 0), (4, 4)], key=lambda x: x[1])


# 能够让list按照第1个元素进行排序.

# In[144]:


sorted([(2, 5), (1, 4), (5, 0), (4, 4)], key=lambda x: x[1], reverse=True)


# 能够让list按照第1个元素进行排序, 但是是递减的顺序。

# >

# In[145]:


def generate_best(): # you code here
    pass


# 好了，现在我们实现了自己的第一个AI模型，这个模型能够生成比较接近于人类的语言。

# > **评阅点**： 是否使用 lambda 语法进行排序

# Q: 这个模型有什么问题？ 你准备如何提升？ 

# Ans:

# >**评阅点**: 是否提出了比较实际的问题，例如OOV问题，例如数据量，例如变成 3-gram问题。

# ##### 以下内容为可选部分，对于绝大多数同学，能完成以上的项目已经很优秀了，下边的内容如果你还有精力可以试试，但不是必须的。

# #### 4. (Optional) 完成基于Pattern Match的语句问答
# > 我们的GitHub仓库中，有一个assignment-01-optional-pattern-match，这个难度较大，感兴趣的同学可以挑战一下。

# 
# #### 5. (Optional) 完成阿兰图灵机器智能原始论文的阅读
# 1. 请阅读阿兰图灵关于机器智能的原始论文：https://github.com/Computing-Intelligence/References/blob/master/AI%20%26%20Machine%20Learning/Computer%20Machinery%20and%20Intelligence.pdf 
# 2. 并按照GitHub仓库中的论文阅读模板，填写完毕后发送给我: mqgao@kaikeba.com 谢谢

# > 

# 各位同学，我们已经完成了自己的第一个AI模型，大家对人工智能可能已经有了一些感觉，人工智能的核心就是，我们如何设计一个模型、程序，在外部的输入变化的时候，我们的程序不变，依然能够解决问题。人工智能是一个很大的领域，目前大家所熟知的深度学习只是其中一小部分，之后也肯定会有更多的方法提出来，但是大家知道人工智能的目标，就知道了之后进步的方向。

# 然后，希望大家对AI不要有恐惧感，这个并不难，大家加油！

# >

# ![](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1561828422005&di=48d19c16afb6acc9180183a6116088ac&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201807%2F28%2F20180728150843_BECNF.thumb.224_0.jpeg)
