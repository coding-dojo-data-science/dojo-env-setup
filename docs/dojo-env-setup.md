# dojo-env-setup

![img](https://file+.vscode-resource.vscode-cdn.net/Users/codingdojo/Documents/GitHub/dojo-env-setup/images/Data%20Science%20Thumbnail.png)

## Installation Overview

So far in this program, you have been working in Google Colab which provides a cloud-based coding environment. We will be transitioning to using a Python environment stored on your local machine. You will be working in Jupyter Notebook, which is very common in the data industry. In addition, these instructions will include the installation of Github Desktop and Visual Studio Code (VS Code).

- We recommend you begin the step-by-step installation **AS SOON AS POSSIBLE** to ensure you have time to troubleshoot any difficulties you may encounter.

- If you run into issues during installation, post your questions/issues on the [ds-python-installation ](https://discord.com/channels/738494436467539968/999108307627294770)Discord channel, and tag your instructor in your question (e.g. @dojo_Instructor_name).

- **These steps should take ~30-90 minutes,** depending on the speed of your machine and internet connection.

------

**By the end of this chapter, you will:**

1. Install GitHub Desktop: 
   - App for working with and managing git repositories.
2. Set up your Terminal/or "shell":
   - The primary application you will use to execute coding-related commands.
3. A Python Distribution:
   - The fundamental infrastructure for installing Python.
   - Install Python via Anaconda on Windows + Intel Macs or mini forge on Macs with an Apple chip)
4. Create our custom Python **environment** (dojo-env)
   - A collection of compatible packages.
5. Install & set up Jupyter Notebook / Jupyter Lab
   - The primary editor we will use (instead of Colab).
6. Install Visual Studio Code.
   - A special text editor designed for code. It has many extensions and languages available.
   - We will use it to edit special files, but it can also run notebooks too!

## OS-Specific Steps/Commands

**For several steps (e.g. Step 1), there are multiple versions of the instructions, depending on what operating system you are using.** (i.e. a Windows computer, vs a Mac with an Intel processor, vs a Mac with an Apple Chip (m1/m1pro/m2/etc).)

>  Please make sure you select the correct instructions page for your OS!

### Currently Supported Operating Systems

- We have prepared environment files (.yml files) for 4 different OS configurations:
  - Windows (10 & 11)
  - Mac (with Intel processors)*
  - Mac (Apple Chips)*
  - Linux**

#### *Note for Mac users - if you don't know which type of Mac you have :

- Check the "About this Mac" screen for your computer.
  - Click on the Apple symbol on the top-left corner of your screen.
  - **Click About This Mac.**
  - A window with your computer's specs will appear like the one in the screenshot below
    - ![img](https://file+.vscode-resource.vscode-cdn.net/Users/codingdojo/Documents/GitHub/dojo-env-setup/images/lp/About_this_Mac_-Intel.png)
  - If it has a "Processor" line that says "Intel" you should follow the Instructions: Mac (Intel Processor).
  - If it has a "Chip" line that says "Apple" then you should follow the Instructions: Mac (Apple Chip).

#### **Note to Linux Users:

- Our Linux installation instructions are still in beta. While they have successfully been installed on students' Linux machines, we currently do not have a Linux machine available for troubleshooting.
  - The beta Linux instructions are located [here ](https://login.codingdojo.com/m/213/13909/99742)and all steps are combined into 1 lesson.

------

## Instructions

- [Windows](https://file+.vscode-resource.vscode-cdn.net/Users/codingdojo/Documents/GitHub/dojo-env-setup/docs/instructions-windows-v23.md)
- [Mac-Apple Chip (m1,m2,etc.)](https://file+.vscode-resource.vscode-cdn.net/Users/codingdojo/Documents/GitHub/dojo-env-setup/docs/instructions-mac-mchip-v23.md)
- [Mac-Intel](https://file+.vscode-resource.vscode-cdn.net/Users/codingdojo/Documents/GitHub/dojo-env-setup/docs/instructions-mac-intel-v23.md)
- `Coming soon!` Linux[]]()

------

## Reference: Helpful Commands

### Installation Commands

- To activate dojo-env and add it to Jupyter (after installation)

```bash
conda activate dojo-env               
python -m ipykernel install --user --name dojo-env --display-name "Python (dojo-env)"
```

- To re-add `conda` command:

```bash
conda init 
```

### Uninstall commands

#### Uninstall dojo-env

- To remove the current dojo-env:

```bash
conda activate base                             
conda remove --name dojo-env-ds --all
```

- Then answer `y` for yes

------

### Setting Default Env

#### For Mac Users (using the default terminal - zsh)

```bash
touch ~/.zshrc
echo "conda activate dojo-env" >> ~/.zshrc
echo 'alias jnb="jupyter notebook"' >> ~/.zshrc
echo 'alias lab="jupyter lab"' >> ~/.zshrc
```

#### For Windows Users (or mac users who switched to bash)

- To set dojo-env as the default Python env and add Jupyter shortcuts

Note: you may need to replace `~` with the full path to your user folder. (e.g. "/Users/codingdojo/.bash_profile" instead of "~/.bash_profile")

```bash
touch ~/.bash_profile
echo "conda activate dojo-env" >> ~/.bash_profile
echo 'alias jnb="jupyter notebook"' >> ~/.bash_profile
echo 'alias lab="jupyter lab"' >> ~/.bash_profile
```

------

### Managing Jupyter Kernels

- To see the list of kernels that jupyter will display as options:

```bash
jupyter kernelspec list 
```

- To remove a kernel that no longer exists (replace `<kernel name>` with name of kernel from the jupyter kernelspec list command ):

```bash
jupyter kernelspec remove <kernel name>
```