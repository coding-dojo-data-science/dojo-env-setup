# Notes on Making Environment .ymls
- Environment Filenames:
	- `environment_m1.yml`: M1 Macs
	- `environment_windows.yml`: Windows
	- `environment_mac_intel.yml`: COMING! Macs without apple silicon chips

## For M1/M2/etc Macs
- M1 macs will be using miniforge instead of anaconda.
- Enviornment File: `environment_mac_mchip.yml`
- YML File needs:
	- channels:
  		- conda-forge
  		- defaults
  		- apple
		
	- Conda Packages:
		- apple::tensorflow-deps
		- conda-forge::sktime
		- lightgbm
		- python-graphviz
		
	- Pip Packages:
		- tensorflow-macos
    	- tensorflow-metal
		- pystan (BEFORE prohpet)
		- prohpet
		- xgboost
		
## For Windows:
- Windows uses actual Anaconda insteadof miniforge.
- Enviornment File: `environment_windows.yml`
- YML File needs:
	- channels:
		- conda-forge
		- defaults
	
	- Conda Packages:
		-  for pystan/prohpet:
			- conda-forge::libpython  #for pystan #msys2::
			- conda-forge::m2w64-toolchain # for pystan #msys2::
				- SEE: https://pystan2.readthedocs.io/en/latest/windows.html for additional requirements if issues
			- conda-forge::pystan
			- conda-forge::prophet
		
	- Pip Packages:
		- tensorflow
		
## For Intel-Processor Macs:
- Use actual Anaconda instead of miniforge.
- Enviornment File: `environment_mac_intel.yml`
- channels:
	- conda-forge
	- defaults
- Conda Packages:
	- conda-forge::sktime
	- lightgbm
	- python-graphviz
- Pip Packages:
	- tensorflow

# CHANGELOG
- 07/01/22: 
	- on m1 mac, jupyter lab was not successfully installed. Testing new m1 environment (first)
		- replaced the "jupyter" dependency to:
			- conda-forge::notebook
			- conda-forge::jupyterlab
- 06/30/22 Windows Update:
	- Ran into issue on windows pc. Removed charset-normalizer install and removed pystan version which seems to have fixed it.
	- All packages that were missing version #'s have been filled in with the version that were installed with the current env.
		- Exceptions:
			- tensorflow
			- jupyter
			- bs4
			- m2w64-toolchain
	- Additions:
		- Added jupyter-contrib-nbextensions and the configurator to simplify extension installation.
	


- 06/30/22:
	- After troubleshooting a Windows PC that failed to install the pip packages, I have added requirements.txt files for each of the OS. The idea is that if the pip installs fail for someone, they can try running, for windows: `pip install -r requirements_windows.txt` 
		- Pmdarima may be the source of the problem.
	- Added numpy as an explicit conda-forge requiremnet v 1.22.4
	- Added nbdime 
	- **KNOWN ISSUES:**
		- On MacOS with an MChip, using prophet's model.fit causes an error about missing file. 
			- Will test on windows and see if same error.
			- May be a pystan related problem.
	
- 06/22/22:
	- Added pandas-datareader
	- Removed notebook from all envs (causes plot_tree warning)
	- ~~Changed sktime to sktime-all-extras~~
	- Changed `conda-forge::jupyterlab` to `jupyter`
	- Added explicit versions for almost all packages.
		- Exceptions:
			- kaggle
			- sktime-all-extras
			- jupyter
			- pandas-profiling
			- python-grapghviz (mchip mac)
			- prophet
			- tensorflow-macos (mchip mac)
			- tensorflow-metal (mchip mac)
			- tensorflow_datasets (mchip mac)
- 06/21/22:
	- Created intel-processor mac environment to test.
	- Renamed m1 mac environment to `environment_mac_mchip.yml`
	- Renamed EnvironmentTester-py38.ipynb to EnvironmentTester-mac.ipynb
- 06/16/22-06/17/22:
	- For m1 environment (on testing branch):
		- Moved Matplotlib from a pip install to a conda install and downgraded below 3.5 for compatibility with SHAP & yellowbrick
		- explicitly used conda-forge for shap install
		- Added packages:
			- nltk
			- jupyterlab
			- pandas-profiling
			- sktime
			- dython
			- pystan + prophet
			- xgboost
			- lightgbm
			- python-graphviz 
				- mac only
				- Windows computer will need to download and run the .exe installer from: https://graphviz.org/download/
			- yellowbrick
		- Changed Versions:
			- plotly from 5.8.0 to 5.8.2
			- matplotlib from 3.5+ to 3.4.3 (compatibility with shap and yellowbrick)
		
