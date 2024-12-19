import pandas as pd 
from NaiveBayesClassifier import NaiveBayesClassifier
from TextProcessor import TextProcessor

train_df = pd.read_excel('../output/归因训练集以及测试集/标记好的归因训练的train集.xlsx').fillna('')
test_df = pd.read_csv('../output/归因训练集以及测试集/归因训练的test集.csv').fillna('')

# 分类器,文本处理器
classifier = NaiveBayesClassifier()
text_processor = TextProcessor()

# 处理以及替换

train_content = text_processor.preprocess_data(train_df['content'])
test_content = text_processor.preprocess_data(test_df['content'])
train_df['content'] = train_content
test_df['content'] = test_content


## 首先提取出reason及其对象进行大分类的标注，然后去除无关，提取type及其对象进一步标注

# 提取大分类进行训练
train_layer1_type = train_df.drop('type',axis=1)
train_layer1_type['reason'] =  [item.strip() for item in train_layer1_type['reason'] ]
train_content = train_layer1_type['content']
test_content = test_df['content']
predicted_labels = classifier.classify(train_content, train_layer1_type['reason'], test_content)
predicted_labels_df = pd.DataFrame(data=predicted_labels, columns=['reason'])
test_layer1_df = pd.concat([test_df, predicted_labels_df], axis=1)

# 提取小分类进行训练
out_df = test_layer1_df[test_layer1_df['reason'] == '外']
in_df = test_layer1_df[test_layer1_df['reason'] == '内']
none_type_df =test_layer1_df[test_layer1_df['reason'] == '无关']

# 对于外，首先提取训练集外的df，获得content和df，然后提取测试集的content，按照格式粘贴回去
train_layer2_type_out_df = train_df[train_df['reason']=='外'].drop('reason',axis=1)
train_content = train_layer2_type_out_df['content']
train_label = [item.strip() for item in train_layer2_type_out_df['type'] ]
test_content = out_df['content']
predicted_labels = classifier.classify(train_content, train_label, test_content)
predicted_labels_df = pd.DataFrame(data=predicted_labels, columns=['type'])
test_layer2_type_out_df = pd.concat([out_df.reset_index(drop=True), predicted_labels_df], axis=1,ignore_index=True)

# 对于内
train_layer2_type_in_df = train_df[train_df['reason']=='内'].drop('reason',axis=1)
train_content = train_layer2_type_in_df['content']
train_label = [item.strip() for item in train_layer2_type_in_df['type'] ]
test_content = in_df['content']
predicted_labels = classifier.classify(train_content, train_label, test_content)
predicted_labels_df = pd.DataFrame(data=predicted_labels, columns=['type'])
test_layer2_type_in_df = pd.concat([in_df.reset_index(drop=True), predicted_labels_df], axis=1,ignore_index=True)

# 对于无关
none_type_df['type'] = ''
none_type_df = none_type_df.reset_index(drop=True)

# 三个子类竖向拼接，然后train和test竖向拼接
test_layer2_type_out_df.columns = train_df.columns.tolist()
test_layer2_type_in_df.columns = train_df.columns.tolist()
all_df = pd.concat([test_layer2_type_out_df,test_layer2_type_in_df,none_type_df,train_df],axis=0)
all_df = all_df.reset_index(drop=True)
all_df.to_csv('../output/归因训练集以及测试集/归因后的全部数据集.csv',index=False)