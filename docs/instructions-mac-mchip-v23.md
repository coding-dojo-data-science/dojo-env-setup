# Mac (Apple Chip) Installation Overview

So far in this program, you have been working in Google Colab which provides a cloud-based coding environment. We will be transitioning to using a Python environment stored on your local machine. You will be working in Jupyter Notebook, which is very common in the data industry. In addition, these instructions will include the installation of Github Desktop and Visual Studio Code (VS Code). 

- In the Advanced Machine Learning course, you will need to submit a CORE ASSIGNMENT containing the error-free test notebook that is included within these instructions. This will ensure that you have the tools you will need to be successful. 

- We recommend you begin the step-by-step installation AS SOON AS POSSIBLE to ensure you have time to troubleshoot any difficulties you may encounter. 

- If you run into issues during installation, post your questions/issues on the [ds-python-installation](https://discord.com/channels/738494436467539968/999108307627294770) Discord channel, and tag your instructor in your question (e.g. @dojo_Instructor_name).

- These steps should take ~30-90 minutes, depending on the speed of your machine and internet connection.

- The [dojo-env-setup repository](https://github.com/coding-dojo-data-science/dojo-env-setup), which you will clone in Step 2.1, contains a backup copy of the entire set of instructions on the README, for convenience.

------

> Note: if you previously installed the dojo-env and are upgrading to the current version, please see the "Updating to New dojo-env" at the end of this chapter (after the Final Notes lesson)

By the end of this chapter, you will:

1. Install GitHub Desktop,
2. Install Python via miniforge (Non Apple-chip macs and Windows use the larger version: Anaconda)
3. Create a special Python environment (dojo-env)
4. Supercharge Jupyter Notebooks with Extensions
5. Install Visual Studio Code.

## If you encounter an error during installation:

- First, read a little further down in the instructions to make sure we do not already address the error message that you ran into.

- Second, please check the "Troubleshooting" chapter for a lesson about the problem you are running into.

  (The Troubleshooting section is the 3rd chapter in this course - see the screenshot below)

  

  ![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1658334627__Troubleshooting-chapter.png)

- Third, reach out on the #ds-python-installation Discord channel (Link) with:

  - What step you are on (e.g. Step 2.3 Creating the dojo-env)
  - What OS you are using (e.g. Windows 10, Windows 11, Mac with an Apple Processor, etc)
  - Screenshots of the error/issue you are running into, whenever possible.
  - Finally, if you have been able to run the test notebook in Step 2.4: Testing the Env, please upload these files with your question.
  
- Fourth, if you do not receive a response by the end of the day on Discord, please email your instructor.

------

## OS-Specific Steps/Commands

#### *Note for Mac users - if you don't know which type of Mac you have :

- Check the "About this Mac" screen for your computer.
  - Click on the Apple symbol on the top-left corner of your screen.
  - Click About This Mac.
  - A window with your computer's specs will appear like the one in the screenshot below
    - ![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1656714456__About%20this%20Mac%20-Intel.png)
  - If it has a "Processor" line that says "Intel" you should follow the Instructions: Mac (Intel Processor).
  - If it has a "Chip" line that says "Apple" then you should follow the Instructions: Mac (Apple Chip).

------

Regardless of OS, you will be using tools that serve the following purposes:

- Your "Terminal"/"Shell":
  - The primary application you will use to execute coding-related commands.
- A Python Distribution:
  - The fundamental infrastructure for installing Python.
- GitHub Desktop:
  - App for working with and managing git repositories.
- Our custom Python Environment (dojo-env)
  - A bundle of packages required for stacks 1-5+
- Jupyter Notebooks / Jupyter Lab
  - The primary editor we will use (instead of Colab).
- Visual Studio Code
  - A special text editor designed for code. It has many extensions and languages available.
  - We will use it to edit special files, but it can also run notebooks too!

------

# 1. Downloading and Installing Required Apps

> Before we install our python environment, we need to take care of a couple requirements. 

In step 1, we will install:

- Your "Terminal"/"Shell": 
  - The primary application you will use to execute coding-related commands.
- A Python Distribution (miniforge):
  - The fundamental infrastructure that will allow us to install Python.
- GitHub Desktop:
  - The way we will work with git repositories and the starting point for our local workflows.

# Step 1 - MacOS (Apple Chip)

## Preface: Good News and Bad News

So...you got one of those shiny new(ish) Mac computers with an Apple chip, eh? We've got some good news and bad news for you.

The good news:

- Your python code will run blisteringly fast compared to a Mac with an Intel chip!
- Code that may take hours elsewhere will only take minutes for your computer.

The bad news:

- Your instructions for Tool #3 below (the Python Distribution) are going to be very different than the other operating systems.

- Additionally, there are still packages that have not yet been updated to be compatible with your processor.

  But don't worry: everything that is in the other OS's dojo-env is also in yours! Just a heads up if you try to install a new package and run into issues.

------

# STEP # 1 INSTRUCTIONS:

Note: steps for Tools # 1 and 2 are the same for Mac users with an Intel processor.

## Tool #1: A Linux-based bash shell/terminal:

- Linux users and MacOS users have this built-in to their OS.
  - On MacOS, the shell is called "Terminal" and can be found in `Applications>Utilities` in Finder
  - OR you can use spotlight search and search for "Terminal".

### Tool #2: GitHub Desktop

- Download the installer from this link: [GitHub Desktop](https://desktop.github.com/)
- Once installation is complete, open the application.
  - Log into the same GitHub account you have been using for your projects.
- Once you have logged into the app, open the Options menu
  - Select `"GitHub Desktop"` on the menu bar (top of the screen) and then select `Preferences`.
  - Select the "Integrations" tab.
  - Make sure the Shell dropdown menu says "Terminal"
    - If not, select it from the dropdown menu.
  - Click Save.

------

> Note: Here is where the instructions for Apple Chips will significantly deviate from the others.

- **The primary difference is that in order for us to use Apple-Chip compatible versions of packages (like TensorFlow), we CAN NOT use the standard Anaconda distribution.**
- There is a lightweight alternative to Anaconda, called miniforge, that will install much of the same foundations as Anaconda, but with access to alternative versions of packages that are optimized for Apple Chips.
  - Note/Warning: you would still be *able* to install Anaconda if you tried, but your computer will never be able to run TensorFlow if you use Anaconda. So please, take our word for it that it is worth following our alternative instructions
- The following instructions are based on [this blog post](https://caffeinedev.medium.com/how-to-install-tensorflow-on-m1-mac-8e9b91d93706), should you wish to review it in-depth.

### Pre-Tool #3 Verification:

**VERIFY THAT ANACONDA IS NOT ALREADY INSTALLED ON YOUR COMPUTER.**

- Open a terminal window and run the "conda" command (without quotation marks).
- If it says conda not found, great! You're ready to install miniforge.
- If it shows a list of available conda commands:
  - You **MUST FOLLOW THE APPENDIX INSTRUCTIONS AT THE BOTTOM OF THIS LESSON FOR "Uninstalling Anaconda"** BEFORE YOU PROCEED!

- CRITICAL NOTE:

  - IF YOUR TERMINAL RECOGNIZED THE CONDA COMMAND ANACONDA MUST BE REMOVED BEFORE INSTALLING MINIFORGE.

  - > Failure to heed this warning will break all of your python environments and it is NOT easy to fix!!!

## Tool #3: Python Distribution - miniforge

Tool # 3 will involve several steps with several verification steps along the way. Make sure to follow each Step and Verification step below to ensure you have a problem-free python installation.

### Step 1: Install XCode (a Mac-specific developer toolkit from Apple)

- Run the command below in your Terminal.
  - Note: this step may take several minutes
  - You may be asked to enter your password to approve the installation. This is your normal user password to log into your computer.
- ```
  xcode-select --install
  ```

### Step 2: Install Homebrew ( a database of downloadable apps/tools for Mac)

Visit https://brew.sh/ for more information about Homebrew

- To Install homebrew, run the following command in your Terminal (and make sure to read the steps below):

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- You may be asked to enter your password in your terminal.
  - This is the same password you use to log into your mac.
  - Enter your password when prompted and hit Enter.
    - NOTE: You will not be able to see what keys you have typed, so just trust that it is recognizing your keystrokes and hit enter. It will notify you if the password was incorrect.
- The installation process will pause and ask you "Press RETURN to continue or any other key to abort".
  - When it does, press Return/Enter!
- Step 2B: CRITICAL NOTE
  - When homebrew has finished installing, it may display a message telling you to run 1 or 2 commands in your Terminal. That looks something like this:
    `echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc`
  - **It is very important that you run those commands, otherwise, your terminal will not know that homebrew has been installed.**

### Step 2 Verification:

Confirm that homebrew was successfully installed:

- Open a New Terminal Window (shortcut: Cmd+N or Cmd+T) and run the "`brew`" command.
  - If it lists available commands, great!  You're all set to move forward.
  - If it says brew not found:
    - You may have missed the commands to paste at the end of the homebrew installation.
    - Try installing homebrew again and make sure to pay attention to the final text that's displayed and follow any additional instructions it displays.

## Step 3: Install miniforge using homebrew.

### Step 3 Commands:

- Enter the brew installation command below in your terminal:

```
brew install miniforge
```

- Once miniforge has finished installing, run the following command in your terminal (required for Matplotlib):

```
brew install pkg-config
```

- Enter the following command to add the "conda" command to Terminal

```
conda init zsh
```

### Post-Step 3 Verification

- Open a new terminal window and enter the "conda" command.
  - If it lists available commands, fantastic!!
    - You are all set to move on to the next page of instructions "2. Setting Up Your dojo-env Environment"!!
  - If it says conda not found, try restarting your computer and then try running the conda command again.
    - If it still says conda not found, reach out to your instructor or a TA for help ASAP.



------

------

## APPENDIX: UNINSTALLING ANACONDA

If your computer already knew the conda command during "Pre-Step 3 Verification", it is critical that you remove anaconda before continuing with the miniforge installation.

Pre-Uninstallation Verification Step:

- If you share your computer with another User who also uses Python:
  - Pause here and check with them BEFORE you uninstall anaconda. You will be removing all of their python environments too, even though they have a separate User account.

- If you share your computer with someone and they have concerns about uninstalling anaconda:

  - Stop here (for now)

    .

    - Do not move forward with the instructions until you have spoken with your instructor.
    - Your instructor may be able to address concerns that your fellow User has and convince them to let you install miniforge.

- Alternatively, you could follow the Step 1 - MacOS (Intel Processor) instructions instead but:
  - Your python code will run slower than it would with miniforge.
  - You will not be able to import tensorflow without your kernel crashing.

- Your instructor may be able to address concerns that your fellow User has and convince them to let you install miniforge.

#### Official Steps for Fully Uninstalling Anaconda:

The following steps are taken directly from the [Official Uninstalling Anaconda documentation page](https://docs.anaconda.com/anaconda/install/uninstall/), specifically "Option B. Full uninstall using Anaconda-Clean and simple remove."

- Install the Anaconda-Clean package from Anaconda Prompt (terminal on Linux or macOS):

```
conda install anaconda-clean
```

- In the same window, run the following command:

```
anaconda-clean --yes
```

- Once the process has been completed, manually delete any "anaconda3" or "anaconda2" folders that still exist.
  - It may be located in one of several possible folders. Run the following "ls -a" commands until you see a folder called "anconda2" or "anaconda3".
  - Once you see an anaconda folder, take note of:
    - Which command showed the folder.
      - Specifically, what did the command say after "ls -a"
      - We will refer to this as your "base folder" in the final step.
    - If the anaconda folder was "anconda2" or "anaconda3"
      - We will refer to this as your "anaconda folder" in the final step.
  - and jump to the very last command at the bottom of the page, with those 2 pieces of information.

```
ls -a ~/
ls -a ~/opt/
ls -a /opt/
```

- Run the final command to remove the anaconda folder once you've identified your "base folder" and "anaconda folder".

  - Replace {base_folder} with the actual folder name

  - Replace {anaconda_folder} with the actual folder name.

```
rm -rf {base_folder}{anaconda_folder}
```



Once you've replaced the placeholder folder names with your actual folder names, the command should look something like this:

```
rm -rf ~/opt/anaconda3
# or 
rm -rf ~/anaconda2
# or 
rm -rf ~/opt/anaconda3
```

#### 

#### Final Verification Step:

- Now, open a new terminal window and try running the "conda" command again. Your terminal should say that conda is not found.

  - If it says conda is not found, you are now ready to jump back up to the "Step 3 Commands" header above.

  - If your computer still displays a list of conda commands: please see the final portion of the [Official Uninstallation Instructions "Removing Anaconda from .bash_profile"](https://docs.anaconda.com/anaconda/install/uninstall/#removing-anaconda-path-from-bash-profile), which is illustrated below:

- Open the two settings file for your terminal and remove anything related to anaconda:

  - 1) Run the "open ~/.bash_profile" (without quotation marks) command and a text editor window should open.

    - Examine the contents of this file and delete any lines that look like either of the screenshots below:
      - 
        ![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1659740063__conda_init_code.png)
      - ![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1659740131__Screen%20Shot%202022-08-05%20at%206.55.05%20PM.png)
    - Save the file and close it.

  - 2. Now repeat the process, but use the "open ~/.zshrc" (without quotation marks) command

    - Delete any lines of code that look like the screenshots above.
    - Save the file and close it.



- FInal Verification:
  - Open a New Terminal Window (the changes you made above only take effect when opening a new window)
  - Run the "conda" command again and you should now see a message that says "conda not found"
    - If you are still seeing the list of conda commands instead, re-open the two files listed above and make sure you saved them after deleting the lines of code.
    - Close your terminal window and open a new one and try the "conda" command again.



- If the conda command still displays the list of commands after the steps above:
  - Try restarting your computer and attempting to run the command one more time.
  - If you are still seeing conda commands:
    - You should post your problem on the [ds-python-installation](https://discord.com/channels/738494436467539968/999108307627294770) discord channel for a TA or instructor to assist you.
    - You should also email your instructor about the issue.



# 2. Setting Up Your dojo-env Environment

## Step 2 Overview:

In Step 1, we installed the foundational tools needed for our local python installation. 

While we did install a Python distribution with a basic copy of Python (Anaconda or miniforge), we have not installed all of the packages and tools that we need as data scientists.

In Step 2, you will be creating a custom python environment called "dojo-env". 

An "environment" is a bundle of specific python packages that are used together. Importantly, an environment specifies specific version #'s of the packages to ensure that all of the versions installed are mutually compatible.

- You can install many environments on your computer and switch between them as needed for different projects.

- We have designed the dojo-env to include everything you'd need for our program, so you may not have a reason to add additional environments. 

- The environment files (and a backup of these instructions) are in the [dojo-env-setup repository](https://github.com/coding-dojo-data-science/dojo-env-setup)
- The Detailed Instructions below will guide you through how to clone and use the environment setup repository.



## Brief Summary of the Following Steps:

- Step 2.1: Clone the dojo-env-setup repository
- Step 2.2: Open the repo in your terminal/GitBash
- Step 2.3: Create the dojo-env environment
- Step 2.4: Setting dojo-env as your default.

# Step 2.1 Clone the dojo-env-setup repository

1. Open the dojo-env-setup repository on GitHub.com:

   1.  https://github.com/coding-dojo-data-science/dojo-env-setup

2. Make sure that :

   1. you are logged in to your account on GitHub.com 
   2. and you are logged into the SAME account in the GitHub Desktop app (that you installed in step 1.)

3. Click on the green `Code` button and then click `Open in GitHub desktop.`

   1. GitHub desktop should open automatically 

      and ask you what folder you would like to store your repository in.

      

      ![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1656806399__clone-repo-menu.png)

      

      1. Troubleshooting Note: if you are brought to the Download GitHub Desktop web page instead:
         1.  It means you were not logged into the same account on GitHub.com and GitHub Desktop when you clicked Open in GitHub Desktop. 
            1. Make sure you see your user profile pic in the top right of GitHub.com 
            2. and check your Account in GitHub Desktop's Preferences/Options menu.
            3. and then try again.

   1. By default, GitHub Desktop

       

      will use a new "GitHub" folder in your Documents folder

      1. GitHub Desktop will create a NEW folder with the same name as the repository INSIDE of whichever folder you select.

      2. If you use the default options, then this will create a "dojo-env-setup/" folder inside of "Documents/GitHub/"

      3. Note: it is strongly recommended that you use the Documents/GitHub folder for this repository.

         

         1. But if you'd rather save the folder somewhere else:

            1. Use the "Choose" button (the button name may be "Browse" on Windows).

            2. A window should pop up for you to find and click on the folder where you want to create the "dojo-env-setup" folder.

            3. Once you have selected a new folder using the Browse button, you should see the full folder path displayed.

            4. IMPORTANT STEP: Make sure to remember the full file path of the folder you selected! 

               (See the screenshot below. )

               1. ![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1656806548__clone-repo-menu%20annotated.png)



# Step 2.2: Open the Repo in Terminal/GitBash

## Open the Repo in Terminal (mac) or GitBash (windows)

Once you have cloned the repository, you will need to open a terminal/gitbash window in the same folder as the repository.

- Open a new terminal in the dojo-env-setup folder

  - First, in GitHub Desktop: make sure the left sidebar says "dojo-env-setup" in the top-left corner under Current Repository.

  - Click on the Repository menu and select "`Open in terminal`" or "`Open in gitbash`"
    - Windows Users: the menu will be at the top of GitHub Desktop's window.
    - Mac Users: the menu will appear at the very top of your screen (your menu bar).
  - Alternatively, you can use the keyboard shortcut to do the same thing. The command for both Mac and Windows is:
    - Control + ` (the key above tab that also has the tilde symbol ~)

- In the terminal window that appears, type the "pwd" command (stands for print working directory) and press Enter.

  - It will display the folder name of the folder your terminal is currently located. 
    - The folder path should end in "dojo-env-setup/"
    - If you used the default GitHub folder when you cloned dojo-env, the full filepath would be something similar to "/Users/yourname/Documents/GitHub/dojo-env-setup/"

## Verify Step 2.2

Run one last command to verify that you are indeed in the correct folder. 

Run the "ls -a" command to see a detailed list of all files in the repo.

```
ls -a
```

You should see a list of all the files in the current folder. 

If you are in the right folder, you should see 3 files that start with "environment" and end with ".yml" like in the screenshot below.

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1656808093__dojo-env-setup%20ls%20result.png)

If so, you are all set for the next step: create the dojo-env environment!

# Step 2.3 Create the dojo-env environment

###  1) Create the dojo-env using the correct "conda create" command for your OS

- Run the  conda env create command below in your Terminal

#### MacOS with an Apple Chip

```
conda env create -f environment-ds_mac_mchip.yml
```



### Wait (patiently) for the dojo-env to be created. 

- It can take anywhere from 3-20 minutes to finish create the environment, depending on your computer and internet connection.
- You will see several progress bars during the process. Once it has been completed you should see a message that says

```
# To activate this environment use:
 conda activate dojo-env
# To deactivate this environment use:
 conda deactivate 
# If conda deactivate doesn't work, activate the "base" env
 conda activate bases
```

- Confirm your environment was installed and activate it.

  - Enter the following command  to display the list of your locally installed environments.

    ```
    conda env list
    ```

    - You should see 2 environments, including dojo-env:
      - `base`
      - `dojo-env`

- If you see dojo-env in the list:

  - Success! dojo-env was successfully created! But we aren't using it yet just yet. We must first "activate" an environment to determine which version of python & packages are currently being used.

### 2) Activate the dojo-env and Install the Env in Jupyter

- The first line in the code block below will switch to dojo-env.
- The second line will install dojo-env as an option in Juyter Notebook/Lab, which you will use instead of Google Colab when working locally.

```
conda activate dojo-env
python -m ipykernel install --user --name dojo-env --display-name "Python (dojo-env)"
```

# Step 2.4: Setting dojo-env as the default + alias commands

This section will require you to enter several commands in your Terminal.

- Make sure that your terminal is not running jupyter notebook (you can press "`Cntrl`+`C`" to force quit the server from your terminal).

- Alternatively, you can open a new terminal. (You can perform these steps from any folder.)

------

### Determining If your Shell is Bash or Zsh

- First, you need to confirm what type of shell your terminal is using. There are 2 possible options that your mac may be using: `zsh` or `bash`. You most likely have `zsh` if you have an Apple chip.

- In your terminal, type the follwing command and hit enter.

```bash
echo $SHELL
```

- You will see a file path displayed in the terminal (e.g. /bin/zsh ). Take note of the last few letters of the file path and select the correct option (A or B) below:

------

### 1A) If the response ends in bash

- Run the following commands to automatically activate dojo-env and to add shortcuts for Jupyter:

```
touch ~/.bash_profile
echo "conda activate dojo-env" >> ~/.bash_profile
echo 'alias jnb="jupyter notebook"' >> ~/.bash_profile
echo 'alias lab="jupyter lab"' >> ~/.bash_profile
```

------

### 1B) If the response ends in zsh:

- Run the following commands to automatically activate dojo-env and to add shortcuts for Jupyter:

```
touch ~/.zshrc
echo "conda activate dojo-env" >> ~/.zshrc
echo 'alias jnb="jupyter notebook"' >> ~/.zshrc
echo 'alias lab="jupyter lab"' >> ~/.zshrc
```

# Part 2) Final Verification Steps

### Confirm `dojo-env` is your default

To confirm that dojo-env is now your default environment:

- Open a Terminal window.
- You should see `(dojo-env)` appear next to your prompt automatically.

## 

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1647634446__confirm_dojo_env.png)

## 

### Confirm the shortcut aliases work

- Try running the command "lab" in your terminal/kitbash.

  - If jupyter lab launches, you're all set!

  - If not, contact your instructor or a TA for assistance.

- Shut down jupyter from the terminal
  - Return to your Terminal window that you used to start jupyter.
  - Press Control+C to shut down the server. 
  - Respond "y" when asked to confirm.

## Note: you can still move on to the next step even if you could not successfully complete this step.

- These steps are for convenience and are not strictly required.
- You should still contact your instructor or a TA for assistance to successfully complete this step at your earliest convenience.

___



## The moment of truth... 

You are all set for the next step: Testing Your New Environment!

# Step 2.5: Testing the Environment

To test that your installation and packages are working properly. We are going to run a specific Environment Testing notebook that is also located in the "dojo-env-setup" folder.

## Running the environment tester notebook with jupyter lab

- Now, return to GitHub desktop and click on the "Open in Terminal" to open a terminal in the dojo-env-setup folder.

- Type `pwd` to confirm it says dojo-env-setup.

- - Note: if you do not see the button for Open in Terminal:

  - - Click on the menu for "Repository" at the very top of your screen on your menu bar.
      - You should see the word "Repository" next to the FIle, Edit, View menus.
    - From the Repository menu: click on Open in Terminal.



- In the new window that opens, start jupyter notebook by entering the `jupyter lab` command in your terminal (or the "lab" shortcut!)

A new tab should open in your web browser that shows the File view for jupyter notebook.

You should see all of the files that were in the dojo-env-folder:

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1657130012__jupyter_file_view.png)

There are 2 "EnvironmentTester" notebooks:

- "EnvironmentTester-mac.ipynb" for macs (both Intel and Apple Chip macs)
- "EnvironmentTester-windows.ipynb" for Windows.

- Click on the EnvironmentTester-mac.ipynb notebook to open it.

Once the notebook interface has loaded, you should see a toolbar with several menu choices.



###  ✅ TO DO: NEW SCREENSHOTS

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1657130146__jupyter_notebook_view.png)



- We want to run all of the cells in this notebook and confirm it can make it to the end without errors.

- To Run the Entire Notebook:

  - Select the "Kernel" Menu > "Restart and Run All"

  - Wait patiently. 

    The testing notebook is going to run through several modeling and EDA steps to confirm that the packages are working correctly.

    - This could take anywhere from 2-10 minutes to run.
    - You will see the web browser tab icon turn to an hourglass when the notebook is running and back to an orange notebook icon when it is done.

- Scroll down to the bottom of the notebook and confirm the cells have run:
  - Check if the very last cell printed the success message.

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1657130803__env_tester_final_msg.png)

- If the entire notebook ran successfully
  - Congrats! Your dojo-env is fully functional and you can move on to the next step/lesson!

- If your notebook did not run the entire notebook successfully:
  - You need to contact your instructor or a TA for assistance.
  - Before contacting them, please follow the instructions below to prepare the troubleshooting files to give to your instructor.

### To Get Help Troubleshooting Your Environment.

- There are 2 files that you should share with your instructor/TA
  1. A copy of your Environment Tester notebook that error'd.
  2. A copy of "FINAL_REPORT.txt" file that is in the Troubleshooting folder of the repo.

1. To share your notebook with an instructor/TA for help:

   - Click File > Save & Checkpoint.

   - Click File > Download As > Notebook (.ipynb)

   - Your web browser should save a copy of the notebook to your normal "Downloads" folder.

     

     ![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1657132437__download_as.png)

2. To share a copy of your FINAL_REPORT.txt:

   - In the first Files tab that opened when you started jupyter notebook you should see a folder called "Troubleshooting"
   - Click on the Troubleshooting folder.
   - Inside the folder you should have a file called "FINAL_REPORT.txt".
   - Check the checkbox next to the file and click on the "Download" button that appears at the top of the list of files.
   - Your web browser will also save this file to your Downloads folder.

![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1657132692__download_report.png)

- Send an email to your instructor 
  - Attach the 2 files listed above. They are located in your Downloads folder.
  - Add any additional details or info you think may be helpful for us to know.
    - For example:
      - "my computer is really old and I think that may be part of the problem."
      - "I share this computer with someone else who also uses python"
- An instructor or TA will get back to you within 1 business day with the next steps for you to try.
  - You will most likely need to set up a Zoom call and share your screen for us to help.



# Step 3: Install a Code Text Editor

## Visual Studio Code

- The final tool to install is a text editor that is designed for programmers.

  - There are several text editors available, but we will be using Visual Studio Code.

- Visual Studio Code (A.K.A "VS Code") 

  is a free editor that is highly customizable and supports many languages.

  - It is maintained by Microsoft and has a robust community of extensions and add-ons.
  - It is very popular and is used by many companies (e.g. Facebook/Meta)



- How will we use VS Code?

  - We could technically run all of our jupyter notebooks using VS Code, but this is not recommended at this point in your education. 

    - While VS Code is convenient for quickly opening and working with a repository or viewing a notebook, it has some limitations in how notebooks look and some quirks to the interface for notebooks.

    - Instead, we will focus on using

       jupyter notebook or jupyter lab in the lessons and live class.

      - You are welcome to try VS Code for notebooks, but it is recommended you become comfortable with jupyter first.

- We will use VS Code for editing simple code files or hidden files.

  - We can open and edit the settings file for your terminal (e.g.: "`~/.bash_profile"`.or "~/.zshrc"

  - We will use it to create and store credentials for APIs (Stack 4)
  - We can use VS Code to edit your projects' README files while previewing them in real time!
  - Finally, while beyond the scope of the standard curriculum, we can also use VS Code to store functions in external files that we can use just like pandas, matplotlib,





## Install Visual Studio Code

- Go to https://code.visualstudio.com/

  - It should auto-recognize your OS and have a blue Download button with a version for your OS.
  - Click Download to download the installer.

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
    - OR you can click on [this link to the extension ](https://marketplace.visualstudio.com/items?itemName=ms-python.python)on the extension marketplace website.
  - Click on the "Install" button for the Python extension.
    ![png](https://raw.githubusercontent.com/coding-dojo-data-science/dojo-env-setup/main/images/2_extension_installation.png)
- Note: the Python extension will also install several required extensions. When installation is complete, you should see the following under the "INSTALLED" section:
  - Python, Pylance, Jupyter Notebook renderer, Jupyter, and Jupyter Keymap

![png](https://raw.githubusercontent.com/coding-dojo-data-science/dojo-env-setup/main/images/3_installed_extensions.png)

## Setting VS Code to use your `dojo-env` as the default Python installation

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

### Add the `code` command to your terminal

We want to be able to type the word "code" in our terminal and have that open up VS Code.

1. Open the Command Palette:
   - Either click on View in the menu bar and select "Command Palette"
   - OR use the keyboard shortcut (`Cmd` + `Shift` +`p`)
2. In the small pop-up window, type "install code" and you should see it auto-suggest the option for "Shell Command: Install 'code' command in PATH".
   - Click on this option.

![png](https://raw.githubusercontent.com/coding-dojo-data-science/dojo-env-setup/main/images/8_install_code_command.png)

### Test the `code` command

- Open a new Terminal window.
- Run the command `code` to verify that VS Code opens.
- Note: You can add a specific folder or filename to open, after the word code.
  - To open the current folder `code .`
- If it opens, great!
  - If not, make sure you've opened a new terminal window AFTER installing the code command.

> Congratulations! You are all set up with your local python environment! 
> You may want to read the Final Notes + Appendix lesson so that you are aware of the contents, in case you need them.

# Final Notes

## 

Congrats! You've got a fully functional professional data science environment on your local machine!

- Please see the next chapter "Working Locally" for:
  -  a walkthrough of how to use your new local installation and tools together
  -  a summary of terminal commands
  - jupyter notebook chgeat sheets
  - how to install additional packages
  -  & more!

- Please see the "Troubleshooting" chapter for commonly encountered errors and any known solutions. including:
  - Reinstalling your dojo-env
  - "code" command not working
  - GitBash "Could not fork child process" error

