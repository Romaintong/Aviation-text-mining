import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

all_year_event_df = pd.read_csv('../output/所有时间所有事件数据集.csv')

# 对于zfjzhb,2018.4.1-2018.5.13,2018.5.14-2018.6.25时间内的数据，分为3U8633
# 对于zfjzhb,2022.2.6-2022.3.20.2022.3.21-2022.5.2时间内的数据，分为MU5735
# 对于zfjzhb,2022.3.20-2022.5.11,2022-5.12-2022.6.23时间内的数据，分为TV9833
condition1 = ((all_year_event_df['topic'] == 'zfjzhb') & (((all_year_event_df['time'] >= '2018-04-01') & (all_year_event_df['time'] <= '2018-05-13')) | ((all_year_event_df['time'] >= '2018-05-14') & (all_year_event_df['time'] <= '2018-06-25'))))
condition2 = ((all_year_event_df['topic'] == 'zfjzhb') & (((all_year_event_df['time'] >= '2022-02-06') & (all_year_event_df['time'] <= '2022-03-20')) | ((all_year_event_df['time'] >= '2022-03-21') & (all_year_event_df['time'] <= '2022-05-02'))))
condition3 = ((all_year_event_df['topic'] == 'zfjzhb') & (((all_year_event_df['time'] >= '2022-03-20') & (all_year_event_df['time'] <= '2022-05-11')) | ((all_year_event_df['time'] >= '2022-05-12') & (all_year_event_df['time'] <= '2022-06-23'))))
replacement_values = ['3U8633_related', 'MU5735_related', 'TV9833_related']
conditions = [condition1, condition2, condition3]
all_year_event_df['topic'] = np.select(conditions, replacement_values, default=all_year_event_df['topic'])

## 事件本身数据集
event_3U8633 = all_year_event_df[all_year_event_df['topic']=='3U8633']
event_MU5735 = all_year_event_df[all_year_event_df['topic']=='MU5735']
event_TV9833 = all_year_event_df[all_year_event_df['topic']=='TV9833']
event_3U8633.to_csv('../output/3种航空事件数据集/3U8633事件数据集.csv',index=False)
event_MU5735.to_csv('../output/3种航空事件数据集/MU5735事件数据集.csv',index=False)
event_TV9833.to_csv('../output/3种航空事件数据集/TV9833事件数据集.csv',index=False)

## zfjzhb数据集
event_3U8633 = all_year_event_df[all_year_event_df['topic']=='3U8633_related']
event_MU5735 = all_year_event_df[all_year_event_df['topic']=='MU5735_related']
event_TV9833 = all_year_event_df[all_year_event_df['topic']=='TV9833_related']
event_3U8633.to_csv('../output/坐飞机坐航班对照组/3U8633_related事件数据集.csv',index=False)
event_MU5735.to_csv('../output/坐飞机坐航班对照组/MU5735_related事件数据集.csv',index=False)
event_TV9833.to_csv('../output/坐飞机坐航班对照组/TV9833_related事件数据集.csv',index=False)

## 归因数据集整理
# 发生后时间的数据提取
# 提取2018.5.14-2018.6.25时间内的数据，为3U8633
# 提取2022.3.21-2022.5.2时间内的数据，为MU5735
# 提取2022-5.12-2022.6.23时间内的数据，为TV9833
condition4 = (all_year_event_df['topic'] == '3U8633' )
year2018_3U8633 = all_year_event_df[condition4]
condition5 = (all_year_event_df['topic'] == 'MU5735' )
year2022_MU5735 = all_year_event_df[condition5]
condition6 = (all_year_event_df['topic'] == 'TV9833' )
year2022_TV9833 = all_year_event_df[condition6]

# 提取出的数据整合，区分训练集和测试集，训练集选1000条数据，要求固定随机数种子
merged_data = pd.concat([year2018_3U8633, year2022_MU5735, year2022_TV9833], axis=0).reset_index(drop=True)
# 设置随机数种子以确保可复现性
random_seed = 42
# 随机选择 1000 条数据作为训练集
train_data, test_data = train_test_split(merged_data, train_size=2000, random_state=random_seed)
train_data.to_csv('../output/归因训练集以及测试集/归因训练的train集.csv',index=False)
test_data.to_csv('../output/归因训练集以及测试集/归因训练的test集.csv',index=False)