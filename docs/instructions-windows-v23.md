# Windows Installation Instructions

___

- [Click here](https://hackmd.io/@jirvingphd/dojo-env-windows ) for a web version of these instructions, with a table of contents sidebar.
- [Click here](https://hackmd.io/@jirvingphd/dojo-env-overview) for the web version of the Installation Overview.

___

<img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1693270300__WIndowstoolsPythonInstallationforDSOverviewv2023.png">

## Table of Contents

**Step 1) Download and install required applications**

- Step 1.1) Install Tool #1: Windows Terminal with GitBash
    - Step 1.1.0) Install Windows Terminal
    - Step 1.1.1) Install Git for Windows
    - Step 1.1.2) Make GitBash the Default Profile in Windows Terminal
    - Step 1.1.3) Confirm that your default shell is set to GitBash
- Step 1.2) Install Tool #2: GitHub Desktop
    - Step 1.2.1) Install GitHub Desktop and Log Into GitHub Account
    - Step 1.2.2) Make Windows Terminal the Default Shell in GitHub Desktop
- Step 1.3) Install a Python distribution (Anaconda)
    - Step 1.3.1) Download and Install Anaconda
    - Step 1.3.2) Verifying that Terminal/GitBash Knows "conda"
    - Step 1.3.3) (if needed) Adding Conda to GitBash

**Step 2) Setting Up Your dojo-env Environment**

- Step 2.1) Clone the dojo-env-setup repository
- Step 2.2) Open the repo's folder in your Terminal
- Step 2.3) Create the dojo-env environment from file
    - Step 2.3.1) Run the correct "conda env create" command for your OS
    - Step 2.3.2) Wait for the dojo-env to be created
    - Step 2.3.3 Confirm your environment was installed.
- Step 2.4) Activate dojo-env and set it as your default environment.
    - Step 2.4.1) Activate dojo-env
    - Step 2.4.2) (if needed): Troubleshoot Conda Activate Errors
    - Step 2.4.3) Confirm that your Home folder is your User folder
    - Step 2.4.4) Add automatic activation of dojo-env 
    - Step 2.4.5) Confirm dojo-env is the default & "jnb" alias works.
    - Step 2.4.6) Shut Down Jupyter (properly)
- Step 2.5) Test the environment.

    - Step 2.5.1) Open the environment tester notebook 
    - Step 2.5.2) Change the notebook's kernel to dojo-env
    - Step 2.5.3) Run the environment test notebook from start to finish.

- **Step 3) Jupyter Notebook Preferences**

- **Step 4) Install a Text Editor - VS Code**



___



# **Step 1) Download and install required applications**

### Table of Contents - Step 1:

- Step 1.1) Install Tool #1: Windows Terminal with GitBash
- Step 1.2) Install Tool #2: GitHub Desktop
- Step 1.3) Install a Python Distribution - Anaconda



Before we install our python environment, we need to take care of a couple of requirements. 

## Step 1.1) Install Tool #1: Windows Terminal with GitBash

- Windows users will use a combination of GitBash and Windows Terminal. Windows Terminal comes pre-installed with Windows 11, but can be added to Windows 10.

- You should not use the  windows command prompt because the commands for working with your terminal will not match the curriculum and other cloud-based platforms (like Amazon Web Services).

    - Note: for a list of the equivalent commands for Windows command prompt see [this cheat sheet](https://www.geeksforgeeks.org/linux-vs-windows-commands/).

### Step 1.1.0) (Windows 10 Only) Install Windows Terminal via the Microsoft Store

NOTE: Windows 11 comes with Windows Terminal pre-installed. If you are running Windows 11, you can skip Step 0 and start with Step 1.

- For Windows 10 users, open your start menu using your Windows key or clicking on the Start Menu in the bottom left corner.

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670872974__1A_start_menu.png)

- Type "Store" with the start menu open and it will automatically start searching. You should see "Microsoft Store" appear.

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670873063__1_search_windows_store.png)

- Click on the Microsoft Store app on the left or click "Open" on the right sidebar to open the Microsoft store.
- Once the Microsoft store opens, click on the Search box on the top of app.

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670873315__2A_microsoft_store_home.png)

- Enter "Windows Terminal" in the search box and you should see the Windows Terminal result appear with a blue "Get" button like in the screenshot below:

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670873463__2_search_windows_terminal.png)

- Click on the blue "Get" button to start downloading the app.

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670873501__3_download_windows_terminal.png)

- Once its done downloading, the blue "Get" button will become an "Open" button. Click on "Open" to confirm that Windows Terminal is properly installed.
- A new "Windows Terminal" window running Powershell should appear, like in the screenshot below:

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670873594__4_open_windows_terminal.png)

- After confirming windows terminal is installed, click on the X in the top right corner to close the app. You are all set to move on to the next step!

------

### Step 1.1.1) Install Git for Windows

- Download the Git for Windows installer (https://gitforwindows.org/) and open it.

#### Select the same options as you see in the screenshots below:

- On the first page, make sure to UNCHECK "Only show new options" like in the screenshot below:

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670711700__Screenshot_20221210_050015.png)

- <font color=red>Make sure to select the option pictured below "Add Git Bash Profile to Windows Terminal"!!</font></font>

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670711711__Screenshot_20221210_050049.png)

- Then select the default options for the remaining options (unless noted otherwise below):

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670711823__Screenshot_20221210_050110.png)

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670711934__Screenshot_20221210_050114.png)

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670711962__Screenshot_20221210_050119.png)

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670711972__Screenshot_20221210_050124.png)

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670711985__Screenshot_20221210_050129.png)

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670712004__Screenshot_20221210_050133.png)


![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1696376250__Gitbashwhatshouldgitdo.png)

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670712057__Screenshot_20221210_050138.png)

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670712094__Screenshot_20221210_050148.png)

- One non-default option that you may want to select is to "Enable symbolic links" in the screenshot below.
    - This option will be helpful if you ever need to access data stored on a network drive. This will *not* be required for the program.

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670712081__Screenshot_20221210_050152.png)

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670712246__Screenshot_20221210_050157.png)

- TROUBLESHOOTING NOTE:
    - If you see the following "Replacing in-use files" screen (screenshot below) about closing open instances of gitbash: close all other windows of GitBash.
    - If it still shows items that are running that you cannot find, the easiest solution is to cancel the installation, restart your computer, and then open the installer again before opening any gitbash windows.

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670712402__Screenshot_20221210_050206.png)

- Click install and wait for the process to finish. Next, move on to Tool #2: GitHub Desktop.

### Step 1.1.2) Make GitBash the Default Profile in Windows Terminal

- From your Windows Start menu, search for "Terminal" and open a new Windows Terminal window.
- It will open using the default shell "Powershell", pictured below:

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670713406__Screenshot_20221210_060318.png)

- Click on the drop down arrow to reveal the menu.
    - Select Settings

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670713567__Screenshot_20221210_060553.png)

- The settings tab will open and should look like the screenshot below:

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670713596__Screenshot_20221210_050800.png)

- Click on the drop down menu for the first option "Default Profile" and select GitBash

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670713683__Screenshot_20221210_060802.png)

- Click the blue Save button in the bottom right corner.

### Step 1.1.3) Confirm that your default shell is set to GitBash

- To test if the default shell is now set to GitBash, open a new Terminal window.
- If you see a window like the one below that has the GitBash icon (the multicolored 4-squares in the top left corner), then you are all set!

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670713874__Screenshot_20221210_061055.png)

- You're all set up with Windows Terminal and GitBash!

------

## Step 1.2) Install Tool #2: GitHub Desktop

### Step 1.2.1) Install GitHub Desktop and Log Into GitHub Account

- Download the installer from this link: [GitHub Desktop](https://desktop.github.com/)
- Once installation is complete, open the application.
- Log into the same GitHub account you have been using for your projects.



Troubleshooting: when GitHub Desktop first opens, you may see a message about git not being installed. 

![png](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1696376238__nogit.png)

- If you see this message, click on the "Install Git" button.

### Step 1.2.2) Make Windows Terminal the Default Shell in GitHub Desktop

- Once you have logged into the app, open the Options menu.![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670712744__Screenshot_20221210_050900.png)

- Click on `File` in the menu bar and then select `Options`

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670712811__Screenshot_20221210_055322.png)

- Select the "Integrations" tab on the left sidebar of the Options window.

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670712772__Screenshot_20221210_050917.png)



- Click on the drop-down menu for Shell and select Windows Terminal. (Windows 10 users, if you do not see this option, make sure you have followed Step 0 of these instructions. If you still do not see Windows Terminal as an option, please restart your computer and try again.)

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670712965__Screenshot_20221210_055455.png)

- Click Save and the window will close.![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1670713097__Screenshot_20221210_055706.png)

- Click Save. You may close Github Desktop for now.

------

___

## Step 1.3) Install a Python Distribution - Anaconda

- Anaconda is a data-science-focused python distributable that comes with a convenient GUI program for working with our python environments.

### Step 1.3.1) Download and Install Anaconda

- Download and run the installer from the following link:  [Anaconda Individual Edition](https://www.anaconda.com/download)

- Use the default options**, EXCEPT when you see the "Advanced Installation Options" window (like in the screenshot below).**
    - Select "Add Anaconda3 to my Path environment variable". Disregard the warning message will appear in red text.
    - BOTH options should be checked, like in the screenshot below:

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1681423160__anacondafinalnew.png)



### Step 1.3.2) Verify that Terminal/GitBash Knows "conda"

You may need to take another step to get anaconda and Terminal working together.

- Open **a new Terminal window** from your start menu. It MUST be a new window!

- **Type the command `conda ` and press enter.**
- **If you see a message that says something like: "bash: conda: command not found"**:
    - Follow the instructions below under "Adding Conda to GitBash"
- **If you do *not* get the command not found message:**
    - **You are all set to move on to Step 2!** Disregard the final section below that says “Adding Conda to GitBash”


### Step 1.3.3) (if needed) Adding Conda to GitBash:

**If a NEW terminal window recognized the conda command in the previous step, then skip this step!**

#### **Step 1.3.3-Option A) Easy Solution (if it works!)**

- **Open the start menu and search for "Anaconda Prompt"**

    - Double-click on Anaconda Prompt to open it.
    - ***If you cannot find Anaconda Prompt, use Option B below instead.***

- **In the window that appears, enter the following command:** 

    ````
    conda init bash
    ````

- **Open a new Windows Terminal window and attempt to run the `conda` command again.** 

    - if it displays a list of commands, great! 
    - If it says something like "conda not found" then move on to Option B below.

#### **Step 1.3.3-Option B) Thorough solution (if option A didn't work)**

Note: the instructions below are adapted from this [Blog Post](https://fmorenovr.medium.com/how-to-add-conda-to-git-bash-windows-21f5e5987f3d)

- Once you have installed anaconda**, use File Explorer to Open Your User folder.** (Windows key +E is shortcut for File Explorer)

    - **Your User folder is the folder that contains your Desktop, Downloads, My Documents, and other user-specific files.**
        - Example: `Users/your_name/`
    - **If you're having trouble finding your user folder:**
        - A) Go to This PC in File Explorer, and then double click on your C drive.
            - Then double click the Users folder and then click on the folder that corresponds to your windows username.
        - or B) Alternatively, you can run the command `whoami` which should display the name of your user folder. 

    

- **Inside your user folder, you should see a folder named "`anaconda3`"** (note: not the hidden folder called `.anaconda` that starts with a `.`). Double-click the folder to open it.

    - You should **see a folder named `etc` inside the `anaconda3` folder**. **Open it.**
    - You should **see a folder called `profile.d` folder** inside the `etc`. **Open it.**

    - You should **see a `conda.sh` file in this folder** (Note: depending on your settings in File Explorer, it may not show the file extension, .sh,  and may just show "conda". This is the correct file!
    - **Right-click somewhere in the "profile.d" folder and select "Open in Terminal" or "Git Bash Here"**
        - Note for Windows 11 Users: "GitBash here" is going to appear in the "Show more options" sub-menu when you right-click
            ![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1659739323__windows_11_right_click1.png). ![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1659739359__windows_11_right_click2.png)



- **From the GitBash window that opens, enter the command**

    ```
    pwd
    ```

- **Press enter and examine the file path that's displayed.**

    - If the file path displayed ends with `profile.d` then you are in the right folder!
    - If not, restart the "Adding Conda to GitBash" instructions again and make sure you can find your profile.d folder.
        - Reach out to your instructor or a TA if you are still having issues.

- **Next, Copy and paste the following command into your Terminal and hit enter:**

    - **Reminder: You can paste in Windows Terminal by simply right-clicking** anywhere within the activate Terminal window.


```bash
echo ". '${PWD}'/conda.sh" >> ~/.bashrc

```

___

- You may see an error message in your Terminal that looks like the follow screenshot: 

![png](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1696376225__warningafter133optionb.png)

- **Do not worry!! It has addressed the problem already and is just letting you know.**

___



- Open a new GitBash window and enter `conda` again.
    - You should no longer get the "bash: conda: command not found" error message!
        - Reach out to your instructor or a TA if you are still having issues.

> You are all set to move on to the next lesson "2. Setting Up Your dojo-env Environment"



___



# **Step 2) Setting Up the dojo-env Environment**

### Table of Contents - Step 2

- Step 2  Overview
- Step 2.1: Clone the dojo-env-setup repository
- Step 2.2: Open the repo in your Terminal
- Step 2.3: Create the dojo-env environment
- Step 2.4: Set `dojo-env` as the default environment.
- Step 2.5: Testing the Environment

## Step 2 Overview:

- In Step 1, we installed the foundational tools needed for our local python installation. 

    - While we did install a Python distribution with a basic copy of Python (Anaconda or miniforge), we have not installed all of the packages and tools that we need as data scientists.
- In Step 2, you will be creating a custom python environment called "dojo-env". 

    - An "environment" is a bundle of specific python packages that are used together. Importantly, an environment specifies specific version #'s of the packages to ensure that all of the versions installed are mutually compatible.
    - You can install many environments on your computer and switch between them as needed for different projects.

    - We have designed the dojo-env to include everything you'd need for our program, so you may not have a reason to add additional environments. 
- The environment files (and a backup of these instructions) are in the [dojo-env-setup repository](https://github.com/coding-dojo-data-science/dojo-env-setup)
    - The Detailed Instructions below will guide you through how to clone and use the environment setup repository.

## Step 2.1) Clone the dojo-env-setup repository

- **Open the dojo-env-setup repository on GitHub.com:** https://github.com/coding-dojo-data-science/dojo-env-setup

- **Before the next step, make sure that :**
    - you are logged in to your account on GitHub.com 
    - you are logged into the SAME account in the GitHub Desktop app

- **Click on the green `Code` button and then click `Open in GitHub desktop.`**
- GitHub desktop should open automatically and ask you what folder you would like to store your repository in.
    ![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1656806399__clone-repo-menu.png)





- **Troubleshooting Note: if you are brought to the Download GitHub Desktop web page instead:**

    - It means you were not logged into the same account on GitHub.com and GitHub Desktop when you clicked Open in GitHub Desktop. 
        - Make sure you see your user profile pic in the top right of GitHub.com 
        - and check your Account in GitHub Desktop's Preferences/Options menu.
        - and then try again.

- **Decide where to save the repo:**

    - By default, GitHub Desktop will use a new "GitHub" folder in your Documents folder.
        - GitHub Desktop will create a NEW folder with the same name as the repository INSIDE of whichever folder you select.
        - If you use the default options, then this will create a "dojo-env-setup/" folder inside of "Documents/GitHub/"
    - **Note: it is strongly recommended that you use the Documents/GitHub folder for this repository.**
        - But if you'd rather save the folder somewhere else: 
            - Use the "Choose" button (the button name may be "Browse" on Windows).
            - A window should pop up for you to find and click on the folder where you want to create the "dojo-env-setup" folder.
            - Once you have selected a new folder using the Browse button, you should see the full folder path displayed.

- **Once you've decided where you will clone the repository:**

    - Remember the full file path of the folder you selected!  **(See the screenshot below. )**
        ![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1656806548__clone-repo-menu%20annotated.png)

        

- **Click Clone**

GitHub Desktop will download a copy of the repository into a new folder on your computer.

## Step 2.2) Open the Repo in Terminal(GitBash)



### Step 2.2.1) Open the dojo-env-setup repository in Terminal.

Once you have cloned the repository, **you must open a Terminal Window in the same folder as the repository**.  The easiest way to do so is from within GitHub Desktop.

- **In GitHub Desktop: make sure the left sidebar says "dojo-env-setup**" in the top-left corner under Current Repository.
- **Click on the Repository menu and select "`Open in terminal`" or "`Open in gitbash`"**
    - For Windows Users, the menu will be at the top of GitHub Desktop's window.
- **Alternatively, you can use the keyboard shortcut:** 
    - **Control + `**   (the key above tab that also has the tilde symbol ~)

### Step 2.2.2) Confirm you are in the correct folder.

- **Note: Terminal/GitBash does not support the Copy and Paste Keyboard Shortcuts (Control+C) /(Control+V).**  

    -  We recommend typing out the shorter commands for experience, but there will be several long commands that we will encourage top copy and paste for accuracy.
    -  **You can paste in Windows Terminal by simply right-clicking** anywhere within the activate Terminal window.

- First, in the terminal window that appears, **type the "pwd" command** (which stands for print working directory) and press Enter.

    ```
    pwd
    ```

    - **It will display the folder name of the folder your terminal is currently located.** 
        - The **folder path should end in "dojo-env-setup/"**
        - If you used the default GitHub folder when you cloned dojo-env, the full filepath would be something similar to "/Users/yourname/Documents/GitHub/dojo-env-setup/"

- **Second, run the command to list all of the files contained in the current fol**de ( the command "ls -a" will display a detailed list of all files in the repo.

```
ls -a
```

- **You should see a list of all the files in the current folder,** similar to the screenshot below. 
    - You should see 3 files that start with "environment-ds_" and end with ".yml" similar in the screenshot below. Note: the exact names of the environment files may be slightly different than the screenshot below.

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1656808093__dojo-env-setup%20ls%20result.png)

**If so, you are all set for step 2.3: create the dojo-env environment!**

### Step 2.2-Troubleshooting Opening the Repo: 

If you are having trouble getting GitHub desktop to open GitBash in the correct folder there are 2 solutions for getting your gitbash window in the dojo-env-setup folder.

#### Solution #1: Using File Explorer + Right Click

If you followed the instructions in step 1 and used the default options when installing Git for Windows/GitBash, you should have a new option in your Right-Click menu that says "GitBash here".

- In GitHub Desktop click the Repository menu again and select "Show in File Explorer".
- Once file explorer opens,  right-click anywhere inside the folder  (right-click on empty space, not on a file) and select GitBash here.
    - A GitBash window should open in the correct folder.

- Type pwd to confirm that you are indeed in the dojo-env-setup folder.



#### Solution #2: Open a new GitBash and navigate to the right folder.

If you do not have the option to "GitBash here", you can manually navigate there in GitBash.

- Open the windows start menu, find and click on GitBash to open a new window.

- Important Note: You must know the full file path for the repo for the next step. We will refer to as <repo_filepath> in the instructions below.

    - if you used the suggested default folder 

        when cloning the repo, your repo_filepath should be: 

        - " /Users/<your name>/Documents/GitHub/dojo-env-setup" 

            - But instead of <your name> it will be your actual user name for your computer

            - If you are not sure what your username is, run the "whoami" command in your GitBash to see your user name.

    - If you did NOT use the suggested default folder, 

        - Your repo_filepath will be the path displayed in the window that appeared when you cloned the repo.
            - You should have taken note of the file path you selected, as indicated in the screenshot.

- Once you know what your repo_filepath is navigate to that folder using the change directory command (cd)

    - "cd <repo_filepath>".
    - See the examples below:

```
## Examples are assuming your username is "codingdojo"
# Example if you used default folder:
cd /Users/codingdojo/Documents/GitHub/dojo-env-setup/
# Example if you used a different folder. e.g. you made a Boot Camp Stuff folder in your Documents folder.
cd /Users/codingdojo/Documents/Boot Camp Stuff/
```

## Step 2.3) Create the dojo-env environment

Now that your terminal is open in the repo's folder, you're ready to create your dojo-env environment.

### Step 2.3.0) *(Optional, but Recommended)* Speed Up Your Environment Creation By Switching to libmamba

The following step, "2.3.1) Run the conda env create command", can take anywhere from 10 - 90 minutes, depending on your computer and internet connection.  

You can speed up the process by changing the default tool that checks that the packages in the new environment are compatible, called the solver. 

- Make sure conda is up to date (it should be if this is the first time you've installed Anaconda)

    ```bash
    conda update -n base conda
    ```

- Run the following 2 commands to install libmamba and to make it the default solver for conda:

    ```bash
    conda install -n base conda-libmamba-solver
    conda config --set solver libmamba
    ```

    - **Note: if you run into issues with this optional step, you can skip it and move on** to step 2.3.1) Run the conda env create command 

- See [A Faster Solver for Conda: Libmamba](https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community) if you'd like to learn more.

###  Step 2.3.1) Run the "conda env create" command

- Run the  conda env create command below in your Terminal

```
conda env create -f environment-ds_windows.yml
```

### Step 2.3.2) Wait (patiently) for the dojo-env to be created. 

- **You will see several progress bars during the process as Anaconda checks the list of packages requested for compatibility** with your machine. 
    - It will then download and install the final versions that it determined would work best for your machine.
    - **Note that it can take anywhere from 10-90 minutes** to finish creating the environment, depending on your computer and internet connection, and if you switched to the faster solver in optional step 2.3.0.

- **Once it has been completed you should see a message that says:**

    ```
    # To activate this environment use:
     conda activate dojo-env
    # To deactivate this environment use:
     conda deactivate 
    ```

    

    ![png](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1696376455__condaactivatemessage.png)

    

### Step 2.3.3) Confirm your environment was installed

- Enter the following command to display the list of your locally installed environments.

    ```
    conda env list
    ```

- **You should see 2 environments, including dojo-env:**

    - `base`
    - `dojo-env`

    - **If you see dojo-env in the list:**

        - **Success! dojo-env was successfully created! But we aren't using it yet just yet.** 
        - We must first "activate" an environment to determine which version of Python & packages are currently being used.

    - **If you do not see dojo-env**:

        - Something went wrong during your installation. **You should reach out for assistance on the discord channel.**

### Step 2.3.4) Activate dojo-env & add dojo-env kernel in Jupyter

- **Run the following 2 commands in your Terminal:**

```python
conda activate dojo-env
python -m ipykernel install --user --name dojo-env --display-name "Python (dojo-env)"
```

- The first line in the code block above will switch to dojo-env environment.
- The second line will install dojo-env as an option in Jupyter Notebook.

### Step 2.3.5) *(Only if needed)*Troubleshoot Conda Activate Errors:

-  **Problem**: when you attempt to run "conda activate dojo-env" you see a message that says something like "your terminal is not set up for conda activate". See the example below: 

```bash
CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run
    $ conda init <shell_name>
Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell
See 'conda init --help' for more information and options.
```



#### Conda Activate Solution #1

##### Step 1) Run Conda Init with Anaconda Prompt

- **Open Anaconda Prompt from your start menu.** This was installed with Anaconda automatically.

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1671129412__A1_anaconda_prompt.png)

- **A window will open that looks the one below**: (if no text appears in the window, press enter and it should appear

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1671129457__a2_prompt_window.png)

- **Run the following command:**

```
conda init bash
```

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1671129622__A3_A_conda_init_command.png)

- **You will see a long list of file paths and should see the word "modified" next to 1-2 of them.**

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1671129488__A3_conda_init_bash.png)

- **Close Anaconda Prompt**

##### Step 2: Run conda init with GitBash

- Open Windows Terminal/GitBash

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1671129694__a4_open_gitbash.png)

- Run the same command again

```
conda init bash
```

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1671129713__a5_conda_init_gitbash.png)

- **You will see another list of filepaths.**

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1671129743__a6_conda_init_bash_result.png)



- **Run the following command:**

```
source ~/.bash_profile
```

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1671129907__a7_source_bash_profile.png)

- **Now you should be able to run "conda activate dojo-env"!**  

#### Conda Activate Solution #2

-  [Alternative/Older Solution] Alternatively, you could use a slightly different command to activate your environment. Replace the word "conda" with "source".
    -  If you use this approach, you will **always** need to say `source activate` instead of `conda activate.`

```
source activate dojo-env
python -m ipykernel install --user --name dojo-env --display-name "Python (dojo-env)"
```

## Step 2.4) Set `dojo-env` as the default environment

The next steps will ensure that the dojo-env is automatically activated for you. 

### Step 2.4.1) Make sure you've activated dojo-env in the previous step. 

- Make sure that you've followed the previous step and activated dojo-env.
- You should see (dojo-env) in parentheses either above or next to your Terminal prompt.

### Step 2.4.2) (if needed) Troubleshoot Conda Activate Errors:

If you receive an error message when activating your dojo-env, please see "Step 2.3.5) *(Only if needed)* Troubleshoot Conda Activate Errors."

### Step 2.4.3) Confirm that your User folder is your home folder ("~")

In your Terminal, the tilde character (~) represents your home directory.  Your home directory should be your User folder (e.g., "/c/Users/codingdojo"). 

We will use the "~" character in the following commands, so we must ensure that your machine has it defined correctly. 

- **Open a new Terminal window.**

- **Run the following command to change your terminal's current directory to the "~" folder** 

    ``` 
    cd ~
    ```

- **Run the following command to print the name of the folder:**

    ```
    pwd
    ```

- **If the folder it displays looks like: "/c/Users/YOUR_USERNAME"**:

    - Then you're all set to move on to the next step!

- **If the file path does *not* start with** "/c/Users/":

    - **Note: if your file path starts with "/cygdrive/c/Users/"** this is **not** the same folder and you must perform the following steps.

    - **You run the following 2 commands, replacing {your-username} with your personal User folder.:**

        ```bash
        touch /c/Users/{your-username}/.bash_profile
        source /c/Users/{your-username}/.bash_profile
        ```

        - Note: if you do not know your User folder's name, you can run the `whoami` command to see the name of your User folder.

        <img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691619428__changesource.png">



### Step 2.4.4) Add automatic activation of dojo-env

- Make sure that your terminal is not running jupyter notebook (you can press "`Cntrl`+`C`" to force quit the server from your terminal).
- Alternatively, you can open a new terminal/GitBash. (You can perform these steps from any folder.)

- Run the following commands to automatically activate dojo-env and to add shortcuts for Jupyter:
    - Note: **it is very important that you do not add any spaces next to the "="** in the alias commands below:
    - **Tip: You can paste in Windows Terminal by simply right-clicking** anywhere within the activate Terminal window.


```bash
touch ~/.bash_profile
echo "conda activate dojo-env" >> ~/.bash_profile
echo 'alias jnb="jupyter notebook"' >> ~/.bash_profile
echo 'alias lab="jupyter lab"' >> ~/.bash_profile

```

- Finally, activate the new settings:
    - Run `source ~/.bash_profile` or open a new GitBash window to activate the changes you just made

### Step 2.4.5) Confirm dojo-env is the default & "jnb" alias works

##### Confirm `dojo-env` is your default env

- To confirm that dojo-env is now your default environment:
    - **Open a new terminal window.**
    - **You should see `(dojo-env)` appear next to, or above, your prompt.**

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1647634446__confirm_dojo_env.png)



##### Confirm the shortcut aliases work

- **Try running the command "`jnb`" in your terminal.**

    - You should see a lot of messages printed in the terminal and then your web browser should open  jupyter automatically .

    <img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691620120__jupyterrunning.png">

    - **If jupyter notebook launches, you're all set!**

    <img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691692984__jupyterfilesview.png" width=800px>

    - **If not, follow the instructions on How to Ask for Help from the Installation Overview** 



### 2.4.6) Shut Down Jupyter (Properly)

It is very important that you shut down Jupyter Notebook in the correct way. 

- Closing the web browser tabs for Jupyter Notebook **does not shut down the jupyter notebook!** The notebook is still running in the jupyter server that was launched in your Terminal window. 
- **Do not force-close the Terminal window by closing it if it is running Jupyter!** If you simply X out of Terminal while Jupyter server was running, it can lead to issues with Windows Terminal, such as the "could not fork child process" error in the screenshot below:

<img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691694396__forkchildprocess.png" width=500px>



#### Option A) Shut Down Jupyter From  Jupyter Notebook

- The best way to shut down Jupyter Notebook is from Jupyer's File menu.

<img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691692985__jupyterfilesmenu.png">


- **Click on File > Shut Down**

    <img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691692985__jupyterfilesshutdown.png">

- If a confirmation window appears, click on Shut Down:

<img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691693251__jupytershutdownconfirm.png">

- The terminal running Jupyter should stop running the server and return to an empty prompt, waiting for input.

<img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691620127__jupytershutdown.png">

#### Option B) Shut down jupyter from the terminal

- Return to the Terminal window that you used to start jupyter.
- Press "Control+C" to shut down the server. 
    - The jupyter server should shut down and the prompt should reappear, ready for new commands:
- If you're asked to confirm, respond "y" and press enter.

- The terminal should stop running the server and return to an empty prompt, waiting for input.

<img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691620127__jupytershutdown.png">



#### The moment of truth... 

You are all set for the next step: Testing the Environment!

## Step 2.5) Testing the Environment

To test that your installation and packages are working correctly, You are going to run a specific Environment Testing notebook that is also located in the "dojo-env-setup" folder.

### 2.5.1) Open the environment tester notebook with jupyter notebook

- **Make sure Jupyter Notebook is not running in any Terminal windows.**
    - Check any open terminals and make sure that they are not running the notebook server. 
    - If you see a lot of text in your terminal window and the final line is not an empty command prompt, like in the screenshot below:
    - <img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691620120__jupyterrunning.png">

- **Next, you will close all of your previous Terminal/GitBash windows BUT before you do:**
    - **if your terminal is still running jupyter notebook** and you do not see the prompt waiting for a command:
        - You must press "Control +C" to force-quit jupyter.
        - Make sure to reply "y" if asked for confirmation.
    - If the cursor appears waiting for a new command, you are all set.

- **Now, return to GitHub desktop and click on the "Open in Terminal/GitBash"** to open a terminal in the dojo-env-setup folder.

- **Type pwd to confirm it says dojo-env-setup.**
    - Note: if you do not see the button for Open in Terminal:
        - Click on the menu for "Repository" at the very top of the window (if using Windows) or at the very top of your screen on your menu bar (if using a Mac).

        - You should see the word "Repository" next to the FIle, Edit, View menus.
            - From the Repository menu: click on Open in Terminal/GitBash




- **In the new window that opens, start jupyter notebook** by entering either the full `jupyter notebook` command, or the `jnb` shortcut.

A new tab should open in your web browser that shows the File view for jupyter notebook.

You should see all of the files that were in the dojo-env-folder.

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691542923__jupyterfilesviewtabs.png)

- There are 2 "EnvironmentTester" notebooks:
    - "EnvironmentTester-mac.ipynb" for macs (both Intel and Apple Chip macs)
    - "EnvironmentTester-windows.ipynb" for Windows.

- **Click on the "EnvironmentTester-windows.ipynb" notebook to open it.**

Once the notebook interface has loaded, you should see a toolbar with several menu choices.

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691543038__jupyternotebookview.png)





### Step 2.5.2) Change the notebook's kernel to dojo-env

We want to run all of the cells in this notebook and confirm it can make it to the end without errors.

- First, confirm the notebook is using dojo-env. In the top-right corner you should see "Python (dojo-env)". 

    <img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691543292__jupyternotebooktoolbarannotatekernel.jpg">

- If you do not see Python(dojo-env), click on the name of the kernel displayed to open the Change Kernel menu.

    <img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691543640__jupyterkernelarrow.png">

- Select Python(dojo-env) from the dropdown menu:

    <img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691543640__jupyterdropdown.png">

    <img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691543640__jupyterdropdownselectkernel.png">

    

### Step 2.5.3) Run the environment tester notebook from start to finish.

- **Run the Entire Notebook:**

    - **Select the "Kernel" Menu > "Restart and Run All Cells"**

        - You can also use the toolbar button, which resembles a fast-forward symbol >>.

        <img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691544402__jupyternotebooktoolbarrunall.jpg">

- **Wait patiently.** 

    The testing notebook is going to run through several modeling and EDA steps to confirm that the packages are working correctly.

    - This could take anywhere from 2-20 minutes to run.
    - You will see the web browser tab icon turn to an hourglass when the notebook is running and back to an orange notebook icon when it is done.

- **Scroll down to the bottom of the notebook and confirm the cells have run:**

    - Check if the very last cell printed the success message.

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1657130803__env_tester_final_msg.png)



- If the entire notebook ran successfully

    - Congrats! Your dojo-env is fully functional and you can move on to the next step/lesson!

- If your notebook did not run the entire notebook successfully:

    - You need to contact your instructor or a TA for assistance.
    - Before contacting them, please follow the instructions below to prepare the troubleshooting files to give to your instructor.

- Shut down the notebook by clicking on the **File menu>Close and shut down the notebook.** 

    <img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691543984__closeandshutdownnotebook.png">

## To Get Help Troubleshooting Your Environment. 

#### Download Troubleshooting Files to Share 

- There are 2 files that you should share with your instructor/TA
    1. A copy of your Environment Tester notebook that error'd.
    2. A copy of "FINAL_REPORT.txt" file that is in the Troubleshooting folder of the repo.

1. To share your notebook with an instructor/TA for help:

    - Click File > Save Notebook

    - Click File > Download

    - Your web browser should save a copy of the notebook to your normal "Downloads" folder.

      ​      

        ![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691543895__downloadnotebook.png)

2. To share a copy of your FINAL_REPORT.txt:

    - In the first Files tab that opened when you started jupyter notebook you should see a folder called "Troubleshooting"
    - Click on the Troubleshooting folder.
    - Inside the folder you should have a file called "FINAL_REPORT.txt".
    - Check the checkbox next to the file and click on the "Download" button that appears at the top of the list of files.
    - Your web browser will also save this file to your Downloads folder.

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691544219__downloadfinalreport.png)




### ASK FOR HELP

- **First, please check the "Troubleshooting" chapter on the learnig platform for a lesson that mentions your problem.** about the problem you are running into. (The Troubleshooting section is the 3rd chapter in this course - see the screenshot below)

<img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1658334627__Troubleshooting-chapter.png" width=200px>


​    

- **Second, reach out on the \#[ds-python-installation Discord channel](https://discord.com/channels/738494436467539968/1099094868762042400) with the following info:**
    - A) Which step are you on? (e.g. Step 2.3.3 Confirm the env was created)
    - B) Which OS you are using (e.g. Windows 10, Windows 11, Mac with an mchip, Mac with an Intel processor, etc.)
    - C) Let us know if you've previously installed an older version of Python.
    - D) Attach your copy of the  environment tester notebook and the FINAL_REPORT.txt files.
    - E) Include any additional screenshots of the error/issue you are running into, whenever possible.
    - F) Add any additional details or info you think may be helpful for us to know.
        - For example:
            - "My computer is really old and I think that may be part of the problem."
            - "I share this computer with someone else who also uses python"
            - "This is my work computer and I am not an administrator." etc

- **Third, if you do not receive a response by the end of the day on Discord, please email your instructor with the same information.**
    - An instructor or TA will get back to you within 1 business day with the next steps for you to try.
    - You will most likely need to set up a Zoom call and share your screen for us to help.



___

# Step 3) Jupyter Notebook Preferences

There are several convenient features in Jupyter Notebook that are not enabled by default. We strongly suggest updating your Jupyter Notebook settings according to the instructions below:

### Quick Settings

- Start from the Jupyter files page,
- Open the Settings Menu on the toolbar. 

<img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691609201__01settingsmenuwidecropped.jpg">

- There are several options that you should select, which are highlighted in the screenshot below.

<img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691609201__01settingsmenuoptionstocheck.jpg">



- **Activate the following options:**
    - Autosave Documents
    - Auto Close Brackets
    - Enable Extension Manager
    - Save Widget State Automatically



### In-Depth Settings

- **After selecting these options, click on the Settings Editor at the bottom of the Settings menu.**

<img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691609592__02settingscheckedopensettingsedit.png">

- The large Settings Editor will open and should look like the screenshot below:

<img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691610277__03settingseditor.png">



For each of the settings, you will first click on the correct section on the left sidebar to reveal the options. Then change the settings as directed.

Note: you can use the search box at the top of the left side bar to search for the name of settings. 



### Code Completion

- Check the "Show the documentation panel" option.
- Recommended: do not check the "Enable autocompletion" box to turn on code autocompletion.
    - Instead of Autocompletion, press `Tab` when typing to have jupyter complete your command.

<img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1692379310__settingscodecompletion.png">



### File Browser

- Find "File Browser" on the sidebar.

- Turn on the following options:
    - Show file size column.
    - Show hidden files
    - Use checkboxes to select items

<img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691611467__03settingsfilebrowser.png">

### Notebook

- Open "Notebook" on the sidebar. 

There are many settings on the Notebook settings tab. We have split them into separate steps for clarity:

##### Code Cell Configuration

- **In the "Code Cell Configuration" section, turn on the following options:**
    - Auto Closing Brackets
    - Code Folding
    - Line Numbers
    - Line Wrap
    - Match Brackets
    - Rectangular selection

<img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691611789__03settingsnotebookcodecells.png">`

##### Rulers

Below the check boxes for Code Cell configuration is a Rulers section.

- **Under the Rulers section, click on the "Add" button to add "rulers-0"**
- **Enter 80 in the text field that says ""must be a number"**

<img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691612584__03settingsnotebookwithrulers.png">

#### Indentation options

- Immediately below the Rulers section, make sure that:
    - Smart indentation is turn on.
    - Tab size is set to 4

<img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691615274__03settingsnotebookindentoptions.jpeg">

#### Document Manager

- Find and open ""Document Manager" on the left sidebar.
- Make sure that the following options are turned on:
    - Autosave Documents
    - Ask for confirmation to close a document
    - Rename Untitled File on First Save

<img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691613922__03settingsdocumentmanager.png"> 



### Table of Contents

- Find and open "Table of Contents" on the left sidebar.
- Select the following options:
    - Decrease Maximum headings depth from 4 to 3.
    - Turn on Synchronize collapse state.

<img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691614475__03settingstableofcontents.png">`

#### Shut Down Options

To ensure that jupyter shuts down the notebooks and kernels after closing them, make enable the following 2 shut-down options

- In the left sidebar, search for **"shut down kernel".** 
    - Click on the listing for **Notebook> Shut down kernel** that should appear on the left sidebar.
    - Make sure that **"Shut down kernel" is turned on.**

<img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691614850__03setingsshutdownkernel.png">

- In the left sidebar, search for **"shut down on close"**
    - Click on the listing for **Terminal > Shut down on close** that should appear on the left sidebar.
    - Make sure that **"Shut down on close" is turned on.**

<img src="https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1691615068__03settingsshutdownonclose.png">





- **When you're finished, close the Settings. The options have been saved to Jupyter's configuration files.**



___

# Step 4) Install a Code Text Editor

## Visual Studio Code

- **The final tool to install is a text editor that is designed for programmers.**
- There are several text editors available, but we will be using Visual Studio Code.
- **Visual Studio Code (A.K.A "VS Code")  is a free editor that is highly customizable and supports many languages.**
- It is maintained by Microsoft and has a robust community of extensions and add-ons. It is very popular and is used by many companies (e.g. Facebook/Meta).
- **How will we use VS Code?**
- We could technically run all of our jupyter notebooks using VS Code, but this is not recommended at this point in your education. 
  
    - While VS Code is convenient for quickly opening and working with a repository or viewing a notebook, it has some limitations in how notebooks look and some quirks to the interface for notebooks.
    
- Instead, we will focus on using jupyter notebook or jupyter lab in the lessons and live class.
  
    - You are welcome to try VS Code for notebooks, but it is recommended you become comfortable with jupyter first.
- **We will use VS Code for editing simple code files or hidden files.**
    - We can open and edit the settings file for your terminal (e.g.: "`~/.bash_profile"`.or "~/.zshrc"
    
    - We will use it to create and store credentials for APIs (Stack 4)
    - We can use VS Code to edit your projects' README files while previewing them in real time!
    - Finally, while beyond the scope of the standard curriculum, we can also use VS Code to store functions in external files that we can use just like pandas, matplotlib,

## Step 4.1) Install Visual Studio Code

- Go to https://code.visualstudio.com/

    - It should auto-recognize your OS and have a blue Download button with a version for your OS.
    - Click Download to download the installer.

    - Click on the installer to run it.
    - Select the default options.

- Once Visual Studio Code installation is completed, open it!

    - Check your Start Menu to find Visual Studio Code (VS Code)

        

![png](https://raw.githubusercontent.com/coding-dojo-data-science/dojo-env-setup/main/images/vs_code_get_started.png)

## Step 4.2) Install Python Extensions

- On the left sidebar, there are several icons for different menus.
- Click on the Extensions sidebar icon (5th down, looks like 4 squares).

![png](https://raw.githubusercontent.com/coding-dojo-data-science/dojo-env-setup/main/images/1_extension_sidebar.png)

- On the Extension sidebar, there will be several sections (INSTALLED/POPULAR/RECOMMENDED).
    - Right now you should have nothing under the INSTALLED menu.
    - **You should see the "Python" extension listed under POPULAR.**
        - If not, you can enter "Python" in the search box at the top of the sidebar
        - OR you can click on [this link to the extension ](https://marketplace.visualstudio.com/items?itemName=ms-python.python)on the extension marketplace website.
    - Click on the "Install" button for the Python extension.
        ![png](https://raw.githubusercontent.com/coding-dojo-data-science/dojo-env-setup/main/images/2_extension_installation.png)
- **You must also install the "Jupyter" extension, which you can find with the search bar.**
- Note: the Python extension will also install several required extensions. When installation is complete, you should see the following under the "INSTALLED" section:
    - Python, Pylance, Jupyter Notebook renderer, Jupyter, and Jupyter Keymap

![png](https://raw.githubusercontent.com/coding-dojo-data-science/dojo-env-setup/main/images/3_installed_extensions.png)

## Step 4.3) Setting VS Code to use your `dojo-env` as the default Python installation

- We must teach the Python extension where to find our `dojo-env`'s version of Python.

- On the extension sidebar, click on the Gear icon for the Python extension and select "Extension Settings" ![png](https://raw.githubusercontent.com/coding-dojo-data-science/dojo-env-setup/main/images/4_python_settings.png)

- You should see a new "Settings" pane open in the main window.

    - Take note of the "Default Interpreter Path".
        - It is currently set to just "python".
            ![png](https://raw.githubusercontent.com/coding-dojo-data-science/dojo-env-setup/main/images/5_settings_default_interp.png)

- We need to change this setting to match the exact filepath for our `dojo-env`'s python.

- In your terminal or GitBash:

    - Make sure your dojo-env is activated

    - Run the command: 

        ```
        which python
        ```

        - It will print out a filepath to your dojo-env.
            ![png](https://raw.githubusercontent.com/coding-dojo-data-science/dojo-env-setup/main/images/6_which_python.png)

    - Copy and paste that exact file path into the "Default Interpreter Path" field in the Python extension settings.

![png](https://raw.githubusercontent.com/coding-dojo-data-science/dojo-env-setup/main/images/7_replace_default_interp.png)

### Step 4.4) Test the `code` command

- Open a new terminal or GitBash window.
- Run the command `code` to verify that VS Code opens.
- Note: You can add a specific folder or filename to open, after the word code.
    - To open the current folder `code .`
- If it opens, great!
    - If not, make sure you've opened a new terminal window AFTER installing the code command.

> Congratulations! You are all set up with your local python environment! 

# Final Notes

Congrats! You've got a fully functional professional data science environment on your local machine!

- **Please see the next chapter "Working Locally" for:**
    -  a walkthrough of how to use your new local installation and tools together
    -  a summary of terminal commands
    -  jupyter notebook cheat sheets
    -  how to install additional packages
    -  & more!

- **Please see the "Troubleshooting" chapter for commonly encountered errors and any known solutions. including:**
    - Reinstalling your dojo-env
    - "code" command not working
    - GitBash "Could not fork child process" error

## Enjoy your new dojo-env! 



### References

[Image Source: Anaconda](https://en.wikipedia.org/wiki/Anaconda_(Python_distribution)](https://en.wikipedia.org/wiki/Anaconda_(Python_distribution)) ;

[Image Source: GitHub Desktop](https://commons.wikimedia.org/wiki/File:Github-desktop-logo-symbol.svg) ;

[Image Source: GitBash](https://appuals.com/what-is-git-bash/);

[Image Source: Windows Terminal](https://commons.wikimedia.org/wiki/File:Windows_Terminal_Logo.png)
