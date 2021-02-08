requirements:
	@pip install pytest

test:
	@pytest test_main.py

run:
	@python main.py