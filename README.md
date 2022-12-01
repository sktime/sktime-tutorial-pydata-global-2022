![](images/team.jpg)

Welcome to the sktime tutorial at PyData Global 2022
====================================================

This tutorial is about [sktime] - a unified framework for machine learning with time series. sktime features various time series algorithms and modular tools for sktime is a widely used scikit-learn compatible library for learning with time series.

`sktime` is easily extensible by anyone, and interoperable with the pydata/numfocus stack.

This `sktime` tutorial explains **basic and advanced sktime pipeline constructs, and the time series transformer** which is the main component in all types of pipelines.

[sktime]: https://sktime.org

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sktime/sktime-tutorial-pydata-global-2022/main)

Also recommended:

:movie_camera: **[general sktime intro tutorial](https://github.com/sktime/sktime-tutorial-pydata-global-2021) from PyData Global 2021**\
:tv: [youtube video of sktime intro at PyData Global 2021](https://www.youtube.com/watch?v=ODspi8-uWgo)

## :rocket: How to get started

In the tutorial, we will move through notebooks section by section.

You have different options how to run the tutorial notebooks:

* Run the notebooks in the cloud on [Binder] - for this you don't have to install anything!
* Run the notebooks on your machine. [Clone] this repository, get [conda], install the required packages (`sktime`, `seaborn`, `jupyter`) in an environment, and open the notebooks with that environment. For detail instructions, see below. For troubleshooting, see sktime's more detailed [installation instructions].
* or, use python venv, and/or an editable install of this repo as a package. Instructions below.

[Binder]: https://mybinder.org/v2/gh/sktime/sktime-tutorial-pydata-global-2022/main?filepath=notebooks
[clone]: https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository
[conda]: https://docs.conda.io/en/latest/
[installation instructions]: https://www.sktime.org/en/latest/installation.html

Please let us know on the pydata slack if you have any issues during the conference, or join the [sktime slack](https://join.slack.com/t/sktime-group/shared_invite/zt-1jphqjpnk-AfxAR8IEfIVkf4By8cT7tQ) to ask for help anytime.

## :bulb: Description

In time series analysis, often multiple, sometimes repetitive, algorithmic steps are applied to the data. Organising these steps in a clear way to enable flexible deployment on multiple data sets and easily reproduce results. Pipelines offer a solution to this challenge by providing a structure to build flexible sequences of applying time series algorithms. The modular building blocks of pipelines are "transformers" or "transformations" (in the scikit-learn sense) as well as estimators specific to learning tasks, such as forecasters or time series classifiers. The challenge in learning with time series are the many different types of transformations, such as:

* transformers of a time series to time series, e.g., differencing and detrending
* transformers of a time series to a row of primitive features/valus in a data frame, e.g., time series summary
* transformers of a time series to a panel of time series, e.g., bootstrap, sliding window
* transformers that apply to hierarchical time series, e.g., reconciliation or hierarchical aggregation
* transformers of a pair of time series to a real number, e.g., time series distances or kernels

sktime provides a framework to distinguish the above, and to use transformers of the various types as components in different types of pipelines, such as:

* forecasting pipelines, with transformers applied to endogeneous, exogeneous, or output data,
* time series classification pipelines, with transformers applied to inputs,
* compositor pipelines for time series distances or parameter estimators,
* specialized reduction steps consuming different types of transformers and machine learning estimators,
* and many more.

The design challenge is to formalize transformers in a way that a given type of transformer can be used in multiple types of pipeline, and creating pipelines that can use multipe types of transformers. sktime solves this challenge through the "scientific type" formalism which applies object orientation based typing to the transformers and inputs/outputs.  The presentation will also briefly touch on advanced pipelining concepts such as graph pipelines and roadmap items inviting contributions.

## :movie_camera: Other Video Tutorials:

- [PyData 2021 - Intro to sktime](https://www.youtube.com/watch?v=ODspi8-uWgo)

- [Pydata 2022 - How to implement your own estimator in sktime](https://www.youtube.com/watch?v=S_3ewcvs_pg)

- [Pydata 2022 - Advanced Forecasting Tutorial](https://www.youtube.com/watch?v=4Rf9euAhjNc)

## :wave: How to contribute

If you're interested in contributing to sktime, you can find out more how to get involved [here](https://www.sktime.org/en/stable/get_involved.html).

Any contributions are welcome, not just code!

## Installation instructions for local use

To run the notebooks locally, you will need:

* a local repository clone
* a python environment with required packages installed

### Cloning the repository

To clone the repository locally:

`git clone https://github.com/sktime/sktime-tutorial-pydata-global-2022.git`

### Using conda env

1. Create a python virtual environment:
`conda create -y -n pydata_sktime python=3.9`
2. Install required packages:
`conda install -y -n pydata_sktime pip sktime seaborn jupyter pmdarima`
3. Activate your environment:
`conda activate pydata_sktime`
4. If using jupyter: make the environment available in jupyter:
`python -m ipykernel install --user --name=pydata_sktime`

### Using python venv

1. Create a python virtual environment:
`python -m venv .venv`
2. Activate your environment:
`source .venv/bin/activate`
3. Install the requirements:
`pip install sktime seaborn jupyter pmdarima`
4. If using jupyter: make the environment available in jupyter:
`python -m ipykernel install --user --name=pydata_sktime`
