rm -rf source/*.rst
sphinx-apidoc -o ./source ../saker
make html
