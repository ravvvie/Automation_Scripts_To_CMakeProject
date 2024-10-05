import argparse
import os
import shutil
import subprocess
from enum import Enum
from pathlib import Path

class Action(Enum):
    FULL_DEFAULT_BUILD = "full_default_build"
    MAKE_COMMIT_AND_PUSH = "make_commit_and_push"
    CLEAN = "clean"
    
DEFAULT_GIT_URL = "https://github.com/ravvvie/Automation_Scripts_To_CMakeProject.git"
DEFAULT_LOCAL_REPO_URL_NAME = "origin"
DEFAULT_BRANCH_NAME = "master"
DEFAULT_USER_NAME = "unknown"
DEFAULT_EMAIL_ADDRESS = "sapov16072002@gmail.com"

msg = input('Type the commit message (+ ENTER):') 
print("Current directory: " + os.path.realpath(__file__))
#os.chdir(os.path.dirname(os.path.realpath(__file__)))
#os.chdir(".")




def run_command(command):
    result = subprocess.run(command, shell=True)
    return result.returncode == 0

def search_for_file(inp_path, dir_to_search):
    return any(
        file.is_dir() and file.name == dir_to_search
        for file in inp_path.glob('**/*')
    )

def init_git_remote_config(URL_git, local_URL_name, user_name, email):
    git_add_remote_URL = ["git", "remote", "add", local_URL_name, URL_git]
    if (not run_command(git_add_remote_URL)):
        print("Failed git add remote URL!")
        return False
    else:
        print("Successfull git add remote URL!") 

    git_add_email = "git config --global user.email " + email
    if (not run_command(git_add_email)):
        print("Failed git add email URL!")
        return False
    else:
        print("Successfull git add email URL!") 
    
    git_add_user_name = "git config --global user.name " + user_name
    if (not run_command(git_add_user_name)):
        print("Failed git add user_name URL!")
        return False
    else:
        print("Successfull git add user_name URL!") 
    
    return True

def default_build_git(URL_git = DEFAULT_GIT_URL, local_URL_name = DEFAULT_LOCAL_REPO_URL_NAME, user_name = DEFAULT_USER_NAME, email = DEFAULT_EMAIL_ADDRESS):
    git_init_path = Path(".")
    if (not search_for_file(git_init_path, ".git")):
        init_command = ["git", "init", "."]
        if (not run_command(init_command)):
            print("Failed git init!")
            return
        else:
            print("Successfull git init!")   
    
    if (not init_git_remote_config(URL_git, local_URL_name, user_name, email)):
        print("Failed git remote config init!")
        return
    else:
        print("Successfull git remote config init!")

    git_first_add_files = ["git", "add", "."]
    if (not run_command(git_first_add_files)):
        print("Failed git add files!")
        return
    else:
        print("Successfull git add files!") 
    
    git_first_commit_files = ["git", "commit", "-m \"Init first commit in workspace\""]
    if (not run_command(git_first_commit_files)):
        print("Failed first commit creation!")
        return
    else:
        print("Successfull first commit creation!") 
    
    git_init_push_files = ["git", "push", "origin", "master"]
    if (not run_command(git_init_push_files)):
        print("Failed first push!")
        return
    else:
        print("Successfull first push!")     
     
#default_build_git()  

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Git Automation Script")
    parser.add_argument(
        "action", type=Action, choices=list(Action), help="Action to perform"
    )
    args = parser.parse_args()

    actions = {
        Action.FULL_DEFAULT_BUILD: default_build_git,
        # Action.GENERATE: generate_project_files,
        # Action.BUILD_DEBUG: lambda: build_project(Configuration.Debug),
        # Action.BUILD_RELEASE: lambda: build_project(Configuration.Release),
        # Action.CLANG_FORMAT: lambda: run_clang_format(Config.SOURCE_DIR),
    }

    selected_action = args.action

    if selected_action in actions:
        actions[selected_action]()
    else:
        print(f"Action '{selected_action}' is not implemented.")
