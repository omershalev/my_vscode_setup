# my_vscode_setup

Create soft links:
1. path to launch.json in Git repo --> path to launch.json in .vscode folder:  
**Linux:** `ln -s my_vscode_setup/launch.json .vscode/launch.json`  
**Windows:** `mklink .vscode\launch.json my_vscode_setup\launch.json`

1. path to settings.json in Git repo --> path to settings.json in .vscode folder:  
**Linux:** `ln -s my_vscode_setup/settings.json .vscode/settings.json`  
**Windows:** `mklink .vscode\settings.json my_vscode_setup\settings.json`
