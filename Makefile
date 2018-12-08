# Driver Script
# Richie Zitomer and Ayla Pearson, Nov 2018

# This driver script opens the zip file,
# cleans the data, creates EDA visualizations,
# generates the model, generates results figures
# and creates the knit final report.

# run all analysis
all: docs/results.md

data/wine_data_cleaned.csv results/viz_class_frequencies.png results/describe_variety.csv results/describe_country.csv results/describe_province.csv results/describe_price.csv: data/winemag-data-130k-v2.csv.zip src/load_data.py
	python src/load_data.py data/winemag-data-130k-v2.csv.zip data/wine_data_cleaned.csv results/viz_class_frequencies.png results/describe_

results/viz_countries.png results/viz_price_boxplot.png results/viz_price_less_than_100_hist.png results/viz_variety.png : data/wine_data_cleaned.csv src/explore_data.py
	python src/explore_data.py data/wine_data_cleaned.csv results/viz_

results/model_rank.csv results/model_decision_tree_depth_3.png results/model_depth_decision.png : data/wine_data_cleaned.csv src/decision_tree.py
	python src/decision_tree.py data/wine_data_cleaned.csv results/model_

results/results_rank_plots.csv results/results_top3.csv : results/model_rank.csv src/result_plots.py
	python src/result_plots.py results/model_rank.csv results/results_

docs/results.md : docs/results.Rmd results/viz_countries.png results/viz_price_boxplot.png results/viz_price_less_than_100_hist.png results/viz_variety.png results/model_rank.csv results/model_decision_tree_depth_3.png results/model_depth_decision.png results/results_rank_plots.csv results/results_top3.csv
	Rscript -e "rmarkdown::render('docs/results.Rmd')"

# Delete all files outputted from running the analysis
clean :
	rm -f data/wine_data_cleaned.csv
	rm -f results/describe_*
	rm -f results/viz_*
	rm -f results/model_*
	rm -f results/results_*
	rm -f docs/results.md
	rm -f docs/results.html
