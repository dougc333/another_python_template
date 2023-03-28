
.PHONY: src test lib data

install:
	#install with pip
	pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
format:
	#format with black
	@echo $(CURDIR)
	black *.py src/test.py lib/logic.py 
lint:
	#flake8 or pylint
	pylint --disable=R,C src/*.py lib/*.py *.py
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



