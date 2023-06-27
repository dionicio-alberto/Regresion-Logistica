import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_categorial(df_data: pd.DataFrame,column: str):
    fig = plt.figure(figsize=(10,10))
    sns.countplot(data=df_data, x=column,hue='Churn')
    plt.show()