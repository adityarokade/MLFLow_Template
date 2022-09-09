conda create --prefix ./env python=3.7 -y
source activate ./env
pip install -r requirements.txt
conda env export > conda.yaml

# echo [$(date)]: "START"
# export _VERSION_=3.7
# echo [$(date)]: "creating environment with python ${_VERSION_}"
# conda create --prefix ./env python=${_VERSION_} -y
# echo [$(date)]: "activate environment"
# source activate ./env
# echo [$(date)]: "install requirements"
# pip install -r requirements.txt
# echo [$(date)]: "export conda environment"
# conda env export > conda.yaml
# echo [$(date)]: "END"
