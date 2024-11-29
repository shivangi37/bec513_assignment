# bec-513_assignment

**Question 1]** Here there are two input files. First we pulled the lines with matching pattern from one file(data1.tsv.gz)and using the script file(sort.py) give it as a input. In sort.py we extract lines having matching pattern with target.tsv
Command used for execution: zless data1.tsv.gz | awk 'NR==1||/ENSG/' | python sort.py data/target.tsv final.tsv

**Question 2]** Here the data file data2.tsv is used and target is to generate line plot based on catogories. The ggplot library is used and plot generated using R script.

Command used for execution: cat data2.tsv | Rscript plot.R "clusters.png" "Relative from center [bp]" "Enrichment over Mean" "MNase fragment profile".

**Question 4]** Here the numeric dataset was divided into quantiles and each data point was labelled according to its quantile. Python script(quantiles.py) is executed on dataset to achieve the output.
Command used for execution:cat hundred_numbers.tsv | python quantiles.py 4

**Question 5]**The target is to generate heatmap of big data file given(not uploaded).The first column from big file is dropped and stored in a file- drpped_data.tsv(not uploaded) then using python script heatmap is obtained.

Commands used for execution: zcat big_data.tsv.gz | cut --complement -f1 > dropped_data.tsv

python heat_map.py
