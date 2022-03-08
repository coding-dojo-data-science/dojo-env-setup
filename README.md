# Installing Python Locally

## Required Installations

> Before we install our python environment, we need to take care of a couple requirements. Please make sure to install all of the items listed below before attempting to follow the remaining instructions. 

1. **A Linux-based bash shell/terminal:**
   - Linux users and MacOS users have this built-in to their OS.
   
   - [ ] **Windows users should install GitBash, instead of using the windows command prompt**
      - [Git for Windows download](https://gitforwindows.org/)
       - Otherwise, all of the commands for working with your terminal will not match the curriculum and other cloud-based platforms (like Amazon Web Services)

        
2. **GitHub Desktop** ([Link](https://desktop.github.com/))
    - [ ] Download the installer and log into the same github account you have been using for your projects. 
    - [ ] After installing, open GitHub desktop:
        1. Open the Preferences menu
            - On Mac: Select "GitHub Desktop" on the menu bar and then select Preferences.
            - **On Windows: <`CHECK WINDOWS APP`> **
        2. Select the Integrations tab.
        3. Make sure the Shell dropdown menu says Terminal (on Mac) or GitBash (on Windows).
            - If not, select it from the dropdown menu.
        4. Click Save.


2. **Anaconda - individual edition.** [Link](https://www.anaconda.com/products/individual)
    - Anaconda is a data-science-focused python distributable that comes with a convenient GUI program for working with our python environments.



## Recommend Installations


- While not explicitly *necessary*, it is strongly recommend you install a text editor for code. 
    - [ ] [SublimeText](https://www.sublimetext.com/): Great lightweight text editor with some convenient features. 
        - [Official Anaconda Guide on setting up SublimeText](https://docs.anaconda.com/anaconda/user-guide/tasks/integration/sublime/)
    - This program will make it easier to work with code-related files that would be difficult to work with if you use your OS's default text editor. 
    - Note: if you already have something like VS Code installed, that will be sufficient
    



## Setting Up Your `dojo-env` Environment

We have prepared a special file for you called `environment.yml` which has a collection of all the packages and versions that you are used to from Google Colab. 


In order to use this file, you will first need to clone this repository to your computer. 


1. Make sure you are logged into the same GitHub account on the github.com website and your local GitHub Desktop application.
2. Navigate to this repository's web page [repo link](https://github.com/coding-dojo-data-science/dojo-env-setup)
3. Click on the green Code button and then click Open in GitHub desktop.
    - GitHub desktop should open automatically and ask you what folder you would like to store your repository in.
    - Note: GitHub Desktop will create a NEW folder INSIDE of the folder you select. 
        - It will be named the same as the repository name.
        
        
4. Once have the repository cloned, you will need to open a terminal window in the same directory as this repository. 
    - There are 2 ways to do this. 
        1. From GitHub desktop, make sure the left side bar says "dojo-env-setup" in the top-left corner under Current Repository. 
            2. Click on the Repository menu and select `Open in terminal` or `Open in gitbash`.
        2. From your terminal, use the change directory command to navigate to the folder where the repo was cloned. (Recommend using option A, as its easier).
    - Once you have your terminal open, type `ls` to see the file contents of your current folder. 
        - You should see a file called `environment.yml`. 
        - If you do not see the folder, check if you see a `dojo-env-setup` folder instead. 
            - If so, type `cd dojo-env-setup` to navigate into the repo.
            - Type `ls` again and confirm you see `environment.yml`.
    - Once you've confirmed you are in the same folder as the `environment.yml` file, type the following command into your terminal .
        - `conda env create -f environment.yml`
        - press `enter`
    - The installation process will take several minuts. 
    - You may be asked a Y/N question at some point.
        - Say `y` and press enter to continue.
        
    - Once succesfully installed, you should see a command displayed telling you how to activate your new environment. 
    
5. Confirm your environment was installed.
    - Type `conda env list` to display the list of your locally installed environments. 
        - You should see 2 environments:
            - `base`
            - `dojo-env`
    - Activate your `dojo-env` with `conda activate dojo-env`
    - Note for Windows users: 
        - if you get an error running `conda activate dojo-env`, try `source activate dojo-env` instead. 
6. Add your new environment to Jupyter Notebook:
    - After activating your `dojo-env`, enter the following command and press enter:
    - `python -m ipykernel install --user --name dojo-env --display-name "Python (dojo-env)"`

        
7. Test your installation of jupyter notebook. 
    - In your terminal, type `jupyter notebook`
    - Your web browser should open and display a list of files contained within the current directory.


8. Create a New test notebook.
    - In the top-right corner, you should see a `New` button for creating a new notebook.
    - Click `New` and select `Python (dojo env)`
     
    - Note: if you do not see this option listed:
        - Quit jupyter notebook by either using the Quit button  OR pressing Control+C in your terminal to force-quit jupyter.
        - Make sure your `dojo-env` is activated.
        - repeat step 6, adding you new environment to Jupyter Notebook

### Additional Steps (Coming soon!)


1. Jupyter notebook extensions
2. Setting `dojo-env` to automatically activate for you.


# Adding Jupyter Notebook Extensions


### Jupyter Notebook Extensions Resources
- [Documentation](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html)
- [Official `nbextensions` Installation Instructions (also detailed below)](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html)



#### Installation via Conda
- **The best way to install is via `conda`** (however, windows users sometimes have issues with the conda installation not working properly).
    0. Open your terminal and make sure learn-env is activated.
        - Mac users: `conda activate dojo-env`
        - Windows users: `source activate dojo-env`

    1. Install the extensions via conda
    ```bash
      conda install -c conda-forge jupyter_contrib_nbextensions
      ```

    2. Activate the extension configurator
    ```bash
    jupyter nbextension enable jupyter_nbextensions_configurator
      ```
 >- Now, boot up jupyter notebook and look for a new tab called (`nbextensions`) on the jupyter file-explorer view. If its there, great! Move on to the "Turning on extensions" section below.
      
      
#### Installing Using Pip    
- **If you have issues installing with conda, install with pip instead ([Documentation](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html)):**
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
    
    
    
- **Clicking the name of an extension will load its options menu** below the table of extensions. 

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


- `Codefolding`: Lets you collapse function definitions and blocks of code. 


- `Live Markdown Preview`: Shows a preview of what the markdown cell you are editing will look like once you render it with Shift+Enter
    - Recommended options:
        - Check `Show the input & output of markdown cells side-by-side while editing them.`

- `Ruler` (not Ruler in Editor)
- `spellchecker`

<!-- 
- `Variable Inspector` (but warning/caveat): 
    - Lets you see details about all of the variables in your notebook.
    - HUGELY helpful for new coders.
    - Recommended options:
        - `Display window at startup` (for now while you are learning python)
 -->

# APPENDIX (work in progress)

## MacOS Terminal: changing from zsh to bash

   - [ ] **Mac Users should consider changing their Default shell to `bash` (Mac OS Catalina and newer)**
       - Open your Terminal application. If the title of the window has `zsh` in the name

## Setting `dojo-env` as your default 



## Showing Hidden Files

- Windows Users: 
    - Turn on View Hidden Files and Folders in your File Explorer menu:
        - [Microsoft Support Article](https://support.microsoft.com/en-us/windows/view-hidden-files-and-folders-in-windows-10-97fbc472-c603-9d90-91d0-1166d1d9f4b5#:~:text=Open%20File%20Explorer%20from%20the,folders%2C%20and%20drives%20and%20OK.)
        
    - On the same settings page, also deselect "Hide extensions for known file types and click OK."
    
    
- Mac Users:
    - Use this keyboard shortcut from inside finder:
    `Cmd+Shift+.`
    - Use it again to hide hidden files. 


```python

```
