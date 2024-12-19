import os
import re
import pandas as pd


def process_time(time):
    try:
        # 尝试将时间转换为datetime
        return pd.to_datetime(time)
    except:
        # 使用正则表达式提取年、月、日信息
        date_pattern = r'(\d{4})年(\d{1,2})月(\d{1,2})日'
        match = re.search(date_pattern, time)
        if match:
            year, month, day = match.groups()
            # 返回处理后的datetime
            return pd.to_datetime(f"{year}-{month.zfill(2)}-{day.zfill(2)}", format='%Y-%m-%d')
        else:
            return pd.NaT  # 如果无法处理，返回NaT


def get_event_type(file_name):
    # 使用正则表达式来匹配文件名中的事件类型
    match = re.search(r'(3U8633|MU5735|TV9833)', file_name)

    # 如果匹配成功，则返回匹配到的事件类型，否则返回None
    if match:
        return match.group(0)
    else:
        return 'zfjzhb'


def date(para):
    # 将数字时间转化为正常值，并且根据时间排序,重置索引
    try:
        delta = pd.Timedelta(str(para) + 'days')
        time = pd.to_datetime('1899-12-30') + delta
        return time
    except:
        return para
# economic_data['time']=economic_data['time'].apply(date)

folder_path = '../data/总/'
all_df = pd.DataFrame(columns = ["time","content","topic"])

for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
    # csv文件dy下，时间	标题	评论	评论时间
    # csv文件wb下，时间	文本
        file_path = os.path.join(folder_path, filename)
        try:
            data = pd.read_csv(file_path,encoding = 'ansi') [['时间','文本']]
        except:
            data = pd.read_csv(file_path,encoding = 'ansi') [['时间','评论']]
        data.columns = ["time","content"]
        data.dropna(subset=['content'], inplace=True)
        data.reset_index(drop=True, inplace=True)
        data['topic'] = get_event_type(filename)
        # 加入
        all_df = pd.concat([all_df,data],axis=0)
    if filename.endswith('.xlsx'):
    # excel文件xhs下，链接	发文时间	文章标题	内容	评论时间	评论内容
    # excel文件wb下，时间	文本
        file_path = os.path.join(folder_path, filename)
        excel_file = pd.ExcelFile(file_path)
        sheet_names = excel_file.sheet_names
        for sheet_name in sheet_names:
            try:
                data = pd.read_excel(excel_file, sheet_name=sheet_name)[['时间','文本']]
            except:
                data = pd.read_excel(excel_file, sheet_name=sheet_name)[['评论时间','评论内容']]
            data.columns = ["time","content"]
            data['time'] = data['time'].apply(date)
            data.dropna(subset=['content'], inplace=True)
            data.reset_index(drop=True, inplace=True)
            data['topic'] = get_event_type(filename)
            all_df = pd.concat([all_df,data],axis=0)
all_df['time'] = all_df['time'].apply(process_time).dt.date
all_df.dropna(subset=['time'], inplace=True)
# 进行去重
all_df.drop_duplicates(subset='content', inplace=True)
all_df.reset_index(drop=True, inplace=True)
all_df.to_csv('../output/所有时间所有事件数据集.csv',index=False)