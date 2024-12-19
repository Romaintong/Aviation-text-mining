from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

class NaiveBayesClassifier:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()
    
    def train(self, train_data, train_labels):
        # 将训练文本转换为文档-词袋表示
        train_features = self.vectorizer.fit_transform(train_data)
        # 训练朴素贝叶斯模型
        self.model.fit(train_features, train_labels)
    
    def predict(self, test_data):
        # 将测试文本转换为文档-词袋表示
        test_features = self.vectorizer.transform(test_data)
        # 预测类别
        predicted_labels = self.model.predict(test_features)
        return predicted_labels
    
    def evaluate(self, test_data, test_labels):
        # 预测测试数据的类别
        predicted_labels = self.predict(test_data)
        # 计算准确率
        accuracy = accuracy_score(test_labels, predicted_labels)
        return accuracy

    def classify(self, train_data, train_labels, test_data):
        # 训练模型
        self.train(train_data, train_labels)
        # 预测测试数据的类别
        predicted_labels = self.predict(test_data)
        return predicted_labels