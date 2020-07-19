import os


def read():
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sample.yml')) as f:
        return f.read()


if __name__ == '__main__':
    print(read())