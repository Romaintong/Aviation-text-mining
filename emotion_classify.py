import jieba
import pandas as pd

class EmotionAnalyzer:
    def __init__(self, emotion_dict_file):
        self.Happy = []
        self.Good = []
        self.Surprise = []
        self.Anger = []
        self.Sad = []
        self.Fear = []
        self.Disgust = []
        self.load_emotion_data(emotion_dict_file)
        
    def load_emotion_data(self, emotion_dict_data):
        for _, row in emotion_dict_data.iterrows():
            if row['情感分类'] in ['PA', 'PE']:
                self.Happy.append(row['词语'])
            if row['情感分类'] in ['PD', 'PH', 'PG', 'PB', 'PK']:
                self.Good.append(row['词语']) 
            if row['情感分类'] in ['PC']:
                self.Surprise.append(row['词语'])     
            if row['情感分类'] in ['NA']:
                self.Anger.append(row['词语'])    
            if row['情感分类'] in ['NB', 'NJ', 'NH', 'PF']:
                self.Sad.append(row['词语'])
            if row['情感分类'] in ['NI', 'NC', 'NG']:
                self.Fear.append(row['词语'])
            if row['情感分类'] in ['NE', 'ND', 'NN', 'NK', 'NL']:
                self.Disgust.append(row['词语'])
        
        self.Positive = self.Happy + self.Good + self.Surprise
        self.Negative = self.Anger + self.Sad + self.Fear + self.Disgust
        
    def emotion_calculate(self, text):
        wordlist = jieba.lcut(text)
        wordset = set(wordlist)

        emotion_counts = {
            'positive': sum(wordlist.count(word) for word in wordset if word in self.Positive),
            'negative': sum(wordlist.count(word) for word in wordset if word in self.Negative),
            'anger': sum(wordlist.count(word) for word in wordset if word in self.Anger),
            'disgust': sum(wordlist.count(word) for word in wordset if word in self.Disgust),
            'fear': sum(wordlist.count(word) for word in wordset if word in self.Fear),
            'good': sum(wordlist.count(word) for word in wordset if word in self.Good),
            'sadness': sum(wordlist.count(word) for word in wordset if word in self.Sad),
            'surprise': sum(wordlist.count(word) for word in wordset if word in self.Surprise),
            'happy': sum(wordlist.count(word) for word in wordset if word in self.Happy),
        }

        emotion_info = {
            'length': len(wordlist),
            **emotion_counts
        }
        indexs = ['length', 'positive', 'negative', 'anger', 'disgust', 'fear', 'sadness', 'surprise', 'good', 'happy']
        return pd.Series(emotion_info, index=indexs)
    
    def analyze_data(self, data):
        result_data = []
        for sentence in data:
            emotions = self.emotion_calculate(sentence)
            result_data.append(emotions)
        return pd.DataFrame(result_data)