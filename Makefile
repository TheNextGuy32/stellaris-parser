# $(BUCKET_NAME) is an environment variable pointing to the bucket name storing the stuff. It's encrypted for security.

init:
	pip install -r requirements.txt

upload: init
	python ./stellaris_parser/aws_tools/upload.py game_files/ $(BUCKET_NAME) ./

download: init
	python ./stellaris_parser/aws_tools/download.py game_files/ $(BUCKET_NAME)