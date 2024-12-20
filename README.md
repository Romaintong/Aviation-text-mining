```markdown
# Code Repository for "Dare to Fly? Analyzing Psychological Reactions and Travel Attitudes of Chinese Social Media Users Post-Aviation Accidents through Text Mining"

This repository contains a collection of Python scripts for emotional analysis and topic modeling of textual data. The project includes data processing, sentiment analysis, emotion classification, and LDA topic modeling.

## Table of Contents

1. [Repository Description](#repository-description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [File Descriptions](#file-descriptions)
5. [Contributing](#contributing)
6. [License](#license)

## Repository Description

This repository contains the code for the research project titled "Dare to Fly? Analyzing Psychological Reactions and Travel Attitudes of Chinese Social Media Users Post-Aviation Accidents through Text Mining." The study focuses on three aviation incidents, and the code for data collection, analysis, and presentation is shared here.


## Installation

To install the required packages, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. **Data Processing:**
   Run `data_process.py` to process and prepare the data.

2. **Emotion Analysis:**
   Use `emotion_analyze.py` and `emotion_calculator.py` for sentiment analysis.

3. **LDA Topic Modeling:**
   Run `conduct_lda_model.py` to perform LDA topic modeling.

4. **Visualization:**
   Use `emotion_grained_research_result.py` to generate visualizations of emotional trends.

## File Descriptions

- `conduct_lda_calculate.py`: Calculates the perplexity of the LDA model to evaluate the effectiveness of different topic numbers.  
  **Dependencies**: gensim, matplotlib, numpy, os  
  **Environment**: Python 3.10, Jupyter/IDE

- `conduct_lda_model.py`: Performs topic modeling using the LDA model, training, and saving the topic model.  
  **Dependencies**: gensim, matplotlib, numpy, os  
  **Environment**: Python 3.10, Jupyter/IDE

- `data_extract.py`: Extracts data from sources and performs basic processing.  
  **Dependencies**: pandas, numpy  
  **Environment**: Python 3.10, Jupyter/IDE

- `data_process.py`: Conducts data cleaning and preprocessing, such as removing missing values and feature selection.  
  **Dependencies**: pandas, numpy, re  
  **Environment**: Python 3.10, Jupyter/IDE

- `emotion_analyze.py`: Performs sentiment polarity analysis based on emotional vocabulary.  
  **Dependencies**: pandas, jieba, sklearn  
  **Environment**: Python 3.10, Jupyter/IDE

- `emotion_calculator.py`: Calculates emotional intensity values and performs emotional calculations based on emotional vocabulary.  
  **Dependencies**: pandas, jieba, numpy  
  **Environment**: Python 3.10, Jupyter/IDE

- `emotion_classify.py`: Uses classifiers for emotional classification.  
  **Dependencies**: sklearn, pandas, jieba  
  **Environment**: Python 3.10, Jupyter/IDE

- `emotion_grained_research_result_2.py`: Further emotional research based on fine-grained emotional analysis results, calculating emotional scores.  
  **Dependencies**: pandas, numpy  
  **Environment**: Python 3.10, Jupyter/IDE

- `emotion_grained_research_result.py`: Processes fine-grained emotional analysis results, calculating scores for different emotional dimensions.  
  **Dependencies**: pandas, numpy  
  **Environment**: Python 3.10, Jupyter/IDE

- `emotion_grained_research.py`: Extracts and calculates data and scores for fine-grained emotional analysis.  
  **Dependencies**: pandas, jieba, numpy  
  **Environment**: Python 3.10, Jupyter/IDE

- `LDA_topic_model.py`: Performs LDA topic modeling on text, calculates the effectiveness of the topic model, and saves it.  
  **Dependencies**: gensim, matplotlib, numpy  
  **Environment**: Python 3.10, Jupyter/IDE

- `LDA.py`: Trains the LDA model, generates a document-topic matrix, and visualizes topics.  
  **Dependencies**: gensim, matplotlib, pandas  
  **Environment**: Python 3.10, Jupyter/IDE

- `NaiveBayesClassifier.py`: Uses a Naive Bayes classifier for text classification, training, and prediction.  
  **Dependencies**: sklearn, pandas  
  **Environment**: Python 3.10, Jupyter/IDE

- `reason_classify_result.py`: Extracts and processes attribution classification results, combining emotional scores with attribution information.  
  **Dependencies**: pandas, numpy  
  **Environment**: Python 3.10, Jupyter/IDE

- `reason_classify.py`: Uses classification algorithms for text attribution classification, annotating attribution types.  
  **Dependencies**: sklearn, pandas, jieba  
  **Environment**: Python 3.10, Jupyter/IDE

- `TextProcessor.py`: Performs text preprocessing, including tokenization, removal of stop words, and special character processing.  
  **Dependencies**: jieba, re  
  **Environment**: Python 3.10, Jupyter/IDE

- `TopicModelAnalyzer.py`: Analyzes text data using the LDA model, evaluates model effectiveness under different topic numbers, and generates coherence score trend graphs.  
  **Dependencies**: gensim, matplotlib, numpy, os  
  **Environment**: Python 3.10, Jupyter/IDE

- `code_wilcx1`: Uses the non-paired Wilcoxon test to calculate statistical measures, p-values, standard deviations, and effect sizes for emotional changes before and after each event.  
  **Dependencies**: lsr, stats (wilcox.test), base  
  **Environment**: R, RStudio

- `code_wilcx2`: Uses the ggpubr package to plot violin diagrams, showing the distribution of different emotions between different groups.  
  **Dependencies**: ggpubr, reshape2, base  
  **Environment**: R, RStudio

- `file operations`: Python script for attribution classification using a Naive Bayes Classifier.  
  **Dependencies**: pandas, NaiveBayesClassifier, TextProcessor  
  **Environment**: Python 3.10

- `TikTok.py`: Scrapes raw data from the TikTok platform.  
  **Dependencies**: selenium, lxml, time, csv, random  
  **Environment**: Google Chrome, ChromeDriver, Python 3.10, CVS

- `Little Red Book.py`: Scrapes raw data from the Little Red Book platform.  
  **Dependencies**: selenium, lxml, time, csv  
  **Environment**: Google Chrome, ChromeDriver, Python 3.10, CVS

- `microblog.py`: Scrapes raw data from the microblog platform.  
  **Dependencies**: requests, bs4, selenium, csv, datetime, os  
  **Environment**: Google Chrome, ChromeDriver, Python 3.10, CVS

## Contributing

Contributions to this project are welcome. Please submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
