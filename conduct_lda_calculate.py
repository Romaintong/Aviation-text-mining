import pandas as pd
from TopicModelAnalyzer import TopicModelAnalyzer
import os

# 文件路径
save_dir_3 = '../figure/主题数选择/'
os.makedirs(save_dir_3, exist_ok=True)

# 进行lda主题建模
event_list = ['../output/3种航空事件数据集的文本处理和情感计算/processed_3U8633_related_content.csv',
                '../output/3种航空事件数据集的文本处理和情感计算/processed_MU5735_related_content.csv',
                '../output/3种航空事件数据集的文本处理和情感计算/processed_TV9833_related_content.csv']
figure_name = ['3U8633LDA求解','MU5735LDA求解','TV9833LDA求解']
for event,name in zip(event_list,figure_name):
    filtered_list = [item for item in event if isinstance(item, str)]
    analyzer = TopicModelAnalyzer(
        file_path= event,
        event_name = name,
        save_dir = save_dir_3
    )
    analyzer.analyze()
    # lda_html_model = LDATopicModelHTML(filtered_list, name)
    print(f'{name}已保存')