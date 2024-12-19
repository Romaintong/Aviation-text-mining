import pandas as pd 
import os 
from scipy.stats import wilcoxon
import scipy.stats as stats

# 禁用SettingWithCopyWarning
pd.options.mode.chained_assignment = None  # 或者设置为 "warn" 来重新启用警告

# 禁止所有UserWarning
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号 #有中文出现的情况，需要u'内容'

import seaborn as sns

def event_resample(df):
    # 将'datetime'列转换为日期时间类型
    df['datetime'] = pd.to_datetime(df['time'])

    # 使用groupby按日期进行分组，并计算每日情绪值的平均值
    daily_avg_emotion = df.groupby('datetime').agg({
        'joy': 'mean',
        'good': 'mean',
        'surprise': 'mean',
        'anger': 'mean',
        'sadness': 'mean',
        'fear': 'mean',
        'disgust': 'mean',
        'emotion_score': 'mean'
    }).reset_index()
    return daily_avg_emotion

## 找到3个topic的文件夹，并且进行对照组的划分，然后分别进行显著性检验以及事件发生前后的情感值绘图
event_3U8633 = pd.read_csv('../output/坐飞机坐航班对照组/3U8633_related事件数据集.csv')
event_MU5735 = pd.read_csv('../output/坐飞机坐航班对照组/MU5735_related事件数据集.csv')
event_TV9833 = pd.read_csv('../output/坐飞机坐航班对照组/TV9833_related事件数据集.csv')
content_3U8633 = pd.read_csv('../output/坐飞机坐航班对照组的文本处理和情感计算/emotion_calculated_3U8633.csv')
content_MU5735 = pd.read_csv('../output/坐飞机坐航班对照组的文本处理和情感计算/emotion_calculated_MU5735.csv')
content_TV9833 = pd.read_csv('../output/坐飞机坐航班对照组的文本处理和情感计算/emotion_calculated_TV9833.csv')
event_3U8633 = pd.concat([event_3U8633.drop(['content', 'topic'],axis=1),content_3U8633.drop('0',axis=1)],axis=1)
event_MU5735 = pd.concat([event_MU5735.drop(['content', 'topic'],axis=1),content_MU5735.drop('0',axis=1)],axis=1)
event_TV9833 = pd.concat([event_TV9833.drop(['content', 'topic'],axis=1),content_TV9833.drop('0',axis=1)],axis=1)


# 对照组和对照组划分
# 定义日期范围
date_range_3U8633_1 = ('2018-04-01', '2018-05-13')
date_range_3U8633_2 = ('2018-05-14', '2018-06-25')
date_range_MU5735_1 = ('2022-02-06', '2022-03-20')
date_range_MU5735_2 = ('2022-03-21', '2022-05-02')
date_range_TV9833_1 = ('2022-03-20', '2022-05-11')
date_range_TV9833_2 = ('2022-05-12', '2022-06-23')
# 对于2018.4.1-2018.5.13,2018.5.14-2018.6.25时间内的数据，分为3U8633
# 对于2022.2.6-2022.3.20.2022.3.21-2022.5.2时间内的数据，分为MU5735
# 对于2022.3.20-2022.5.11,2022-5.12-2022.6.23时间内的数据，分为TV9833
event_3U8633_1 = event_3U8633[(event_3U8633['time'] >= date_range_3U8633_1[0]) & (event_3U8633['time'] <= date_range_3U8633_1[1])]
event_3U8633_2 = event_3U8633[(event_3U8633['time'] >= date_range_3U8633_2[0]) & (event_3U8633['time'] <= date_range_3U8633_2[1])]
event_MU5735_1 = event_MU5735[(event_MU5735['time'] >= date_range_MU5735_1[0]) & (event_MU5735['time'] <= date_range_MU5735_1[1])]
event_MU5735_2 = event_MU5735[(event_MU5735['time'] >= date_range_MU5735_2[0]) & (event_MU5735['time'] <= date_range_MU5735_2[1])]
event_TV9833_1 = event_TV9833[(event_TV9833['time'] >= date_range_TV9833_1[0]) & (event_TV9833['time'] <= date_range_TV9833_1[1])]
event_TV9833_2 = event_TV9833[(event_TV9833['time'] >= date_range_TV9833_2[0]) & (event_TV9833['time'] <= date_range_TV9833_2[1])]

# 进行时间校准
event_3U8633_1 = event_resample(event_3U8633_1) #43
event_3U8633_2 = event_resample(event_3U8633_2) #43
event_MU5735_1 = event_resample(event_MU5735_1) #43
event_MU5735_2 = event_resample(event_MU5735_2) #43
event_TV9833_1 = event_resample(event_TV9833_1) #9
event_TV9833_2 = event_resample(event_TV9833_2) #43

for file,name in zip([event_3U8633_2,event_MU5735_2,event_TV9833_2],['3U8633','MU5735','TV9833']):
    file.to_csv(f'../data/{name}按月份情感值总和.csv',index=False)

# 创建图片保存目录
save_dir = '../figure/不同事件不同情感的前后趋势对比图/'
os.makedirs(save_dir, exist_ok=True)
save_dir_2 = '../figure/不同事件不同情感的分布对比图/'
os.makedirs(save_dir_2, exist_ok=True)
# 配置配色
color_before = '#ff9f00'
color_after = '#0c213c'

# 进行t检验
t_results = []
type_lists = ["joy", "good", "surprise", "sadness", "fear", "disgust","emotion_score"]
event_1_list = [event_3U8633_1,event_MU5735_1]
event_2_list = [event_3U8633_2,event_MU5735_2]
event_name = ['3U8633','MU5735']
for emotion_type in type_lists:
    for event_1, event_2,name in zip(event_1_list, event_2_list,event_name):
        emotion_df_1 = event_1[emotion_type]
        emotion_df_2 = event_2[emotion_type]

        # 正态性检验
        _, p_value_1 = stats.normaltest(emotion_df_1)
        _, p_value_2 = stats.normaltest(emotion_df_2)

        # 检查p值来决定使用t检验还是Wilcoxon符号秩检验
        alpha = 0.05  # 设定显著性水平

        if p_value_1 > alpha and p_value_2 > alpha:
            # 两个数据列都服从正态分布，使用t检验
            _, p_value = stats.ttest_ind(emotion_df_1, emotion_df_2)
            test_used = 't-test'
        else:
            # 至少有一个数据列不服从正态分布，使用Wilcoxon符号秩检验
            _, p_value = stats.wilcoxon(emotion_df_1, emotion_df_2)
            test_used = 'Wilcoxon Rank Sum Test'

        # 将结果添加到结果列表中
        t_results.append({
            'event': name,
            'Emotion Type': emotion_type,
            'Test Used': test_used,
            'P-Value': p_value
        })

        # 绘制变化图
        plt.figure(figsize=(15, 6))
        plt.plot(emotion_df_1, label='事件发生前的情绪', linestyle='-', marker='o', color=color_before)
        plt.plot(emotion_df_2, label='事件发生后的情绪', linestyle='-', marker='s', color=color_after)
        plt.xlabel('时间')
        plt.ylabel('情感值')
        plt.title(f'{name}的{emotion_type}情绪趋势对比')
        plt.grid(True)  # 添加网格线
        # 获取顺序序号和用户列表
        x_ticks = list(range(1, len(emotion_df_1) + 1))
        # 设置每隔10个数据点显示一个标签
        step = 10
        plt.xticks(x_ticks[::step], x_ticks[::step], rotation=45, ha='right')
        # 调整图例位置为右上角
        plt.legend(loc='upper right')
        plt.tight_layout()
        # 保存变化图
        filename = f'{emotion_type}_{name}_变化图.png'
        save_path = os.path.join(save_dir, filename)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        # 绘制分布图
        fig, ax = plt.subplots()
        sns.kdeplot(emotion_df_1, color=color_before, label='事件发生前的情绪', ax=ax, fill=True)
        sns.kdeplot(emotion_df_2, color=color_after, label='事件发生后的情绪', ax=ax, fill=True)
        plt.title(f'{name}的{emotion_type}情绪分布对比')
        plt.xlabel('Emotion Value')
        plt.ylabel('密度')
        plt.legend()
        # 保存分布图
        filename = f'{emotion_type}_{name}_分布图.png'
        save_path = os.path.join(save_dir_2, filename)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
# 输出df
t_test_results = pd.DataFrame(t_results)
t_test_results.to_csv('../output/结果分析/t检验结果.csv',index=False)