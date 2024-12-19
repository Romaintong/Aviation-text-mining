import gensim
from gensim import corpora
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import warnings
from gensim.models.coherencemodel import CoherenceModel
from gensim.models.ldamodel import LdaModel
import os

class TopicModelAnalyzer:
    def __init__(self, file_path, event_name, save_dir):
        self.file_path = file_path
        self.event_name = event_name
        self.save_dir = save_dir

    def preprocess_text(self):
        file_object = open(self.file_path, encoding='utf-8', errors='ignore').read().split('\n')
        data_set = []
        for i in range(len(file_object)):
            result = []
            seg_list = file_object[i].split()
            for w in seg_list:
                result.append(w)
            data_set.append(result)
        return data_set

    def calculate_lda(self, corpus, dictionary, num_topics=10):
        return LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=30, random_state=1)

    def perplexity(self, ldamodel, corpus):
        return ldamodel.log_perplexity(corpus)

    def coherence(self, ldamodel, data_set, dictionary):
        ldacm = CoherenceModel(model=ldamodel, texts=data_set, dictionary=dictionary, coherence='c_v')
        return ldacm.get_coherence()

    def plot_coherence_graph(self, x, y):
        plt.plot(x, y)
        plt.xlabel('主题数目')
        plt.ylabel('coherence大小')
        plt.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False
        plt.title('主题-coherence变化情况')
        filename = f'{self.event_name}_coherence趋势图.png'
        save_path = os.path.join(self.save_dir, filename)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()

    def analyze(self):
        data_set = self.preprocess_text()
        dictionary = corpora.Dictionary(data_set)
        corpus = [dictionary.doc2bow(text) for text in data_set]
        num_topics_list = range(1, 15)
        coherence_scores = []

        for num_topics in num_topics_list:
            lda_model = self.calculate_lda(corpus, dictionary, num_topics)
            coherence_score = self.coherence(lda_model, data_set, dictionary)
            coherence_scores.append(coherence_score)

        self.plot_coherence_graph(num_topics_list, coherence_scores)
