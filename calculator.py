def add(first_item, second_item):
    return first_item + second_item


def subtract(first_item, second_item):
    return first_item - second_item


print(add(4, 6))
print(subtract(9, 8))

# pip install flake8 pytest pytest-cov
# pip freeze > requirements.txt
# To check the alignment we can run the flake8 --statistics
# python -m pytest -v --cov .

# .yaml file uses the serialization language called YAML designed to be pretty human readable

# Docker is like minimal container which contians all the resources which can be required to run the code
