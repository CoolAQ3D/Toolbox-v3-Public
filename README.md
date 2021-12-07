# Toolbox v2

## Note Done Yet!
Just for fun. Quick access to new features.

## Installation

Paste this code in main.sh bash file.

```bash
#Download

if [[ ! -d Test-1 ]]; then
  echo 'Downloading Library!!!'
  git clone https://github.com/CoolAQ3D/Toolbox-v3-Public

#Remove This part for stopping auto updates.
else
  cd Test-1
  git pull | grep -v 'Already up to date.'
  echo 'Latest Update v2'

fi

