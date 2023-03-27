
.PHONY: src test lib data

install:
	#install with pip
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
all:
	#install lint test deploy



