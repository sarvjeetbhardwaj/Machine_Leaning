import seaborn as sns
import matplotlib.pyplot as plt

class statistical_analysis():

    def __init__(self,data):
        self.data = data
        sns.countplot(data=self.data , x=60)
        plt.xlabel('R = Rock , M = Mine')
        plt.ylabel('Count of Rock/Mine')
        plt.show()

        print('Value counts of the Output feature')
        print('\n')
        print(self.data[60].value_counts())

        sns.boxplot(data=self.data)
        plt.xlabel('Column Names')
        plt.xticks(rotation=90)
        plt.ylabel('Distribution of data')
        plt.show()

        print('Staistical Distribution of Data')
        print('\n')
        print(self.data.describe())

        print('Distribution of the number of null values in all features')
        print('\n')
        print(self.data.isnull().sum())

        self.data.isnull().sum().plot()
        plt.xlabel('Features')
        plt.ylabel('Count of Null values')
        plt.title('Distribution of the number of null values in all features')
        plt.show()

        #sns.pairplot(data=data,hue=60)
        #plt.show()

        print(f'Correlation statistics ::\n{data.corr()}')
        sns.heatmap(data.corr())
        plt.show()

        print(self.data.groupby(60).mean())



    