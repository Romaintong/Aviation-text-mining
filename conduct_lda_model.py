import pandas as pd
import os
from scipy.stats import wilcoxon
# 禁用SettingWithCopyWarning
pd.options.mode.chained_assignment = None  # 或者设置为 "warn" 来重新启用警告
# 禁止所有UserWarning
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from LDA_topic_model import LDATopicModelHTML

def concatenate_strings(dataframe, column_name):
    # 创建一个空字符串来存储结果
    concatenated_string = ""
    # 遍历指定列的每一行，并将字符串联接起来
    for row in dataframe[column_name]:
        if isinstance(row, str):
            concatenated_string += row
    return concatenated_string

## 找到3个topic的文件夹，并且进行对照组的划分，提取发生后的时间，整合content内容，分别构建主题模型
event_3U8633 = pd.read_csv('../output/3种航空事件数据集的文本处理和情感计算/processed_3U8633_related_content.csv')
event_MU5735 = pd.read_csv('../output/3种航空事件数据集的文本处理和情感计算/processed_MU5735_related_content.csv')
event_TV9833 = pd.read_csv('../output/3种航空事件数据集的文本处理和情感计算/processed_TV9833_related_content.csv')

# 进行lda主题建模
event_list = [event_3U8633['content'],event_MU5735['content'],event_TV9833['content']]
html_name = ['3U8633LDA求解','MU5735LDA求解','TV9833LDA求解']
for event,name in zip(event_list,html_name):
    filtered_list = [item for item in event if isinstance(item, str)]
    lda_html_model = LDATopicModelHTML(filtered_list, name)
    html_path = lda_html_model.generate_lda_html()
    print(f'生成的HTML文件保存在: {html_path}')