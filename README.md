# python-tutorials

## Create new Conda env from requirements file
conda create --name python-tutorials --file requirements.txt

## Create new Conda env
conda create --name python-environment

source activate python-tutorials

## install new package (via conda)
conda install package-name

## install new package (via pip - if not available in conda)
conda install pip

pip install package-name

## create/update requirements file
conda list --export > requirements.txt

http://conda.pydata.org/docs/_downloads/conda-pip-virtualenv-translator.html