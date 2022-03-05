import venv, sys, shutil, os
from subprocess import run
from contextlib import redirect_stderr, redirect_stdout


def create_venv(directory: str):
    venv.create(directory, with_pip=True)


def install_figlet(venv_directory: str):
    with open('/tmp/help.txt', 'w') as std_out:
        run([f'{venv_directory}/bin/pip', 'install', 'pyfiglet'], stdout=std_out)
    os.remove('/tmp/help.txt')


def run_figdate(venv_directory: str, args: list):
    run([f'{venv_directory}/bin/python3', '-m', 'figdate'] + args)


if __name__ == '__main__':
    venv_dir = '/tmp/venv_02_pushpip'
    create_venv(venv_dir)
    install_figlet(venv_dir)
    run_figdate(venv_dir, sys.argv[1:])
    shutil.rmtree(venv_dir)