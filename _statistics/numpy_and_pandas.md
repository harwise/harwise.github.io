---
layout: default
title: numpy and pandas
---

{% include katex.html %}

# python
```

# ------------------- string

print('accuracy: {:.4f}'.format(test_acc))              # 浮点转字符串
print('accuracy: {:<.4f}'.format(accuracy))

' '.join(text)                                          # join
path.replace('../data', 'data_cut')                     # replace
line.lower()                                            # 大小写

# ------------------- re

re.split("\s+and\s+|\s*,\s*", string)                   # 根据逗号或者and进行分词
CountVectorizer(token_pattern = r"(?u)\b\w[\w\-. ]+\b") # 找出名字；名字中间可能有如下符号："-", "." 以及 空格

# ------------------- zip

a, b = [1, 2]
head, text = [], []
for key, value in zip(region, university_count):
    pass

# ------------------- list/tuple

for i in range(self.num_iter):
    pass

info_names = [c[3:] for c in df.columns if c.startswith('red')]                                      # 取出要作差值的特征名字（除去red前缀）
len(info_names)

current = (cv_acc, max_depth, min_samples_split, impurity_t)                                         # 记录参数和结果
print('better cv_accuracy: {:.4f}, max_depth={}, min_samples_split={}, impurity_t={}'.format(*best)) # 输出准确率和参数

# ------------------- set

set([f_idx]+[f for f in skip_features])

# ------------------- Counter

from collections import Counter
cnt = Counter(data)                                                     # 计数每个值出现的次数
cnt.most_common(1)

# ------------------- 进度条

from tqdm.autonotebook import tqdm
for line in tqdm(lines, leave=False, mininterval=1, desc='read file'):  # 遍历每一行

# ------------------- directory/files

def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r

import struct
magic, n = struct.unpack('>II', lbpath.read(8))
labels = np.fromfile(lbpath, dtype=np.uint8)

# ------------------- datatime

from datetime import datetime
datetime_object = datetime.strptime(t, '%Y-%m-%d %H:%M:%S')

# ------------------- 图像

from PIL import Image
img = Image.open('data/train/0/4-3.jpg')  # 打开图片
img  # 显示图片

```

# ipython
```

display

%%time


```

# numpy

```
import numpy as np

# ------------------- 取得数据

labels = np.fromfile(lbpath, dtype=np.uint8)                            # data from file
np.array(img)                                                           # np.array
all_y = discrete_df['blueWins'].values                                  # 取得dataframe的数据
np.zeros                                                                # 0
np.ones                                                                 # 1
np.arange(len(Y))                                                       # arange

sample_idx = np.random.choice(train_idx, size=len(Y), replace=True)     # 随机取数据
np.random.normal(0, init_std, (self.num_input, self.num_output))        # 正态分布随机数

# ------------------- 查看

all_y.shape

# ------------------- 处理数据

np.array(img).reshape(-1)                                               # reshape 成一行
Yvalues, counts = np.unique(y_train, return_counts=True)                # 不同的值的详细信息

W = [10,1,1,1]
levels[:,] *= W                                                         # 每一列乘以对应的权重
b[np.arange(Y.size), Y] = 1                                             # b[(0, Y_0), (1, Y_1) ... (n, Y_n)] = 1

np.random.shuffle(indices)                                              # shuffle
self.batch_indices = np.split(indices, num_iteration)                   # split

# ------------------- 计算

np.sum
np.max                                                                  # max value in A
np.mean

np.maxmium(A, B)
np.exp
np.log
np.exp2
np.log2

np.dot(GW0.T, GW1)                                                      # (10, 100) dot (100, 784) => (10, 784)
np.sum(GW0.T, axis=1, keepdims=True)                                    # (10, 100) => (10, 1)
wxb_max_class = np.max(wxb, axis=1)                                     # max
wxb_max_class_i = np.argmax(wxb, axis=1)                                # the index of the max

t = t / t.sum(axis=1, keepdims=True)

# --------------------拼接

np.concatenate                            # 沿指定轴拼接，维度不变
np.append                                 # 不指定轴的时候，扁平化之后拼接
np.stack                                  # 增加一个维度，默认增加的是0轴
np.hstack/vstack/dstack                   # 对给定数组的所有元素，进行拼接
np.columen_stack/row_stack                # 整体看作一个二维矩阵。拿出columns之后，组成这些column的数组


```

# scipy

```

# -------------------- 稀疏矩阵

from scipy.sparse import hstack
x_train = hstack([x_train_text, x_train_h1 * f_repeat])                 # 拼接稀疏向量，也可在此对特征加权
scipy.sparse.hstack([train_X, train_df['overall'].values.reshape((-1, 1)) / 5])

# -------------------- stats

from scipy.stats import norm, cauchy

```

# pandas

```
import pandas as pd

# ------------------- 读入数据

data_df = pd.read_csv("data.csv", sep=',')                      # 读入csv文件为pandas的DataFrame
discrete_df = df.copy()                                         # 复制一份数据

# ------------------- 预处理数据

data_df = data_df.drop(columns='gameId')                        # 舍去对局标号列
data_df = data_df.dropna()                                      # 舍去包含 NaN 的 row
data_df = data_df.fillna('')                                    # 填充空值为空字符串

# ------------------- 观察数据

len(data_df)
data_df.info()                                                  # 输出数据大致信息
data_df.head(3).T                                               # 观察前几列并转置方便观察
print(data_df.iloc[0])                                          # 输出第一行数据
data_df.describe()                                              # 每列特征的简单统计信息

pd.set_option('display.max_columns', None)                      # 使得data_df.describe() 输出能够显示所有列


# ------------------- 处理数据

level[1]["f_duration"].sum()                                    # sum
level[1]["f_success"].any()                                     # any
user[1]["f_duration"].max()                                     # max

len(df[c].unique())                                             # 某一列的不同的值的个数
df[c].value_counts().count()                                    # 某一列的不同的值的详细信息

discrete_df[c] = pd.cut(df[c], bins=5, right=False, labels=False)           # 连续值离散化: 等密度区间
discrete_df[c] = pd.qcut(df[c], q=5, labels=False, duplicates='drop')       # 连续值离散化: 等长区间

discrete_df.columns[1:]                                         # 取列名称
top_df.index.values                                             # 取index
hamSamples = X_train_vec[y_train == "ham"]                      # 选取某些行
seq_df.loc[seq_df['level_id'].isin(level_groups[label])]        # 根据条件选取某些行

mean_df = data_df.groupby('institution').mean()                 # 按学校聚合并对聚合的列取平均
top_df = mean_df.sort_values(by='score', ascending=False)       # sort

for label, items in meta_df.groupby("label"):                   # 分组
    # items is a DataFrame.
    pass

f = data_df[feature_cols + ['score']].corr()                    # 相关矩阵

# ------------------- 写数据

result_df = pd.DataFrame()
result_df['Id'] = test_df['Id'].values
result_df['Predicted'] = y_predict
result_df.to_csv('./result.csv', index=False)

```

# pyplot

```
import matplotlib.pyplot as plt
```

# seaborn

That is, it uses Matplotlib “under the hood”, but it offers the user a much simpler API (set of commands) that enable us to generate a variety of great-looking plots that are particularly useful in data science. 

```
import seaborn as sns

sns.set_theme()

# 画条形图
sns.barplot(x=x, y=y, orient='h', palette="Blues_d")
plt.xlim(75, 101)   # 限制 x 轴范围
plt.show()

# 折线图
sns.lineplot(x=sampleCountMean, y=accus_samples_mean)

# 方法观察变量之间的关联关系，可以从图中看到，少部分变量之间有线性关系；各个变量和结果之间，近似对数关系。
sns.pairplot(data_df[feature_cols + ['score']], height=3, diag_kind="kde")
plt.show()

# 用热力图的形式呈现相关度矩阵
f = data_df[feature_cols + ['score']].corr()
sns.heatmap(f, annot=True, cmap=plt.get_cmap('binary'))
plt.show()

# 散点图
sns.scatterplot(x=tsne_x[:,0], y=tsne_x[:,1], hue=all_y, palette="deep") # 散点图
plt.show()

# Regression图
sns.regplot(data_df['quality_of_faculty'], data_df['score'], marker="+")

```

# sklearn

```

# ------------------ 预处理

from sklearn.preprocessing import MinMaxScaler      # normalizing
from sklearn.preprocessing import LabelBinarizer    # one-hot

# ------------------- 划分训练集和测试集/交叉验证/参数调优

from sklearn.model_selection import train_test_split, cross_validate
import sklearn.model_selection.GridSearchCV

# 划分数据集函数
x_train, x_test, y_train, y_test = train_test_split(all_x, all_y, test_size=0.2, random_state=RANDOM_SEED)

# 交叉验证: 需要有 fit / predict / get_params / set_params 方法
cv_result = skms.cross_validate(NB, X_train_vec, y_train_binary, scoring=("accuracy", "precision", "recall"), cv=5) # 5折交叉验证   

# 网格搜索用于找最优参数值
grid_search = GridSearchCV(DT, parameters, scoring='accuracy', cv=5, verbose=100, n_jobs=4) # 传入模型和要遍历的参数
grid_search.fit(x_train, y_train) # 在所有数据上搜索参数

# ------------------ 回归

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.linear_model import LogisticRegression

# RMSE ---- TODO

# ------------------ Bayes

from sklearn.naive_bayes import MultinomialNB, BernoulliNB, ComplementNB # 三种朴素贝叶斯算法，差别在于估计p(x|y)的方式

# ------------------ KNN

from sklearn.neighbors import KNeighborsClassifier

# ------------------ SVM

from sklearn import svm

# ------------------ Cluster

from sklearn.cluster import KMeans, AgglomerativeClustering                     # 聚类方法

# ------------------ ensemble

from sklearn.ensemble import AdaBoostClassifier

# ------------------ 文本向量化

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer    # 提取文本特征向量的类
# TfidfVectorizer可能等价于：CountVectorizer + TfidTransformer

# ------------------ 降维

from sklearn.manifold import TSNE # tSNE降维
from sklearn.decomposition import PCA # PCA

# ------------------ 概率校正

# 使用交叉验证生成器, 并对每个拆分模型参数对训练样本和测试样本的校准进行估计. 然后对折叠预测的概率进行平均.
from sklearn.calibration import CalibratedClassifierCV
clf = CalibratedClassifierCV(clf, cv=2, method='sigmoid')

# ------------------ 评价指标

from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve

test_acc = accuracy_score(p_test, y_test)                                       # 将测试预测值与测试集标签对比获得准确率
roc_auc_score(gournd_truth["Expected"].values, dtc_bagging_score)               # AUC

fpr, tpr, _ = roc_curve(gournd_truth["Expected"].values, dtc_bagging_score)     # ROC
plt.plot(fpr,tpr)
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

```

# nltk

```
import nltk

words = nltk.tokenize.word_tokenize(string)         # 先切词
stemmer = nltk.stem.SnowballStemmer('english')      # 使用nltk词干化工具
words = [stemmer.stem(w) for w in words]            # 对每个词词干化
# lemma = nltk.wordnet.WordNetLemmatizer()          # 这里也可以做lemma，但是lemma要求变换后的词也是有意义的所以更严格
# words = [lemma.lemmatize(w).lower() for w in words] 
stopwords = nltk.corpus.stopwords.words('english')  # 使用nltk的停用词
words = [w for w in words if w not in stopwords]    # 去除停用词

```