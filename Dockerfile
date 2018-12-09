# Docker file for Top_Predictors_for_Great_Wine
# Ayla Pearson and Richie Zitomer Dec, 2018

# use rocker/tidyverse as the base image
FROM rocker/tidyverse

# Install additional R packages
RUN Rscript -e "install.packages('rmarkdown')"
RUN Rscript -e "install.packages('knitr')"

# Install Python
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN apt-get install -y python3-tk

# Install necessary Python packages
RUN pip3 install numpy
RUN pip3 install argparse
RUN pip3 install pandas
RUN pip3 install scikit-learn
RUN apt-get install -y graphviz && pip install graphviz
RUN apt-get update && \
    pip3 install matplotlib && \
    rm -rf /var/lib/apt/lists/*
