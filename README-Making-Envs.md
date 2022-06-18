# Notes on Making Environment .ymls
- Environment Filenames:
	- `environment_m1.yml`: M1 Macs
	- `environment_windows.yml`: Windows
	- `environment_mac_intel.yml`: COMING! Macs without apple silicon chips

## For M1 Mac
- M1 macs will be using miniforge instead of anaconda.
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
		


# CHANGELOG
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
		
NOTE: testing changing mac prophet to conda 