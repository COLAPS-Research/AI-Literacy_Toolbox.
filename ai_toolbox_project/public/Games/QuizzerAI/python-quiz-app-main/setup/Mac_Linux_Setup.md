# Setup (only needed **ONCE**)

## Checklist if you're ready

## Clone The Repository

As you already have an empty project opened in your IDE and selected git bash as your terminal emulator you're now ready to go for getting the code on
your computer.

1. Fork this repository by putting the command into your `terminal` opened in your IDE.
> Note: [How to fork a repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
2. **How to determine where the repository should be stored?**
 - use the `cd` command to move up to the directory in your file system where the repo should be cloned.
 - the `mkdir` command creates a new folder. We use this to create a dedicated place where the repository should go.
 - Example:

```bash
 # Start at the root directory (in your terminal of choice)
   cd Documents                    # Move into your Documents folder
   mkdir python-quiz-app           # create new folder
   cd python-quiz-app              # move into new folder

   # Now clone your forked repository into this new folder
   git clone <gitlab-repo-to-clone-or-fork>
 ```

> INFO: You can copy-paste this commands *one-by-one* or follow the order of commands, but set a custom path.

## Open the cloned project in your IDE

You can close the systems terminal ow and open the cloned repository with pycharm. From now on we will always refer to the integrated terminal in your IDE.

### For PYCHARM users

It will ask you if you would like to create a **virtual-environment** by default.
This is usually initialized as .venv and you'll directly see it in your project structure if you follow the steps.

**Run**:
```bash
# Step1: Check if the .venv or venv is listed either in the project folder (`command` + `1`) or by running:
ls -lah
# Step 2: activate the virtual environment if not yet (.venv/venv is the name of your virtual-environment)
source <name_of_venv>/bin/activate
# Step 3: Check the python version
python --version
# Step 4: if python version is less than 3.13, else _be happy_
rm -rf <name_of_venv>
```

### For VSCODE users

Just continue to the [next section (running the setup script)](#run-the-setup-script).

## Run The Setup-Script

SO, as the project is now cloned and a virtual environment exists we can now proceed in the `terminal` of your **IDE**.

Before we can start the implementation we quickly need to install all the necessary software. With `software` we mean
the required **python-packages** for running the application.

**Run:**
```bash
cd src
python3.13 setup.py
```

## Congratulations

Run the following to return to project root in your terminal.
```bash
cd ..
```
If the install run without errors you're ready to go and start working on the project! 🎉

## Troubleshooting

### Make shell scripts executable
If during running the setup.py command an error occurs run the following:

```bash
chmod +x scripts/setup_mac_linux.sh
```

And re-run the setup command:
```bash
python3.11 setup.py
```
