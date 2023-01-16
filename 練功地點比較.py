import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 資料引入
df = pd.read_excel("天堂w_練功.xlsx", sheet_name="66")
# print('原本的樣子:\n', df,'\n')

# 資料清洗
df1 = df.iloc[:,0:4]
# print('iloc 取前面5個 col:\n', df1,'\n')
# df3 = df1.dropna(how='all')      
# print('dropna 空格的資料\n', df3,'\n')
df2 = df1.dropna(how='any')
# print('dropna 空格的資料\n', df2,'\n')


col_names = ['等級', '地點']
summeries = {'經驗值': 'mean', '錢': 'mean'}
df3 = df2.groupby(by=col_names).agg(summeries).reset_index()
# print('groupby排序/計算後:\n', df3,'\n')



# 製圖
level = df3["等級"]
spot = df3["地點"].astype(str)
ex = df3["經驗值"]
money = df3["錢"]


plt.figure(figsize=(16,8))
plt.bar(spot, ex)
plt.yticks(np.arange(0, 1, 0.05))
plt.grid()
plt.legend()


#上標籤 未解決 用text 但似乎有series 資料型態有問題

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

plt.title("66等妖精練功地點效率圖")
plt.show()