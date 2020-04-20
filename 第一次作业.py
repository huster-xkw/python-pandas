import pandas as pd
import numpy as np
```
五、问题与练习
 1. 问题
 【问题一】 Series和DataFrame有哪些常见属性和方法？
 【问题二】 value_counts会统计缺失值吗？
 【问题三】 与idxmax和nlargest功能相反的是哪两组函数？
 【问题四】 在常用函数一节中，由于一些函数的功能比较简单，因此没有列入，现在将它们列在下面，请分别说明它们的用途并尝试使用。
 sum/mean/median/mad/min/max/abs/std/var/quantile/cummax/cumsum/cumprod
 【问题五】 df.mean(axis=1)是什么意思？它与df.mean()的结果一样吗？第一问提到的函数也有axis参数吗？怎么使用？
 ## 问题一
Series：

属性：index,value,name,dtype

方法：['']取值，mean平均值，var方差，count，等等list有的他都有

DataFrame：

属性：列名，序号（行名），value,shape

方法：[]取值，rename重命名，drop,pop,等删除方法，[]直接加，assign加，等等

## 问题二
会

## 问题三
idxmin,nsmallest

## 问题四
求和/求平均/中位数/根据平均值求绝对平均距离差/最大/最小/绝对值/标准差/方差/四分位数/前--多少个最大的数/前多少个数的和/前多少个数的积

## 问题五
这个是求每一行的平均值。返回的结果不同。有，直接加在后面。

axis = 0：沿着垂直方向进行操作，也就是沿着每一列进行相应的函数操作

axis = 1：沿着水平方向进行操作，也就是沿着每一行进行相应的函数操作
 ```
 
 ```
 ### 2. 练习
#### 【练习一】 现有一份关于美剧《权力的游戏》剧本的数据集，请解决以下问题：
#### （a）在所有的数据中，一共出现了多少人物？
#### （b）以单元格计数（即简单把一个单元格视作一句），谁说了最多的话？
#### （c）以单词计数，谁说了最多的单词？
```
data = pd.read_csv('data/Game_of_Thrones_Script.csv')
print(data['Name'].nunique())
data = data.assign(Words=data['Sentence'].apply(lambda x:len(x.split()))).sort_values(by='Name')
print(data)
N_words = list(zip(data['Name'],data['Words']))
L_count=[]
for i in N_words:
    if i == N_words[0]:
        L_count.append(i[1])
        last = i[0]
    else:
        L_count.append(L_count[-1]+i[1] if i[0] == last else i[1])
        last = i[0]
data['count'] = L_count
print(data['Name'][data['count'].idxmax()])
df = pd.read_csv('data/Kobe_data.csv',index_col='shot_id')
#index_col的作用是将某一列作为行索引
print(pd.Series(list(zip(data['action_type'],data['combined_shot_type']))).value_counts().index[0])
print(pd.Series(list(list(zip(*(pd.Series(list(zip(df['game_id'],df['opponent']))).unique().tolist())))[1])).value_counts().index[0])
 
