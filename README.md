# pytype_stubs


This folder should be in the same directory than pytype:

My pytype Version (this repo should work with default pytype):
https://github.com/MiguelTavares10/pytype

https://github.com/MiguelTavares10/pytype

add pytype to pythonPath
export PYTHONPATH=$PYTHONPATH:PYTHONPATHTOBEADDED


Run ex.py file (you need to change directories)
python3 -m pytype.single --imports_info /home/aluno-di/pytype_stubs/.import_info --module-name ex --platform darwin -V 3.8 -o /home/aluno-di/pytype_stubs/.pytype/pyi/ex.pyi --analyze-annotated --nofail --quick /home/aluno-di/pytype_stubs/ex.py
