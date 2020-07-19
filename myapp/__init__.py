ENV = {
    'secret_yaml_path': ''
}


def config(secret_yaml_path):
    ENV['secret_yaml_path'] = secret_yaml_path


def get_env(key):
    return ENV[key]