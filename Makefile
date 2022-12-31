.PHONY: python_files output downloads tables outcomes definitions 2016_goals relations docs all

export OUTPUT_LANG := ja
export OUTPUT_DOCS := 0

all:
	make python_files
	make downloads
	rm -rf output
	make output
	mkdir -p output_in_github
	cp -r ./output/* output_in_github

output:
	make python_files
	make tables
	make outcomes
	make definitions
	make 2016_goals
	if [ ${OUTPUT_DOCS} -ge 1 ]; then make docs ;fi
	make relations

outcomes:
	python ./python/output_outcomes.py

2016_goals:
	python ./python/output_2016_goals.py

relations:
	python ./python/output_relations.py

tables:
	python ./python/output_tables.py


definitions:
	python ./python/output_definitions.py

docs:
	python ./python/output_docs.py

downloads:
	python ./python/download_sheets.py
	python ./python/download_zip_doc.py

python_files:
	jupyter nbconvert --to python ./src/*.ipynb
	rm -rf python
	mkdir -p python
	cp ./src/*.py python
	cp -r ./src/lib python
	rm ./src/*.py
