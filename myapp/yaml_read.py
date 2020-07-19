import os
from myapp import get_env


def read():
    with open(get_env('secret_yaml_path')) as f:
        return f.read()


if __name__ == '__main__':
    from myapp import config

    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sample.yml')
    config(path)
    print(read())
