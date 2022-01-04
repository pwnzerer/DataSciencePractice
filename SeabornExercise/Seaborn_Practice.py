# -*- coding: utf-8 -*-

#importing libraries

import seaborn as sns
import matplotlib.pyplot as plt

#setting default style

sns.set_style('whitegrid')

#training dataset available by default with seaborn

titanic = sns.load_dataset('titanic')

#different plots

sns.jointplot(x='fare',y='age',data=titanic)

sns.displot(titanic['fare'],kde=False,bins=50,color='orange')

sns.boxplot(x='class',y='age',data=titanic)

sns.swarmplot(x='class',y='age',data=titanic)

sns.heatmap(titanic.corr())

plot =  sns.FacetGrid(data=titanic,col='sex')
plot.map(plt.hist ,'age')