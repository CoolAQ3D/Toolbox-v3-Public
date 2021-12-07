
import subprocess, os, sys
import pkg_resources

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

def check_cli_existence(
  show_installed_message=False
):
  reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
  installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

  for package in ['toolbox']:
    try:
        dist = pkg_resources.get_distribution(package)
        print('{} ({}) is installed!'.format(dist.key, dist.version))
    except pkg_resources.DistributionNotFound:
        #print('{} is NOT installed'.format(package))
        print('Installing Toolbox Features!')
        os.system("pip install -e ./Toolbox")

  #print(installed_packages[113]) 