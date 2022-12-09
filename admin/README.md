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
conda env export -f  environemnt_mac_mchip.yml --no-builds  
```

### 5. Remove manually created env and rebuild
- Remove the manually created env:
```bash
conda activate base
conda remove --name dojo-env --all  

conda env create -f environemnt_mac_mchip.yml
conda activate dojo-env
python -m ipykernel install --user --name dojo-env --display-name "Python (dojo-env)"
```
___

# Reference

## Terminal Commands

### Remove env
```bash
conda activate base
conda remove --name dojo-env --all  
```
- Respond: y



### Install Commands (for my macbook computer)
```bash
cd $HOME/Documents/GitHub/_CURRICULUM/dojo-env-setup
conda env create -f environment_py39_mac_mchip.yml
conda activate dojo-env
python -m ipykernel install --user --name dojo-env --display-name "Python (dojo-env)"
```