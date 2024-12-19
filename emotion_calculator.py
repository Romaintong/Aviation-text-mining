import jieba
import pandas as pd

class EmotionCalculator:
    def __init__(self, emotion_dict_file):
        self.word_data = {}
        self.load_emotion_data(emotion_dict_file)

    def load_emotion_data(self, emotion_dict_file):
        for _, row in emotion_dict_file.iterrows():
            word = row["词语"]
            info = {
                "情感分类_大类": row["情感分类_大类"],
                "强度": row["强度"]
            }
            self.word_data[word] = info

    def calculate_emotion_intensity(self, data, emotion_type):
        total_intensitys = []
        for row in data:
            total_intensity = 0
            wordlist = jieba.lcut(row)
            for word in wordlist:
                word_info = self.word_data.get(word)
                if word_info and word_info["情感分类_大类"] == emotion_type:
                    intensity = word_info["强度"]
                    total_intensity += intensity
            total_intensitys.append(total_intensity)

        return pd.DataFrame(data=total_intensitys, columns=[emotion_type])

    def get_intensity_data(self, data, emotion_types):
        intensity_data = pd.DataFrame(data)
        for emotion_type in emotion_types:
            total_intensitys = self.calculate_emotion_intensity(data, emotion_type)
            intensity_data = pd.concat([intensity_data, total_intensitys], axis=1)
        return intensity_data
