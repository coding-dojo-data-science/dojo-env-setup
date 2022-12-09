import os
command ="conda create -n dojo-env python=3.9 "

with open('./admin/requirements-py39.txt') as f:
	pkgs = f.read()
	
command+= pkgs.replace('\n',' ')



activate = """\n\nconda activate dojo-env
python -m ipykernel install --user --name dojo-env --display-name "Python (dojo-env)"\n\n
"""

pip_reqs = """pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user\n\n
"""

## Add Mac-M1
mac_command = command + activate + pip_reqs
mac_command += "pip install tensorflow-macos\n"
mac_command += "pip install tensorflow-metal\n"
# print("\n\n"+mac_command)

## Add Mac-intel
mac_intel_command = command + activate + pip_reqs
mac_intel_command += "pip install tensorflow"
print("\n\n"+mac_intel_command)


## add windows - conda
windows_conda_cmd = command + " tensorflow " + activate + pip_reqs
# print(windows_conda_cmd)


## add windows -source 
windows_source_cmd = command + " tensorflow " + activate.replace('conda','source')  + pip_reqs
# print(windows_source_cmd)