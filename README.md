# python-tutorials

Using conda envs with pip requirements

## List Conda envs
conda info --envs

## Create new Conda env
conda create --name python-tutorials python=3.6

## Activate env (osx)
source activate python-tutorials

## Activate env (windows, set path to \Anaconda\envs\pyXX\Scripts)
activate python-tutorials

## install new package (via pip)
pip install package-name

## create/update requirements file
pip freeze > requirements.txt

## install from requirements file
pip install -r requirements.txt

## Enable conda envs in jupyter (run from env)
conda install jupyter  # if not installed already

conda install nb_conda

conda install ipykernel

python -m ipykernel install --user --name python-tutorials

## Launch jupyter (run from env)
jupyter notebook

http://conda.pydata.org/docs/_downloads/conda-pip-virtualenv-translator.html