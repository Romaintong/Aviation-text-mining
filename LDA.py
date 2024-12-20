import gensim
from gensim import corpora
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import warnings
import os
warnings.filterwarnings('ignore')  # To ignore all warnings that arise here to enhance clarity
from gensim.models.coherencemodel import CoherenceModel
from gensim.models.ldamodel import LdaModel

PATH = "../output/3种航空事件数据集的文本处理和情感计算/processed_3U8633_related_content.csv"

file_object2 = open(PATH, encoding='utf-8', errors='ignore').read().split('\n')  # 一行行的读取内容
data_set = []  # 建立存储分词的列表
for i in range(len(file_object2)):
    result = []
    seg_list = file_object2[i].split()
    for w in seg_list:  # 读取每一行分词
        result.append(w)
    data_set.append(result)
print(data_set)

dictionary = corpora.Dictionary(data_set)  # 构建词典
corpus = [dictionary.doc2bow(text) for text in data_set]  #表示为第几个单词出现了几次

ldamodel = LdaModel(corpus, num_topics=10, id2word = dictionary, passes=30,random_state = 1)   #分为10个主题
print(ldamodel.print_topics(num_topics=10, num_words=15))  #每个主题输出15个单词

#计算困惑度
def perplexity(num_topics):
    ldamodel = LdaModel(corpus, num_topics=num_topics, id2word = dictionary, passes=30)
    print(ldamodel.print_topics(num_topics=num_topics, num_words=6))
    print(ldamodel.log_perplexity(corpus))
    return ldamodel.log_perplexity(corpus)

#计算coherence
def coherence(num_topics):
    ldamodel = LdaModel(corpus, num_topics=num_topics, id2word = dictionary, passes=30,random_state = 1)
    print(ldamodel.print_topics(num_topics=num_topics, num_words=6))
    ldacm = CoherenceModel(model=ldamodel, texts=data_set, dictionary=dictionary, coherence='c_v')
    print(ldacm.get_coherence())
    return ldacm.get_coherence()

if __name__ == '__main__':
    x = range(1,15)
    # z = [perplexity(i) for i in x]  #如果想用困惑度就选这个
    y = [coherence(i) for i in x]
    plt.plot(x, y)
    plt.xlabel('主题数目')
    plt.ylabel('coherence大小')
    plt.rcParams['font.sans-serif']=['SimHei']
    matplotlib.rcParams['axes.unicode_minus']=False
    plt.title('主题-coherence变化情况')
    # 保存分布图
    filename = '3U8633困惑度计算.png'
    save_path = os.path.join('../figure/主题数选择/', filename)
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()