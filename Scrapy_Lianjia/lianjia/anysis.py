# -*- coding:utf-8 -*-
#V:Python 3.6.3

import pandas as pd
from IPython.display import display
from matplotlib.pylab import plt

data = pd.read_csv('house.csv')
data['total_price'] = data['room_area']*data['unti_price']/10000

#计算南京市的不同区域的二手房的平均房价
data_mean = data.groupby('room_location')['unti_price'].mean()
#统计南京市的不同区域的二手房的数量
data_count = data.groupby('room_location')['unti_price'].count()

# print(data_mean.values)
# print(data_count.index)


#通过柱状图来显示南京市各区域的二手房的平均房价
plt.figure(1,figsize=(10,6))
plt.rc('font',family='SimHei',size=13)
plt.title(u'南京市周围的二手房的平均房价')
plt.xlabel(u'南京的行政区')
plt.ylabel(u'平均房价')
plt.bar(data_mean.index,data_mean.values,color='g')
plt.show()

#统计南京市各个行政区域的二手房的数量

plt.figure(2,figsize=(10,6))
plt.rc('font',family='SimHei',size=13)
plt.title(u'南京市周围的二手房的数量')
plt.xlabel(u'南京的行政区')
plt.ylabel(u'数量')
plt.bar(data_count.index,data_count.values,color='y')
plt.show()

#统计各个行政区域的二手房所占有的比例（饼图）
plt.figure(3,figsize=(10,10))
plt.rc('font',family='SimHei',size=13)
explode = [0]*len(data_count)
explode[7] = 0.1
plt.pie(data_count,radius=2,autopct='%1.f%%',shadow=True,labels=data_mean.index,explode=explode)
plt.axis('equal')
plt.show()