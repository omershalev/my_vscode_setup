import os
import sys
import platform


####### Config #######
workspace_alias = 'mujoco'
######################

if __name__ == '__main__':
    system =  platform.system()

    vscode_setup_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
    workspace_path = os.path.abspath(os.path.join(vscode_setup_path, os.pardir))        
    dot_vscode_path = os.path.join(workspace_path, '.vscode')

    source_settings_path = os.path.join(vscode_setup_path, 'workspace_specific_settings', f'{workspace_alias}_settings.json')
    source_launch_path = os.path.join(vscode_setup_path, 'workspace_specific_launch', f'{workspace_alias}_launch.json')

    target_settings_path = os.path.join(dot_vscode_path, 'settings.json')
    target_launch_path = os.path.join(dot_vscode_path, 'launch.json')

    if not os.path.exists(dot_vscode_path):
        print (f'First, create the .vscode folder {dot_vscode_path}, only then rerun the script')
        sys.exit(0)

    if system == 'Windows':
        print ('Run the below commands on elevated Command Prompt:')
        print ('=========================================')
        print (f'mklink {target_settings_path} {source_settings_path}')
        print (f'mklink {target_launch_path} {source_launch_path}')
        print ('============= End of Script =============')        

    elif system in ['Darwin', 'Linux']:
        print ('Run the below commands:')
        print (f'ln -s {source_settings_path} {target_settings_path}')
        print (f'ln -s {source_launch_path} {target_launch_path}')
        print ('============= End of Script =============')
    else:
        raise NotImplementedError()