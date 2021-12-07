# Toolbox v3

For Fun, while also learning python, javascript, html, css, etc...
## Installation

_Only supports 2 type of  installtion for now._

### Method #1
Install using pip directly
<br>
`pip install git+https://github.com/CoolAQ3D/Toolbox-v3-Public`

### Method #2
Install using shell command. (Auto Update Supports)
<br>
1: Paste this code in `main.sh` shell file.
<br>
2: Run `main.sh` file.
<br>
3: Import the library using `import Toolbox` in `main.py` file

```bash

#Install Toolbox v3

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
```

## Version
1.0.0


