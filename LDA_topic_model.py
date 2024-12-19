from gensim.models import LdaModel
from gensim import corpora
import pyLDAvis.gensim

class LDATopicModelHTML:
    def __init__(self, text_list, html_name):
        self.text_list = text_list
        self.html_name = html_name
        self.dictionary, self.corpus = self.preprocess_text_and_create_corpus(self.text_list)
        
    def preprocess_text_and_create_corpus(self, text_list):
        # 分割字符串为标记
        tokenized_list = [text.split() for text in text_list]
        # 创建词典
        dictionary = corpora.Dictionary(tokenized_list)
        # 将标记化的文本转换为文档-词袋表示
        corpus = [dictionary.doc2bow(tokens) for tokens in tokenized_list]
        return dictionary, corpus
    
    def generate_lda_html(self, num_topics=10, passes=30):
        lda = LdaModel(corpus=self.corpus, id2word=self.dictionary, num_topics=num_topics, passes=passes, random_state=1)
        
        # pyLDAvis.enable_notebook()
        data = pyLDAvis.gensim.prepare(lda, self.corpus, self.dictionary)
        
        # 保存HTML文件
        html_path = f'../figure/主题模型/{self.html_name}.html'
        pyLDAvis.save_html(data, html_path)
        
        return html_path