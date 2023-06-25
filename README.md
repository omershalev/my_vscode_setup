# my_vscode_setup

1. Clone this repo locally (prefarably in the VS code workspace folder)

2. Soft links - **workspace**:

* Full path to launch.json in Git clone --> path to launch.json in .vscode folder, e.g.:  
**Mac/Linux:** `ln -s ~/push_objects_ws/my_vscode_setup/launch.json .vscode/launch.json`  
**Windows:** `mklink .vscode\launch.json D:\CodingArea\push_objects_ws\my_vscode_setup\launch.json`

* Full path to workspace settings.json in Git clone --> path to settings.json in .vscode folder, e.g.:  
**Mac/Linux:** `ln -s ~/CodingArea/avo_workspace/my_vscode_setup/workspace_specific_settings/avo_settings.json .vscode/settings.json`  
**Windows:** `mklink .vscode\settings.json D:\CodingArea\push_objects_ws\my_vscode_setup\workspace_specific_settings\push_objects_settings.json`

3. Soft links - **user**:
* Full path to user settings file in Git clone --> path to settings.json in user area, e.g.:  
**Mac/Linux:** `ln -s ~/CodingArea/avo_workspace/my_vscode_setup/user_settings.json /Users/omershal/Library/Application\ Support/Code/User/settings.json`  
**Windows:** `mklink C:\Users\omers\AppData\Roaming\Code\User\settings.json \\wsl$\Ubuntu\home\omer\push_objects_ws\my_vscode_setup\user_settings.json` (requires Command Prompt in elavated mode)
  
* Full path to keybindings.json file in Git clone --> path to keybindings.json in user area, e.g.:  
**Windows:** `mklink C:\Users\omers\AppData\Roaming\Code\User\keybindings.json \\wsl$\Ubuntu\home\omer\push_objects_ws\my_vscode_setup\keybindings\keybindings.json` (requires Command Prompt in elavated mode)

## Notes:
1. On Windows, run `mklink` commands from "Command Prompt" (in "PowerShell", the tool is not installed by default).
2. When working on WSL, address to the "Windows" section for **user** links and "Mac/Linux" section for **workspace** links (run the commands in WSL prompt).
