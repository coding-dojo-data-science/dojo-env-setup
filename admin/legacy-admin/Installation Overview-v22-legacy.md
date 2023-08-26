# [v23] Installation Overview

So far in this program, you have worked in Google Colab, which provides a cloud-based coding environment. We will transition to using a Python environment stored on your local machine. You will work in Jupyter Notebook, which is very common in the data industry. In addition, these instructions will include the installation of Github Desktop and Visual Studio Code (VS Code).

### TIMELINE/DEADLINE

- In the Advanced Machine Learning course, you will need to submit a CORE ASSIGNMENT containing the error-free test notebook that is included within these instructions. This will ensure that you have the tools you will need to be successful.
- We recommend you begin the step-by-step installation AS SOON AS POSSIBLE to ensure you have time to troubleshoot any difficulties you may encounter.
- If you run into issues during installation, post your questions/issues on the [ds-python-installation](https://discord.com/channels/738494436467539968/1099094868762042400) Discord channel, and tag your instructor in your question (e.g. @dojo_Instructor_name).
- These steps should take ~30-90 minutes, depending on the speed of your machine and internet connection.
- The [dojo-env-setup repository](https://github.com/coding-dojo-data-science/dojo-env-setup), which you will clone in  Step 2.1, contains a backup copy of the entire set of instructions on the README, for convenience.

> Note: if you previously installed the dojo-env and are upgrading to the current version, please see the "Updating to New dojo-env" at the end of this chapter (after the Final Notes lesson)

By the end of this chapter, you will:

1. Install GitHub Desktop,
2. Install Python via Anaconda (or via miniforge - if on a Mac with an Apple Chip)
3. Create a special Python environment (dojo-env)
4. Supercharge Jupyter Notebooks with Extensions
5. Install Visual Studio Code.



### If you encounter an error during installation:

- **First, read a little further down in the instructions** to make sure we do not already address the error message that you ran into.

- **Second, please check the "Troubleshooting" chapter for a lesson** about the problem you are running into. (The Troubleshooting section is the 3rd chapter in this course - see the screenshot below)

   

  ![img](https://assets.codingdojo.com/boomyeah2015/codingdojo/curriculum/content/chapter/1658334627__Troubleshooting-chapter.png)

- **Third, reach out on the \#[ds-python-installation Discord channel](https://discord.com/channels/738494436467539968/1099094868762042400)**

   **with the following info:**

  - A) What step you are on (e.g. Step 2.3 Creating the dojo-env)
  - B) Which OS you are using (e.g. Windows 10, Windows 11, Mac with an mchip, Mac with an Intel processor, etc.)
  - C) Screenshots of the error/issue you are running into, whenever possible.
  - D) Finally, if you have been able to run the test notebook in Step 2.4: Testing the Env, please upload these files with your question.

- **Fourth, if you do not receive a response by the end of the day on Discord, please email your instructor.**

## OS-Specific Steps/Commands

For several steps (e.g. Step 1), there are multiple versions of the instructions, depending on what operating system you are using.

For step 1, please make sure you are on the correct instruction page for your OS.

### Currently Supported Operating Systems

We have prepared environment files (.yml files) for 4 different OS configurations:
- Windows (10 & 11)
- Mac (with Intel processors)*
- Mac (Apple Chips)*
- Linux**

#### **Note to Linux Users:

- Our Linux installation instructions are still in beta. While they have successfully been installed on students' Linux machines, we currently do not have a Linux machine available for troubleshooting.
  - The beta Linux instructions are located [here](https://login.codingdojo.com/m/213/13909/99742) and all steps are combined into 1 lesson.

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