# Installation of Python tools
1. npx
npx stands for Node Package eXecute. 
This command-line utility, bundled with npm version 5.2.0 
and above, allows developers to execute Node.js packages directly 
from the npm registry without globally installing them on your system.

https://dev.to/orlikova/understanding-npx-1m4

install:
npm install -g npx

npx makes it easy to install and manage dependencies hosted in npm registry. 
It simplifies the process and provides a better for executables.

$ npx <command> //command: package to be installed

Use cases:
   To execute one-off commands
   To use gist based scripts
   To use different versions of an npm module
   If you don’t have permission to install it globally.
   
2. nv
Tools are Python packages that provide command-line interfaces.

install:
pip install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

3. nu usage
To install multiple Python versions:
uv python install 3.11 3.12

To reinstall uv-managed Python versions, use --reinstall, e.g.:
uv python install --reinstall

To view available and installed Python versions:
uv python list

To upgrade all uv-managed Python versions:
uv python upgrade

create a python project:
uv init --package <name>

add coverage tool to project
uv add --dev coverage

install coveage tool
uv tool install coverage