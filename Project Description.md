| 文件名 |职责|功能| input |output|
| ------------------ | :----------------- | ------------------ | :----------------------------------------------------------- |------------------ |
| data_process.py    |处理文件|提取2018，2022文件夹的数据，提取时间、信息、话题| data文件夹  <br />按照时间和事件整理的数据 |2018年时间及评论数据.csv<br />2022年时间及评论数据.csv|
| emotion_classify.py |模块|进行情感细粒度分类|                                                              ||
| emotion_calculator.py |模块|进行情感细粒度计算| ||
| emotion_analyze.py |模块|进行情感极性分析|  ||
| TextProcessor.py |模块|进行文本处理| ||
| emotion_grained_research.py |处理文件|对于指定文件夹的content进行情感细粒度研究| 2018年时间及评论数据.csv<br />2022年时间及评论数据.csv |emotion_calculated.csv<br />processed_content.csv<br />|
| data_extract.py |处理文件|对于处理过的2018和2022数据进一步处理，分为3个topic| 2018年时间及评论数据.csv<br />2022年时间及评论数据.csv |3个topic文件|
| emotion_grained_research_result.py |处理文件|情感细粒度的结果进一步研究|  |图和t检验结果|
| LDA_topic_model.py |模块|主题模型建模|  ||
| conduct_lda_model.py |处理文件|应用模块进行建模| ||
| NaiveBayesClassifier.py |模块|朴素贝叶斯分类器|  ||
| reason_classify.py |处理文件|归因|  ||
| reason_classify_result.py |处理文件|对归因后的数据集分别进行情感计算| ||
