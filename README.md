# python-tutorials

## Create new Conda env
conda create --n python-tutorials python=3.6

## Activate env
source activate python-tutorials

## install new package (via pip)
pip install package-name

## create/update requirements file
conda list --export > requirements.txt

http://conda.pydata.org/docs/_downloads/conda-pip-virtualenv-translator.html

## Enable conda envs in jupyter (run from env)
conda install jupyter  # if not installed already
conda install nb_conda
conda install ipykernel
python -m ipykernel install --user --name python-tutorials

## Launch jupyter (run from env)
jupyter notebook


pip freeze > requirements.txt

pip install -r requirements.txt
