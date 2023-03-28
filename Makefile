
.PHONY: src test lib data

install:
	#install with pip
	pip install --upgrade pip && pip install -r requirements.txt
format:
	#format with black
lint:
	#flake8 or pylint
test:
	#pytest with coverage
build:
	#docker build
run: 
	#run docker command
deploy:
	#deploy to aws ecr or eks
check:
	#check does nothing
distcheck: 
	#distcheck does nothing
all:
	#install lint test deploy



