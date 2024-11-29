import pandas as pd
import sys

num_quantiles = int(sys.argv[1])

numbers = [float(line.strip()) for line in sys.stdin]


dataframe = pd.DataFrame(numbers, columns=["Value"])

dataframe["Quantile_Label"], bins = pd.qcut(dataframe["Value"], q=num_quantiles, labels=[f"q{i+1}" for i in range(num_quantiles)], retbins=True)
dataframe["Quantile_Interval"] = pd.cut(dataframe["Value"], bins=bins)

for _, row in dataframe.iterrows():
    print(f"{row['Value']}\t{row['Quantile_Label']}\t{row['Quantile_Label']} {row['Quantile_Interval']}")

