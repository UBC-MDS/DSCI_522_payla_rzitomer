# Driver Script
# Richie Zitomer and Ayla Pearson, Nov 2018

# This driver script opens the zip file,
# cleans the data, creates EDA visualizations,
# generates the model, generates results figures
# and creates the knit final report.

# run all analysis
all: doc/docs/results.md

data/wine_data_cleaned.csv : data/winemag-data-130k-v2.csv.zip src/load_data.py
	python src/load_data.py data/winemag-data-130k-v2.csv.zip data/wine_data_cleaned.csv

results/viz_ : data/wine_data_cleaned.csv src/explore_data.py
	python src/explore_data.py data/wine_data_cleaned.csv results/viz_

results/rank.csv : data/wine_data_cleaned.csv src/decision_tree.py
  python src/decision_tree.py data/wine_data_cleaned.csv results/rank.csv

results/results_ : results/rank.csv src/result_plots.py
  python src/result_plots.py results/rank.csv results/results_

docs/results.md : docs/results.Rmd results/viz_ results/results_
  Rscript -e "rmarkdown::render('docs/results.Rmd')"

clean :
  rm -f data/wine_data_cleaned.csv
	rm -f results/viz_
  rm -f results/rank.csv
	rm -f results/results_
	rm -f doc/count_report.md doc/count_report.html
