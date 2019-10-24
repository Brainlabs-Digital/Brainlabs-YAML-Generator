install:
	pipenv run python setup.py install

run:
	pipenv run blyaml

deploy:
	pipenv run python setup.py bdist_wheel
	pipenv run python -m twine upload --skip-existing dist/*.whl

test:
	pipenv run python -m pytest
