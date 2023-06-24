# my_vscode_setup

Create soft links:
1. Full path to launch.json in Git clone --> path to launch.json in .vscode folder, e.g.:  
**Mac:** `ln -s ~/push_objects_ws/my_vscode_setup/launch.json .vscode/launch.json`  
**Windows:** `mklink .vscode\launch.json D:\CodingArea\push_objects_ws\my_vscode_setup\launch.json`

2. Full path to workspace settings.json in Git clone --> path to settings.json in .vscode folder, e.g.:  
**Mac:** `ln -s ~/CodingArea/avo_workspace/my_vscode_setup/workspace_specific_settings/avo_settings.json .vscode/settings.json`  
**Windows:** `mklink .vscode\settings.json D:\CodingArea\push_objects_ws\my_vscode_setup\settings.json`

3. Full path to user settings file in Git clone --> path to settings.json in user area, e.g.:  
**Mac:** `ln -s ~/CodingArea/avo_workspace/my_vscode_setup/user_settings.json /Users/omershal/Library/Application\ Support/Code/User/settings.json`
