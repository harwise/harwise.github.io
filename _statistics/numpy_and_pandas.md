---
layout: default
title: numpy and pandas
---

{% include katex.html %}

# python
```
for key, value in zip(region, university_count):

from collections import Counter
cnt = Counter(data) # 计数每个值出现的次数

def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r
```

# ipython
```
display
```

# numpy

```
import numpy as np

hamSamples = X_train_vec[y_train == "ham"] # 选取某些行

Yvalues, counts = np.unique(y_train, return_counts=True)
spamTotal = np.sum(spamSamples)
hamProb = np.log2(hamProb)
```

# pandas

```
import pandas as pd # 数据处理

data_df = pd.read_csv("data.csv", sep=',')  # 读入csv文件为pandas的DataFrame

data_df.head(3).T  # 观察前几列并转置方便观察
print(data_df.iloc[0])      # 输出第一行数据
data_df.describe()          # 每列特征的简单统计信息

# 可以用 pd.set_option('display.max_columns', None) 使得 data_df.describe() 输出能够显示所有列。

data_df = data_df.drop(columns='gameId')    # 舍去对局标号列
data_df = data_df.dropna()  # 舍去包含 NaN 的 row

mean_df = data_df.groupby('institution').mean()  # 按学校聚合并对聚合的列取平均
top_df = mean_df.sort_values(by='score', ascending=False)   # sort
f = data_df[feature_cols + ['score']].corr()

# 数据离散化
# if (len(df[c].unique()) <= 5):
if (df[c].value_counts().count() <= 5):
    continue
#discrete_df[c] = pd.cut(df[c], bins=5, right=False, labels=False)
discrete_df[c] = pd.qcut(df[c], q=5, labels=False, duplicates='drop')

# 拿出数据
all_y = discrete_df['blueWins'].values # 所有标签数据
feature_names = discrete_df.columns[1:] # 所有特征的名称
all_x = discrete_df[feature_names].values # 所有原始特征值，pandas的DataFrame.values取出为numpy的array矩阵

x = top_df['score'].values  # 综合得分列表
y = top_df.index.values  # 学校名称列表

```

# scipy.stats

```
from scipy.stats import norm, cauchy
```

# pyplot

```
import matplotlib.pyplot as plt
```

# seaborn

That is, it uses Matplotlib “under the hood”, but it offers the user a much simpler API (set of commands) that enable us to generate a variety of great-looking plots that are particularly useful in data science. 

```
import seaborn as sns  # 作图

sns.set_theme()

sns.barplot(x=x, y=y, orient='h', palette="Blues_d")  # 画条形图
plt.xlim(75, 101)  # 限制 x 轴范围
plt.show()

sns.pairplot(data_df[feature_cols + ['score']], height=3, diag_kind="kde")
plt.show()

sns.heatmap(f, annot=True, cmap=plt.get_cmap('binary'))
plt.show()

sns.regplot(data_df['quality_of_faculty'], data_df['score'], marker="+")
plt.show()
```

# sklearn

```
from sklearn.model_selection import train_test_split, cross_validate # 划分数据集函数

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer # 提取文本特征向量的类, 其中TfidfVectorizer可能等价于：CountVectorizer + TfidTransformer
from scipy.sparse import hstack
x_train = hstack([x_train_text, x_train_h1 * f_repeat]) # 拼接稀疏向量，也可在此对特征加权

from sklearn.preprocessing import MinMaxScaler # normalizing

from sklearn.metrics import accuracy_score, precision_score, recall_score # 准确率函数
from sklearn.metrics import mean_squared_error, r2_score

from sklearn import linear_model
from sklearn.naive_bayes import MultinomialNB, BernoulliNB, ComplementNB # 三种朴素贝叶斯算法，差别在于估计p(x|y)的方式

from sklearn.preprocessing import LabelBinarizer    # one-hot

import sklearn.cluster as skclst


# 划分训练集和测试集

x_train, x_test, y_train, y_test = train_test_split(all_x, all_y, test_size=0.2, random_state=RANDOM_SEED)
all_y.shape, all_x.shape, x_train.shape, x_test.shape, y_train.shape, y_test.shape # 输出数据行列信息

# accuracy_score
test_acc = accuracy_score(p_test, y_test) # 将测试预测值与测试集标签对比获得准确率
# print('accuracy: {:.4f}'.format(test_acc)) # 输出准确率

# 交叉验证: 需要有 fit / predict / get_params / set_params 方法

cv_result = skms.cross_validate(NB, X_train_vec, y_train_binary, scoring=("accuracy", "precision", "recall"), cv=5) # 5折交叉验证   

# 多个参数网格化搜索最优

sklearn.model_selection.GridSearchCV

```