import jieba
import re

class TextProcessor:
    def __init__(self, stopwords_file='utils/stopwords.txt'):
        self.stopwords_file = stopwords_file
        self.load_stopwords()

    def load_stopwords(self):
        self.stopwords = [line.strip() for line in open(self.stopwords_file, encoding='UTF-8').readlines()]

    def remove_special_characters(self, sentence):
        r = "[A-Za-z0-9_.!+-=——,$%^，。？、~@#￥%……&*《》<>「」{}【】()/]"
        sentence = re.sub(r, ' ', sentence)
        return sentence

    def segment_and_remove_stopwords(self, sentence):
        sentence_depart = jieba.cut(sentence.strip())
        outstr = ''
        for word in sentence_depart:
            if word not in self.stopwords and len(word) > 1:
                if word != '\t':
                    outstr += word
                    outstr += " "
        return outstr.strip()

    def preprocess_data(self, data):
        processed_data = []
        for line in data:
            line = self.remove_special_characters(line)
            line = self.segment_and_remove_stopwords(line)
            processed_data.append(line)
        return processed_data