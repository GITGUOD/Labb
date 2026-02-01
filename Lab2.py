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
        data = pd.read_csv(file, names=['user', 'contributions'])

        counts = data["user"].value_counts()

        top_n = counts.head(n)

        plt.bar(top_n.index, top_n.values)

        plt.ylabel('Nbr of Contributions')
        plt.xlabel('Contributors')
        plt.show()

    # GPT code below
    def contributors1(file, n):

        data = pd.read_csv(
            file,
            sep="|",
            names=["rev", "user", "datetime", "info"]
        )

        # rensa mellanslag
        data["user"] = data["user"].str.strip()

        # plocka bara själva datumet (utan +0200 osv)
        data["datetime"] = data["datetime"].str.strip().str[:19]

        # gör till datetime
        data["datetime"] = pd.to_datetime(data["datetime"])

        # räkna commits per user
        counts = data["user"].value_counts()

        top_n = counts.head(n)

        # stapeldiagram
        plt.bar(top_n.index, top_n.values)

        plt.xlabel("Contributors")
        plt.ylabel("Number of contributions")
        plt.title(f"Top {n} contributors")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # senaste aktivitet per user
        latest = data.groupby("user")["datetime"].max().sort_values()

        return latest










