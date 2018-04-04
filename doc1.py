#! /usr/bin/python3
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
dataset=pd.read_csv('/usr/local/lib/python3.5/dist-packages/sklearn/datasets/data/iris.csv')

plt.style.use('ggplot')

print(dataset)
