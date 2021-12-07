# Toolbox v3

## Installation

Paste this code in main.sh bash file.

```bash
#Download
python main.py

if [[ ! -d Toolbox ]];then
 if [[ ! -d Toolbox-Install ]]; then
  echo 'Downloading Library!!!'
  git clone https://github.com/CoolAQ3D/Toolbox-v3-Public Toolbox-Install

  cd Toolbox-Install
  mv .git Toolbox
  mv Toolbox ..
  #echo $PWD
  cd ..
  rm -rf Toolbox-Install
  fi
else
  git pull | grep -v 'Already up to date.'
  echo 'Your Library is up to date!'
fi


