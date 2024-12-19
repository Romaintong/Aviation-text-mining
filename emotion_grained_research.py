import pandas as pd 
import os
from TextProcessor import TextProcessor # 进行文本处理
from emotion_classify import EmotionAnalyzer # 进行情感细粒度分类
from emotion_calculator import EmotionCalculator # 进行情感细粒度计算
from emotion_analyze import DictClassifier # 进行情感极性分析

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

## 首先进行文本处理，然后进行情感细粒度分析和计算，最后进行情感极性分析，并将结果输出
# 关于zfjzhb
processed_file_names = ['processed_3U8633_related_content.csv', 'processed_MU5735_related_content.csv','processed_TV9833_related_content.csv']
emotion_calculate_names = ['emotion_calculated_3U8633.csv', 'emotion_calculated_MU5735.csv','emotion_calculated_TV9833.csv']
# 关于三个事件
processed_file_names_2 = ['processed_3U8633_content.csv', 'processed_MU5735_content.csv','processed_TV9833_content.csv']
emotion_calculate_names_2 = ['emotion_calculated_3U8633.csv', 'emotion_calculated_MU5735.csv','emotion_calculated_TV9833.csv']

## 关于zfjzhb

if any(not os.path.exists(os.path.join('../output/坐飞机坐航班对照组的文本处理和情感计算/', file_name)) for file_name in processed_file_names):
    # 文本处理
    text_processor = TextProcessor()
    event_3U8633_df = pd.read_csv('../output/坐飞机坐航班对照组/3U8633_related事件数据集.csv')
    event_MU5735_df = pd.read_csv('../output/坐飞机坐航班对照组/MU5735_related事件数据集.csv')
    event_TV9833_df = pd.read_csv('../output/坐飞机坐航班对照组/TV9833_related事件数据集.csv')
    content_df_list = [event_3U8633_df['content'],event_MU5735_df['content'],event_TV9833_df['content']]
    output_name_list = ['3U8633','MU5735','TV9833']
    # content_df_list = [year2018_df['content']]
    for content_df,output_name in zip(content_df_list,output_name_list):
        processed_df = text_processor.preprocess_data(content_df)
        processed_df = pd.DataFrame(data = processed_df ,columns = ['content'])
        processed_df.to_csv(f'../output/processed_{output_name}_related_content.csv',index=False)
    # 将NaN值填充为空字符串,否则细粒度分类会报错
    processed_3U8633_content = pd.read_csv('../output/坐飞机坐航班对照组的文本处理和情感计算/processed_3U8633_related_content.csv')['content'].fillna('').tolist()
    processed_MU5735_content = pd.read_csv('../output/坐飞机坐航班对照组的文本处理和情感计算/processed_MU5735_related_content.csv')['content'].fillna('').tolist()
    processed_TV9833_content = pd.read_csv('../output/坐飞机坐航班对照组的文本处理和情感计算/processed_TV9833_related_content.csv')['content'].fillna('').tolist()
else:
    # 将NaN值填充为空字符串,否则细粒度分类会报错
    processed_3U8633_content = pd.read_csv('../output/坐飞机坐航班对照组的文本处理和情感计算/processed_3U8633_related_content.csv')['content'].fillna('').tolist()
    processed_MU5735_content = pd.read_csv('../output/坐飞机坐航班对照组的文本处理和情感计算/processed_MU5735_related_content.csv')['content'].fillna('').tolist()
    processed_TV9833_content = pd.read_csv('../output/坐飞机坐航班对照组的文本处理和情感计算/processed_TV9833_related_content.csv')['content'].fillna('').tolist()

# 情感细粒度计算
if any(not os.path.exists(os.path.join('../output/坐飞机坐航班对照组的文本处理和情感计算/', file_name)) for file_name in emotion_calculate_names):
    type_lists = ["joy", "good", "surprise", "anger", "sadness", "fear", "disgust"]
    emotion_dict = preprocess_emotion_dict()
    emotion_calculator = EmotionCalculator(emotion_dict)
    d = DictClassifier()
    content_df_list = [processed_3U8633_content,processed_MU5735_content,processed_TV9833_content]
    output_name_list = ['3U8633','MU5735','TV9833']
    # content_df_list = [year2018_df['content']]
    for content_df,output_name in zip(content_df_list,output_name_list):
        intensity_data = emotion_calculator.get_intensity_data(content_df, type_lists)
        emotion_results = analyze_sentences(content_df, d)
        emotion_score=pd.DataFrame(data=emotion_results,columns=['emotion_score'])
        intensity_data=pd.concat([intensity_data,emotion_score],axis=1)
        intensity_data.to_csv(f'../output/坐飞机坐航班对照组的文本处理和情感计算/emotion_calculated_{output_name}.csv',index=False)

print('坐飞机做航班数据集处理完毕')

## 关于三个事件
## 关于三个事件
if any(not os.path.exists(os.path.join('../output/3种航空事件数据集的文本处理和情感计算/', file_name)) for file_name in processed_file_names_2):
    # 文本处理
    text_processor = TextProcessor()
    event_3U8633_df = pd.read_csv('../output/3种航空事件数据集/3U8633事件数据集.csv')
    event_MU5735_df = pd.read_csv('../output/3种航空事件数据集/MU5735事件数据集.csv')
    event_TV9833_df = pd.read_csv('../output/3种航空事件数据集/TV9833事件数据集.csv')
    content_df_list = [event_3U8633_df['content'],event_MU5735_df['content'],event_TV9833_df['content']]
    output_name_list = ['3U8633','MU5735','TV9833']
    # content_df_list = [year2018_df['content']]
    for content_df,output_name in zip(content_df_list,output_name_list):
        processed_df = text_processor.preprocess_data(content_df)
        processed_df = pd.DataFrame(data = processed_df ,columns = ['content'])
        processed_df.to_csv(f'../output/3种航空事件数据集的文本处理和情感计算/processed_{output_name}_related_content.csv',index=False)
    # 将NaN值填充为空字符串,否则细粒度分类会报错
    processed_3U8633_content = pd.read_csv('../output/3种航空事件数据集的文本处理和情感计算/processed_3U8633_related_content.csv')['content'].fillna('').tolist()
    processed_MU5735_content = pd.read_csv('../output/3种航空事件数据集的文本处理和情感计算/processed_MU5735_related_content.csv')['content'].fillna('').tolist()
    processed_TV9833_content = pd.read_csv('../output/3种航空事件数据集的文本处理和情感计算/processed_TV9833_related_content.csv')['content'].fillna('').tolist()
else:
    # 将NaN值填充为空字符串,否则细粒度分类会报错
    processed_3U8633_content = pd.read_csv('../output/3种航空事件数据集的文本处理和情感计算/processed_3U8633_content.csv')['content'].fillna('').tolist()
    processed_MU5735_content = pd.read_csv('../output/3种航空事件数据集的文本处理和情感计算/processed_MU5735_content.csv')['content'].fillna('').tolist()
    processed_TV9833_content = pd.read_csv('../output/3种航空事件数据集的文本处理和情感计算/processed_TV9833_content.csv')['content'].fillna('').tolist()

# 情感细粒度计算
if any(not os.path.exists(os.path.join('../output/3种航空事件数据集的文本处理和情感计算/', file_name)) for file_name in emotion_calculate_names_2):
    type_lists = ["joy", "good", "surprise", "anger", "sadness", "fear", "disgust"]
    emotion_dict = preprocess_emotion_dict()
    emotion_calculator = EmotionCalculator(emotion_dict)
    d = DictClassifier()
    content_df_list = [processed_3U8633_content,processed_MU5735_content,processed_TV9833_content]
    output_name_list = ['3U8633','MU5735','TV9833']
    # content_df_list = [year2018_df['content']]
    for content_df,output_name in zip(content_df_list,output_name_list):
        intensity_data = emotion_calculator.get_intensity_data(content_df, type_lists)
        emotion_results = analyze_sentences(content_df, d)
        emotion_score=pd.DataFrame(data=emotion_results,columns=['emotion_score'])
        intensity_data=pd.concat([intensity_data,emotion_score],axis=1)
        intensity_data.to_csv(f'../output/3种航空事件数据集的文本处理和情感计算/emotion_calculated_{output_name}.csv',index=False)

print('3种航空事件数据集处理完毕')