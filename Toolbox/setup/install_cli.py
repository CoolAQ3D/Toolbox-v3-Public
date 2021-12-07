
import subprocess, os, sys

def check_cli_existence(
  show_installed_message=False
):
  reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
  installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

  if 'Toolbox' not in installed_packages:
    os.system("pip install -e ./Toolbox/setup")
  else:
    if show_installed_message:
      print('Installed')

#print(installed_packages[113])
