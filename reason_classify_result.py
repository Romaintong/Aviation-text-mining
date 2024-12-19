import pandas as pd 
from TextProcessor import TextProcessor # 进行文本处理
from emotion_calculator import EmotionCalculator # 进行情感细粒度计算
from emotion_analyze import DictClassifier # 进行情感极性分析
import os

def preprocess_emotion_dict(file_path='utils/情感词汇本体.xlsx'):
    # 读取情感词汇本体文件
    emotion_dict = pd.read_excel(file_path)
    # 选择需要的列并删除缺失值
    emotion_dict_2 = emotion_dict[['词语', '词性种类', '词义数', '词义序号', '情感分类', '强度', '极性']]
    emotion_dict_2 = emotion_dict_2.dropna(axis=0).reset_index(drop=True)
    # 定义情感分类的字典映射
    emotion_mapping = {
        "joy": ["PA", "PE"],
        "good": ["PD", "PH", "PG", "PB", "PK"],
        "surprise": ["PC"],
        "anger": ["NA"],
        "sadness": ["NB", "NJ", "NH", "PF"],
        "fear": ["NI", "NC", "NG"],
        "disgust": ["ND", "NE", "NN", "NK", "NL"]
    }
    # 使用apply方法根据情感分类进行映射
    emotion_dict_2['情感分类_大类'] = emotion_dict_2['情感分类'].apply(
        lambda x: next((key for key, value in emotion_mapping.items() if x in value), None)
    )
    return emotion_dict_2

def analyze_sentences(csv_file, d):
    results = []
    for line in csv_file:
        result = d.analyse_sentence(line)
        results.append(result)
    return results

if not(os.path.exists('../output/emotion_calculated_归因数据集.csv')):
    reason_classify_df = pd.read_csv('../output/归因后的全部数据集.csv').fillna('')
    type_lists = ["joy", "good", "surprise", "anger", "sadness", "fear", "disgust"]
    emotion_dict = preprocess_emotion_dict()
    emotion_calculator = EmotionCalculator(emotion_dict)
    d = DictClassifier()
    intensity_data = emotion_calculator.get_intensity_data(reason_classify_df['content'], type_lists)
    emotion_results = analyze_sentences(reason_classify_df['content'], d)
    emotion_score=pd.DataFrame(data=emotion_results,columns=['emotion_score'])
    intensity_data=pd.concat([intensity_data,emotion_score],axis=1)
    reason_emotion_df = pd.concat([reason_classify_df.drop('content',axis=1),intensity_data],axis=1)
    reason_emotion_df.to_csv('../output/emotion_calculated_归因数据集.csv',index=False)
else:
    reason_emotion_df = pd.read_csv('../output/emotion_calculated_归因数据集.csv')

content_3U8633 = pd.read_csv('../output/事件本身的言论/emotion_calculated_3U8633.csv')
content_MU5735 = pd.read_csv('../output/事件本身的言论/emotion_calculated_MU5735.csv')
content_TV9833 = pd.read_csv('../output/事件本身的言论/emotion_calculated_TV9833.csv')
processed_reason_emotion_df = reason_emotion_df[['topic','reason','type','joy', 'good',\
       'surprise', 'anger', 'sadness', 'fear', 'disgust', 'emotion_score']]
event_3U8633_reason_emotion_df = processed_reason_emotion_df[processed_reason_emotion_df['topic']=='3U8633'].drop('topic',axis=1)
event_MU5735_reason_emotion_df = processed_reason_emotion_df[processed_reason_emotion_df['topic']=='MU5735'].drop('topic',axis=1)
event_TV9833_reason_emotion_df = processed_reason_emotion_df[processed_reason_emotion_df['topic']=='TV9833'].drop('topic',axis=1)
reason_emotion_df_type = [event_3U8633_reason_emotion_df,event_MU5735_reason_emotion_df,event_TV9833_reason_emotion_df]
name_list = ['3U8633','MU5735','TV9833']
for event,name in zip(reason_emotion_df_type,name_list):
    grouped_data = event.groupby(['reason', 'type']).mean()
    grouped_data.to_csv(f'../output/归因结果/{name}的归因结果.csv')