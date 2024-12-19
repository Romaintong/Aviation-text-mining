import pandas as pd
import os
from scipy.stats import wilcoxon

# 禁用SettingWithCopyWarning
pd.options.mode.chained_assignment = None  # 或者设置为 "warn" 来重新启用警告

# 禁止所有UserWarning
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号 #有中文出现的情况，需要u'内容'

import seaborn as sns


def plot_emotion_trend(event_data, event_name, save_dir):
    data = event_data.copy()
    data = data.set_index('datetime', drop=True)
    emotions = ['joy', 'good', 'surprise', 'anger', 'sadness', 'fear', 'disgust', 'emotion_score']

    # 创建一个新的figure
    plt.figure(figsize=(15, 5))

    for emotion in emotions:
        plt.plot(data.index, data[emotion], label=emotion)

    plt.xlabel('日期')
    plt.ylabel('情感值')
    plt.title(f'{event_name}的8种情感的时间趋势图')
    plt.legend(loc='best')
    plt.grid(True)

    # 显式指定X轴刻度的日期范围，例如，从数据的最小日期到最大日期
    x_min = data.index.min()
    x_max = data.index.max()
    x_ticks = pd.date_range(data.index.min(), data.index.max(), freq='1M')
    x_ticks_labels = [str(date.date()) for date in x_ticks]
    plt.xticks(x_ticks, x_ticks_labels, rotation=45)  # 旋转刻度标签，以便更好地显示

    plt.tight_layout()

    # 保存趋势图
    filename = f'{event_name}_趋势图.png'
    save_path = os.path.join(save_dir, filename)
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()


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


## 对事件本身讨论的情绪变化趋势和情绪分类。数据：事件后六周爬取的与事件本身相关的言论。
event_3U8633 = pd.read_csv('../output/3种航空事件数据集/3U8633事件数据集.csv')
event_MU5735 = pd.read_csv('../output/3种航空事件数据集/MU5735事件数据集.csv')
event_TV9833 = pd.read_csv('../output/3种航空事件数据集/TV9833事件数据集.csv')
content_3U8633 = pd.read_csv('../output/3种航空事件数据集的文本处理和情感计算/emotion_calculated_3U8633.csv')
content_MU5735 = pd.read_csv('../output/3种航空事件数据集的文本处理和情感计算/emotion_calculated_MU5735.csv')
content_TV9833 = pd.read_csv('../output/3种航空事件数据集的文本处理和情感计算/emotion_calculated_TV9833.csv')
event_3U8633 = pd.concat([event_3U8633.drop(['content', 'topic'], axis=1), content_3U8633.drop('0', axis=1)], axis=1)
event_MU5735 = pd.concat([event_MU5735.drop(['content', 'topic'], axis=1), content_MU5735.drop('0', axis=1)], axis=1)
event_TV9833 = pd.concat([event_TV9833.drop(['content', 'topic'], axis=1), content_TV9833.drop('0', axis=1)], axis=1)
event_3U8633 = event_resample(event_3U8633)
event_MU5735 = event_resample(event_MU5735)
event_TV9833 = event_resample(event_TV9833)
event_3U8633.to_csv('../figure/趋势图/event_3U8633.csv',index=False)
event_MU5735.to_csv('../figure/趋势图/event_MU5735.csv',index=False)
event_TV9833.to_csv('../figure/趋势图/event_TV9833.csv',index=False)

# 文件路径
save_dir_3 = '../figure/趋势图/'
os.makedirs(save_dir_3, exist_ok=True)

# 依次画图
event_after_list = [event_3U8633, event_MU5735, event_TV9833]
event_name = ['3U8633', 'MU5735', 'TV9833']
for event, name in zip(event_after_list, event_name):
    plot_emotion_trend(event, name, save_dir_3)