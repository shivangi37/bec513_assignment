import pandas as pd
import sys

required_file = sys.argv[1] 
filtered_file = sys.argv[2] 

selection_df = pd.read_csv(required_file, names=['Column'])
pattern = set(selection_df['Column'])

with open(filtered_file, 'w') as output:
    for line in sys.stdin:
        if any(term in line for term in pattern):
            output.write(line)

