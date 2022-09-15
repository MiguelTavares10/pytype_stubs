pyenv install -s -v 3.8.13
pyenv local 3.8.13

PPATH=`pyenv which python`
rm -rf python3.8
ln -s $PPATH python3.8
chmod +x python3.8
PATH=$PATH:`pwd`

if [ ! -d "pytype" ] 
then
    git clone https://github.com/MiguelTavares10/pytype
fi

PYTHONPATH=$PYTHONPATH:`pwd`/pytype

python3.8 -m pip install pytest
python3.8 -m pip install -r pytype/requirements.txt



mkdir -p .pytype/pyi

python3.8 -m pytype.single \
	--imports_info .import_info \
	--module-name ex \
	--platform darwin \
	-V 3.8 \
	-o .pytype/pyi/ex.pyi \
	--analyze-annotated \
	--nofail \
	--quick \
	ex.py