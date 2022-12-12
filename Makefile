.PHONY: downloads python_files csv markdown output texts docs other_data all output_outcomes_text

all:
	make python_files
	make output

output:
	make downloads
	rm -rf output
	make csv
	make outcomes_text
	make docs
	make other_data
	mkdir -p output_in_github
	cp -r ./output/* output_in_github


csv:
	python ./python/output_outcomes_csv.py
	python ./python/output_relations.py
	python ./python/output_2016_goals.py


outcomes_text:
	python ./python/output_outcomes_text.py

other_data:
	python ./python/output_other_data.py

docs:
	python ./python/output_docs_data.py


downloads:
	python ./python/download_sheets.py
	python ./python/download_docx.py
	python ./python/download_zip_doc.py

python_files:
	jupyter nbconvert --to python ./src/*.ipynb
	rm -rf python
	mkdir -p python
	cp ./src/*.py python
	cp -r ./src/lib python
	rm ./src/*.py
