# python-tutorials

## Create new Conda env
conda create --name python-tutorials python=3.5

## Activate env
source activate python-tutorials

## install new package (via pip)
pip install package-name

## create/update requirements file
conda list --export > requirements.txt

http://conda.pydata.org/docs/_downloads/conda-pip-virtualenv-translator.html

## Enable conda envs in jupyter (run from env)
conda install -c conda-forge nb_conda

## Launch jupyter (run from env)
jupyter notebook


pip freeze > requirements.txt

pip install -r requirements.txt