# Notes on Making Environment .ymls

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
		
	- Pip Packages:
		- tensorflow-macos
    	- tensorflow-metal
		- prohpet
		- xgboost