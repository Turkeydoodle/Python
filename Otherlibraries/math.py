import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
dataframe = pd.read_csv("https://raw.githubusercontent.com/cwkteacher/Data/master/athletes.csv")
dataframe["height"].fillna(0, inplace=True)
dataframe['bronze'].fillna(0, inplace=True)
plt.scatter(dataframe["height"], dataframe["bronze"])
plt.title('Height Bronze Medal Winners')
plt.xlabel('Height')
plt.ylabel('Bronze Medals')
plt.grid(True)
plt.show()