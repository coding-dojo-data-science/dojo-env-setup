# Admin: Constructing dojo-env
- Workflow as of 12/09/22

## Summary
- NOTE: steps below must be repeated on a windows AND mac computer to generate each env

1. Manually create a new conda environment using a (mostly verison-less) list of packages. 
2. Confirm the environment works with the env tester notebook
3. Export env to .yml without build information.
4. Remove your manually created env
5. Use the environment.yml file to construct the env again
6. Test the env with tester notebook
7. If it works, then the file is all set for deployment.



## Workflow 

### 1. Update files
- First, update the `admin/requirements-py39.txt` with the list of packages for the conda create command (created using .py below)
- Use `make_conda_create_commands.py` to help construct the same commands on mac and windows.
	- Comment out lines for printing any OS besides the one you are using.

### 2. Run `python admin/make_conda_create_commands.py`
- Paste the commands into terminal and wait for installations.

### 3. Boot up jupyter, test and confirm
- Run the environment testing notebook for your OS.
- If it works, then export for students:


### 4. Export Env

- Example for Mac:
```bash
conda env export -f  environment_mac_mchip.yml --no-builds  
```


- Example for Windows:
```bash
conda env export -f  environment_windows.yml --no-builds  
```

### 5. Remove manually created env and rebuild
- Remove the manually created env:

##### MAC
```bash
conda activate base
conda remove --name dojo-env --all  

conda env create -f environment_mac_mchip.yml
conda activate dojo-env
python -m ipykernel install --user --name dojo-env --display-name "Python (dojo-env)"
```

##### WINDOWS
```bash
conda activate base
conda remove --name dojo-env --all  

conda env create -f environment_windows.yml
conda activate dojo-env
python -m ipykernel install --user --name dojo-env --display-name "Python (dojo-env)"
```
___

# Reference

## Terminal Commands



### Installation Commands 

#### Macs with Apple Chip

```bash
conda env create -f environment_mac_mchip.yml
conda activate dojo-env
python -m ipykernel install --user --name dojo-env --display-name "Python (dojo-env)"
```

#### Macs with Intel Processor
```bash
conda env create -f environment_mac_intel.yml
conda activate dojo-env
python -m ipykernel install --user --name dojo-env --display-name "Python (dojo-env)"
```


#### Macs with Intel Processor
```bash
conda env create -f environment_mac_intel.yml
conda activate dojo-env
python -m ipykernel install --user --name dojo-env --display-name "Python (dojo-env)"
```

## Remove env
```bash
conda activate base
conda remove --name dojo-env --all  
```
- Respond: y


## Clone Environment

- To create a clone of dojo-env called "my-env":
```bash
conda create --name my-env --clone dojo-env
python -m ipykernel install --user --name my-env --display-name "Python (my-env)"
```

___
___

# OLD ENV CREATION WORKFLOW/NOTES:

## Notes on Making Environment .ymls
- Environment Filenames:
	- `environment_m1.yml`: M1 Macs
	- `environment_windows.yml`: Windows
	- `environment_mac_intel.yml`: COMING! Macs without apple silicon chips

### For M1/M2/etc Macs
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
		
### For Windows:
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
		
### For Intel-Processor Macs:
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

## CHANGELOG
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
		
