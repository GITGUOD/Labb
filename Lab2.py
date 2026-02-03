import pandas as pd
import matplotlib.pyplot as plt
class Second_Lab:
    # Exercise: filter not completed cases:

    def removeNA(data):
        data = data.dropna()
        return data
    
    def analyzePotentialOutliers(data, threshold):
        '''
        AnalyzePotentialOutliers
        
        :param data: DataFrame to analyze according to earlier analysis
        :param threshold: Vector with threshold values for each variable/column

        '''

        results_list = []

        for col, limit in threshold.items():

            rawData = data[col]

            outliers = rawData[rawData > limit]

            number_Of_Outliers = len(outliers)

            mean_Value_Of_Non_Outliers = rawData[rawData <= limit].mean()

            results = {
                "variable": col,
                "number_of_outliers": number_Of_Outliers,
                "mean_value_of_non_outliers": mean_Value_Of_Non_Outliers
            }

            results_list.append(results)
            df_results = pd.DataFrame(results_list)

            df_results = df_results.set_index("variable")

        return df_results
    
    def contributors(file, n):
        data = pd.read_csv(
            file,
            sep="|",
            names=["rev", "user", "datetime", "commitments"]
        )
        counts = data["user"].value_counts()

        top_n = counts.head(n)

        plt.bar(top_n.index, top_n.values)

        plt.ylabel('Nbr of Contributions')
        plt.xlabel('Contributors')
        plt.xticks(rotation=90) # rotera x-axelns etiketter precis som uppgiften

        plt.show()

