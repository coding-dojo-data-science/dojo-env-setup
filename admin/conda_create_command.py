"""A CLI version of make_conda_create_commands.py"""

import click

@click.command()
@click.option('--os',default='mac-apple',help ="Operating system. Options are ['mac-apple','mac-intel','windows','windows-source']")
@click.option('--reqs', default ='./admin/requirements-py39.txt', help='Requirements File with packages for conda create')
def show_command(os, reqs ):
	"""Construct and display the conda create command using specific requirements file 
	for the specified os.
	
	Args:
		os (str): Operating system. Options are ['mac-apple','mac-intel','windows','windows-source']
	"""
	# lowercase os for easier matching
	os = os.lower()
	
		
	## Start of command (os agnostic)
	command ="conda create -n dojo-env python=3.9 "

	with open(reqs) as f:
		pkgs = f.read()
		
	command+= pkgs.replace('\n',' ')


	## activation and jupyter kernel creation
	activate = "\n\nconda activate dojo-env\n"
	activate+='python -m ipykernel install --user --name dojo-env --display-name "Python (dojo-env)"\n\n'
	

	# Install nbexensions via pip
	pip_reqs = "pip install jupyter_contrib_nbextensions\n"
	pip_reqs += "jupyter contrib nbextension install --user\n\n"



	## Mac with Apple Chip commands
	mac_mchip_command = command + activate + pip_reqs
	mac_mchip_command += "pip install tensorflow-macos\n"
	mac_mchip_command += "pip install tensorflow-metal\n"
	

	## Mac with Intel Processor commands
	mac_intel_command = command + activate + pip_reqs
	mac_intel_command += "pip install tensorflow\n"


	## add windows - conda
	windows_conda_cmd = command + " tensorflow " + activate + pip_reqs
	# print(windows_conda_cmd)


	## add windows -source 
	windows_source_cmd = command + " tensorflow " + activate.replace('conda','source')  + pip_reqs
	# print(windows_source_cmd)
	print('\n')
	if ('mac-apple' in os) | ('mac-m' in os):
		print(mac_mchip_command)
		
	elif ('mac-intel' in os):
		print(mac_intel_command)
	elif ('windows' in os):
		if 'source' in os:
			print(windows_source_cmd)
		else:
			print(windows_conda_cmd)
			
			
if __name__ == "__main__":
	show_command()
	
