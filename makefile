install:
	pip install -r requirements.txt

test:
	pytest

run:
	python file_processor.py
clean:
	rm -f file1.txt file2.txt two_files.txt combination.txt