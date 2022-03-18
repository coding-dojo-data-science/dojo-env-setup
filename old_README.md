# Installing Python Locally

## 1. Required Installations

> Before we install our python environment, we need to take care of a couple requirements. Please make sure to install all of the items listed below before attempting to follow the remaining instructions. 

1. **A Linux-based bash shell/terminal:**
   - Linux users and MacOS users have this built-in to their OS.
       - On MacOS, the shell is called Terminal and can be found in `Applications>Utilities` in Finder
       - OR you can use spotlight search and search for "Terminal".
   
   
   - [ ] **Windows users should install GitBash, instead of using the windows command prompt**
       - Otherwise, all of the commands for working with your terminal will not match the curriculum and other cloud-based platforms (like Amazon Web Services)
      - Download  the Git for Windows Installer: [Git for Windows download](https://gitforwindows.org/)
      - Use the default options.
       
       

        
2. **GitHub Desktop** ([Link](https://desktop.github.com/))
    - [ ] Download the installer and log into the same github account you have been using for your projects. 
    - [ ] After installing, open GitHub desktop:
        1. Open the Preferences menu
            - On Mac: Select `"GitHub Desktop"` on the menu bar and then select `Preferences`.
            - **On Windows: Click on `File` in the menu bar and then select `Options` **
        2. Select the Integrations tab.
        3. Make sure the Shell dropdown menu says Terminal (on Mac) or GitBash (on Windows).
            - If not, select it from the dropdown menu.
        4. Click Save.



3. **Anaconda - individual edition.** [Link](https://www.anaconda.com/products/individual)
    - Anaconda is a data-science-focused python distributable that comes with a convenient GUI program for working with our python environments.
    - Download and run the installer from the link above.
    - Use the default options, EXCEPT when you see the "Advanced Installation Options" window, check BOTH options, like in the screenshot below:
    
    <img src="images/anaconda_check_path.png">
    

    
    
    
    
4. [Windows Users Only] **Ensuring GitBash Can Find Anaconda.**
    - Windows users may need to take an additional step to get anaconda and gitbash working together.
    - **Inside a GitBash window, type `conda` and hit enter.**
        - **If you see a list of available conda commands, great!** You are all set to move on to the "Setting Up Your `dojo-env`" step.
        - **If you see a message that says: "bash: conda: command not found", then follow the instructions below:**
        
    - **Instructions for Adding Conda to GitBash:**
        - Note:the instructions below are adapted from this [Blog Post](https://fmorenovr.medium.com/how-to-add-conda-to-git-bash-windows-21f5e5987f3d)
        1. Once you have installed anaconda, use File Explorer to Open Your **User** folder. 
            - This is the folder that contains your Desktop, Downloads, My Documents, and other user-specific files. 
            - Example: `Users/your_name/`
            
        2. In File Explorer, open the "`anaconda3`" folder (note: not the hidden folder called `.anaconda` that starts with a `.`)
            - Open the `etc` folder inside the `anaconda3` folder. 
            - Open the `profile.d` folder inside the `etc` folder. 
                - You should see a `conda.sh` file in this folder.
            - Right click somewhere in the folder and select "Git Bash Here" to open a GitBash window in this current directory. 

        3. From the GitBash window you opened from the `profile.d` folder:
            - From your GitBash window, confirm that you are in the `profile.d` folder by typing `pwd` and hit enter. 
            - If the file path displayed ends with `profile.d` then are in the right folder. 
            - Enter the following command and hit etner.
                - `echo ". '${PWD}'/conda.sh" >> ~/.bashrc`
            
        4. Open a new GitBash window and enter `conda` again. You should no longer get the "bash: conda: command not found" error message! 
            -   You are all set to move on to "Setting Up Your `dojo-env` Environment"!

## 2. Setting Up Your `dojo-env` Environment

**We have prepared a special file for you called `environment.yml` which has a collection of all the essential packages we will need**


In order to use this file, you will first need to clone this repository to your computer. 

**1. Make sure you are logged into the same GitHub account on BOTH the github.com website and your local GitHub Desktop application.**

2. **Navigate to this repository's web page repo link**: https://github.com/coding-dojo-data-science/dojo-env-setup


3. **Click on the green `Code` button and then click `Open in GitHub desktop.`**
    - GitHub desktop should open automatically and ask you what folder you would like to store your repository in.
    - Note: GitHub Desktop will create a NEW folder INSIDE of the folder you select. 
        - It will be named the same as the repository name.
        
        
4. **Once have the repository cloned, you will need to open a terminal window in the same directory as this repository.**
    - There are 2 ways to do this. 
        1. From GitHub desktop, make sure the left side bar says "dojo-env-setup" in the top-left corner under Current Repository. 
            - Click on the Repository menu and select `Open in terminal` or `Open in gitbash`.
        2. From your terminal, use the change directory command to navigate to the folder where the repo was cloned. (Recommend using option A, as its easier).
    - **Once you have your terminal open, type `ls` to see the file contents of your current folder.**
        - You should see a file called `environment.yml`. 
        - If you do not see the folder, check if you see a `dojo-env-setup` folder instead. 
            - If so, type `cd dojo-env-setup` to navigate into the repo.
            - Type `ls` again and confirm you see `environment.yml`.
    - **Once you've confirmed you are in the same folder as the `environment.yml` file, type the following command into your terminal.**
        - `conda env create -f environment.yml`
        - press `enter`
    - The installation process will take several minuts. 
    - You may be asked a Y/N question at some point.
        - Say `y` and press enter to continue.
        
    - Once succesfully installed, you should see a command displayed telling you how to activate your new environment. 
   
    
    
5. **Confirm your environment was installed and activate it.**
    - Type `conda env list` to display the list of your locally installed environments. 
        - You should see 2 environments:
            - `base`
            - `dojo-env`
    - **Activate your `dojo-env` with `conda activate dojo-env`**
    - Note for Windows users: 
        - if you get an error running `conda activate dojo-env`, try `source activate dojo-env` instead.
        
        
6. **Add your new environment to Jupyter Notebook**
    - After activating your `dojo-env`, enter the following command and press enter:
    - `python -m ipykernel install --user --name dojo-env --display-name "Python (dojo-env)"`

        
7. **Test your installation of jupyter notebook.**
    - In your terminal, type `jupyter notebook`
    - Your web browser should open and display a list of files contained within the current directory.
    - Note: Your terminal window will be busy whenever it is running jupyter notebook. You will not be able to enter any additional commands in this terminal window while jupyter is running. 



8. Create a New test notebook.
    - In the top-right corner, you should see a `New` button for creating a new notebook.
    - Click `New` and select `Python (dojo env)`
     
    - Note: if you do not see this option listed:
        - Quit jupyter notebook by either using the Quit button  OR pressing Control+C in your terminal to force-quit jupyter.
        - Make sure your `dojo-env` is activated.
        - repeat step 6, adding you new environment to Jupyter Notebook

# 3. Adding Jupyter Notebook Extensions


### Jupyter Notebook Extensions Resources
- [Documentation](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html)
- [Official `nbextensions` Installation Instructions (also detailed below)](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html)

       
#### Installing Using Pip    
- **Below is an abbreviated version of the official instructions for Installing jupyter-contrib-nbextensions ([Documentation](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html)):**
    1. Install extensions
    ```bash
    pip install jupyter_contrib_nbextensions
    ```
    2. Install additional requirements (Install javascript and css file):
    ```bash
    jupyter contrib nbextension install --user
    ```
    3. Activate the extension configurator
    ```bash
    jupyter nbextension enable jupyter_nbextensions_configurator
    ```
>- Now, boot up jupyter notebook and look for a new tab called (`nbextensions`) on the jupyter file-explorer view. If its there, great! Move on to the "Turning on extensions" section below.
      

### Turning on extensions

- **When you boot up jupyter notebook, there should be a new tab at the top called `nbextensions`.** Click on the tab to open the list of available extensions.


- This opens a menu of all of the available extensions with checkboxes to activate them; 
  - ***NOTE: If the list of available notebook extensions is grayed out:***
    - Uncheck "`disable configuration for nbextensions without explicit compatibility (they may break your notebook environment, but can be useful to show for nbextension development)`" at the top of the page next to the search box.
    
    
    
- **To enable the recommended extensions**:
  - Click on the **checkbox** next to the extensions name  
  
- **To change the settings for an extension**:
  - Click on the **name** of the extension to select it. Now, if you scroll down, you should see the list of options for the currently selected extension. 
  
- **Note: any extensions that you enable or settings that you change are *automatically* saved.**

### Recommended extensions & settings



- `Table of Contents (2)`: 
    - Clickable sidebar with markdown headers as bookmarks/links.
    - Recommended options:
        - Change `Maximum level of nested sections to display on the tables of contents` to 3.
        -  Check `Display Table of Contents as a sidebar (otherwise as a floating window)`
        - Check `Collapse/uncollapse ToC sections when the collapsible_headings nbextension is used to collapse/uncollapse sections in the notebook. For the inverse behaviour, see collapsible_headings' configuration`


- `Collapsible Headings`: Collapse sections of your notebook using markdown headers.
    - Recommended options: 
        -  Check 'Collapse/uncollapse notebook sections when the ToC2 nbextension is used to collapse/uncollapse sections in the table of contents. For the inverse behaviour, see ToC2's configuration' at towards the bottom of the options.


- `Live Markdown Preview`: Shows a preview of what the markdown cell you are editing will look like once you render it with Shift+Enter
    - Recommended options:
        - Check `Show the input & output of markdown cells side-by-side while editing them.`

- `Ruler` (not Ruler in Editor)
- `spellchecker`



# 4. Setting `dojo-env` as your default + adding `jnb` shortcut

- This section will require you to enter several commands in your Terminal (on Mac) or GitBash (on Windows). 
- **Note: when the instructions say to "run" a command**, it means to type that command (or copy and paste it) into your Terminal/Git Bash and then hit `Enter`

## Mac
- On a Mac, we need to first see what shell you're running.
     - In your terminal, type `echo $SHELL.` and hit enter.
     
#### If the response ends in `bash`

1. Add the environment activation command:
    - Run `echo "conda activate dojo-env" >> ~/.bash_profile`


2. Add the alias to start "jupyter notebook" using `jnb`
    - Run `echo 'alias jnb="jupyter notebook"' >> ~/.bash_profile`
    
    
3. Finally, activate the new settings:
    - Run `source ~/.bash_profile`.


#### If the response ends in `zsh`:

1. Add the environment activation command:
    - Run `echo "conda activate dojo-env" >> ~/.zshrc` 
    
    
2. Add the alias to start "jupyter notebook" using `jnb`
    - Run `echo 'alias jnb="jupyter notebook"' >> ~/.zshrc`
    
    
3. Finally, activate the new settings:
     - Run `source ~/.zshrc` 

## Windows

- Make sure you have installed GitBash, per the instructions above.
- Determine which set of instructions below to follow:
    - Take note of if you were able to run `conda activate dojo-env` to activate your `dojo-env` or if you had to use `source activate dojo-env`.


####   If you were able to run `conda activate dojo-env`:


0. Make sure the profile file for GitBash has been created. 
    - Run `touch ~/.bash_profile` to create a new hidden file called ".bash_profile" in your user folder.
    
1. Add the environment activation command.
    - Run `echo "conda activate dojo-env" >> ~/.bash_profile` 

2. Add the alias to start "jupyter notebook" using `jnb`
    - Run `echo 'alias jnb="jupyter notebook"' >> ~/.bash_profile`
   

3. Finally, activate the new settings:

    - Run `source ~/.bash_profile` to activate the changes you just made
    
#### If you had to run `source activate dojo-env`:
    
0. Make sure the profile file for GitBash has been created. 
    - Run `touch ~/.bash_profile` to create a new hidden file called ".bash_profile" in your user folder.
    
1. Add the environment activation command.
    - Run `echo "source activate dojo-env" >> ~/.bash_profile` 

2. Add the alias to start "jupyter notebook" using `jnb`
    - Run `echo 'alias jnb="jupyter notebook"' >> ~/.bash_profile`
   

3. Finally, activate the new settings:

    - Run `source ~/.bash_profile` to activate the changes you just made
    

# 5. Install a code editor - Visual Studio Code


- Finally, we will install a text editor that is designed for programmers, called Visual Studio Code.
    - We will use this editor to work with some special settings files (like your terminal's `.bash_profile`. 
    - You can also use VS Code to edit your projects' README files while previewing them in real time!

## Install Visual Studio Code

- Go to https://code.visualstudio.com/
    - It should auto-recognize your OS and have a blue Download button with a version for your OS.
    - Click Download to download the installer. 
    
- For Windows Users:
    - Click on the installer to run it.
    - Select the default options. 
    
- For Mac Users:
    - Click on the installer to unzip it. 
    - Once the Application is unzipped, drag the icon for Visual Studio Code.app to your applications folder on your sidebar in Finder. 
![png](https://raw.githubusercontent.com/coding-dojo-data-science/dojo-env-setup/main/images/mac_vscode_install.png)

    
    
- Once Visual Studio Code installation is completed, open it!
    - Windows Users: check your Start Menu. 
    - Mac Users: check your Applications folder in Finder.

![png](https://raw.githubusercontent.com/coding-dojo-data-science/dojo-env-setup/main/images/vs_code_get_started.png)

## Install Python Extensions
- On the left sidebar, there are several icons for different menus.
- Click on the Extensions sidebar icon (5th down, looks like 4 squares).

![png](https://raw.githubusercontent.com/coding-dojo-data-science/dojo-env-setup/main/images/1_extension_sidebar.png)

- On the Extension sidebar, there will be several sections (INSTALLED/POPULAR/RECOMMENDED).
    - Right now you should have nothing under the INSTALLED menu.
    - You should see "Python" listed under POPULAR. 
        - If not, you can enter "Python" in the search box at the top of the sidebar
        - OR you can click on [this link to the extension ](https://marketplace.visualstudio.com/items?itemName=ms-python.python) on the extension marketplace website.
        
    - Click on the "Install" button for the Python extension.
![png](https://raw.githubusercontent.com/coding-dojo-data-science/dojo-env-setup/main/images/2_extension_installation.png)



- Note: the Python extension will also install several required extensions. When installation is complete, you should see the following under the "INSTALLED" section:
    - Python, Pylance, Jupyter Notebook renderer,Jupyter, and Jupyter Keymap

![png](https://raw.githubusercontent.com/coding-dojo-data-science/dojo-env-setup/main/images/3_installed_extensions.png)


## Setting VS Code to use your `dojo-env` as the default Python installation

- We must teach the Python extension where to find our `dojo-env`'s version of Python.

- On the extension sidebar, click on the Gear icon for the Python extension and select "Extension Settings"
![png](https://raw.githubusercontent.com/coding-dojo-data-science/dojo-env-setup/main/images/4_python_settings.png)

- You should see a new "Settings" pane open in the main window. 
    - Take note of the "Default Interpreter Path".
        - It is currently set to just "python".
![png](https://raw.githubusercontent.com/coding-dojo-data-science/dojo-env-setup/main/images/5_settings_default_interp.png)

- We need to change this setting to match the exact filepath for our `dojo-env`'s python.

- In your terminal or GitBash:
    - Make sure your dojo-env is activated
    - Run the command: `which python`
        - It will print out a filepath to your dojo-env.
![png](https://raw.githubusercontent.com/coding-dojo-data-science/dojo-env-setup/main/images/6_which_python.png)
    - Copy and paste that exact file path into the "Default Interpreter Path" field in the Python extension settings.
    
    
    
![png](https://raw.githubusercontent.com/coding-dojo-data-science/dojo-env-setup/main/images/7_replace_default_interp.png)

### Mac Users Only: Add the `code` command to your terminal

- We want to be able to type the word "code" in our terminal and have that open up VS Code. 
    - Windows users have this command added automatically during installation. 
    
    - Mac Users must run 1 more command from VS Code. 
    
1. Open the Command Palette: 
    - Either click on View in the menu bar and select "Command Palette"
    - OR use the keyboard shortcut (`Cmd` + `Shift` +`p`)

2. In the small pop-up window, type "install code" and you should see it auto-suggest the option for "Shell Command: Install 'code' command in PATH".
    - Click on this option. 
    
![png](https://raw.githubusercontent.com/coding-dojo-data-science/dojo-env-setup/main/images/8_install_code_command.png)
    
    
    


### Test the `code` command

- Open a new terminal or GitBash window.
- Run the command `code` to verify that VS Code opens. 

- Note: You can add a specific folder or filename to open, after the word code. 
    - To open the current folder `code .`
- If it opens, great!
    - If not, make sure you've opened a new terminal window AFTER installing the code command.

# FINAL NOTES

## Packages NOT Installed in `dojo-env`

### XGBoost
- Due to Windows vs MacOS differences, we did not include xgboost in our environment.
- For Windows Users and MacOS Users (that are NOT using a mac with a M1 Apple Chip):
    - see the official Installation instructions for Python Xgboost here: https://xgboost.readthedocs.io/en/stable/install.html#python 

- For MacOS users with a M1 Apple chip:
    - see the section below ("M1 Mac Users")

### M1 Mac Users

- There are several packages that you may have previously used on Google Colab that are not currently supported on Apple's M1 processors. 

    - These include:
        - tensorflow
        - xgboost

    
- While there are some third-party instructions for workarounds, they are rather involved and may cause issues with what we have already installed in your environment. 

- **For now, continue to use Google Colab for projects using tensorflow and xgboost.**

# APPENDIX

## What to do if your environment breaks and you need to re-install it.

- It is not uncommon to accidentally break our virtual environment by isntalling a new package or updating a pre-existing one. 
- In the event your environment stops working and it needs to be re-installed: 
	1. open your terminal/gitbash and deactivate your `dojo-env`:
		- Type `conda activate base` or `conda deactivate` and press enter. 
		- Your terminal should now say `(base)` with your promit instead of `(dojo-env)`.
	2. Remove the broken `dojo-env` using the command:
		- `conda remove --name dojo-env --all`
		- enter `y` to approve the removal of the environment and hit enter. 
	
	3. Wait for the env to be removed.
		- This will delete all of the files associated with JUST our `dojo-env`. So anconda will still be installed, we will just need to re-install our `dojo-env`.
	4. Once its completed, use this repository's environment file to set up the `dojo-env` again. 
		- Repeat the environment installation commands from the "Setting Up Your `dojo-env` Environment" section above. 

## Showing Hidden Files

- Windows Users: 
    - Turn on View Hidden Files and Folders in your File Explorer menu:
        - [Microsoft Support Article](https://support.microsoft.com/en-us/windows/view-hidden-files-and-folders-in-windows-10-97fbc472-c603-9d90-91d0-1166d1d9f4b5#:~:text=Open%20File%20Explorer%20from%20the,folders%2C%20and%20drives%20and%20OK.)
        
    - On the same settings page, also deselect "Hide extensions for known file types and click OK."
    
    
- Mac Users:
    - Use this keyboard shortcut from inside finder:
    `Cmd+Shift+.`
    - Use it again to hide hidden files. 
