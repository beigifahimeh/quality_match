.PHONY: test install setup pre-commit clean

SRC_DIR = quality_match

pre-commit: 
	pre-commit run --all-files

test:
	pytest $(SRC_DIR) -v

install:
	pip install -r requirements.dev.txt
	pip install -e .

setup:
	(\
		echo "> Creating venv"; \
		python -m venv .venv; \
		source .venv/bin/activate; \
		echo "> Installing dev requirements"; \
		pip install -r requirements.dev.txt; \
		echo "> Installing local package in editable mode"; \
		pip install -e .; \
		echo "> Making venv available in jupyter notebooks"; \
		python -m ipykernel install --name=$(SRC_DIR); \
		jupyter kernelspec list; \
		echo "> Installing pre-commit"; \
		pre-commit install; \
	)

clean:
	echo "> Removing virtual environment"
	rm -r .venv	