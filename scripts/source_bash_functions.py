"""
  tpkit/scripts/source_bash_functions.py
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This installation script makes the bash functions implemented in 
`tpkit/commands/bash_functions.sh` available via command line
"""

import os
import pwd
import pathlib

BASH_PROFILE_FILENAME = '.zshrc'

BASH_FUNCTIONS_FILENAME = 'bash_functions.sh'

def update_bash_profile():
  """
  sources 'bash_functions.sh' in the OS user's bash profile, so the functions included in
  the file can be called as terminal commands. if the file is already sourced in the profile, 
  this function does nothing.
  """

  osx_user_id = os.getuid()
  osx_user_account = pwd.getpwuid(osx_user_id)
  osx_username = osx_user_account.pw_name
  path_to_bash_profile = os.path.join('/Users', osx_username, BASH_PROFILE_FILENAME)

  path_to_tpkit_directory = pathlib.Path(__file__).parent.parent
  path_to_bash_functions = path_to_tpkit_directory.joinpath('commands') \
                                                  .joinpath(BASH_FUNCTIONS_FILENAME) \
                                                  .resolve()

  # check if the bash functions are already sourced in the bash profile, and if it is,
  # return nothing to exit the function to avoid duplicate `source` commands
  with open(path_to_bash_profile) as bash_profile_file:
    bash_profile = bash_profile_file.read()
    for command in bash_profile.splitlines():
      if command.startswith('source') and command.endswith(str(path_to_bash_functions)):
        return

  # open the bash profile in append mode and add a command sourcing our bash functions
  with open(path_to_bash_profile, 'a') as bash_profile_file:
    source_command = f'source {path_to_bash_functions}'
    bash_profile_file.write('\n' + source_command + '\n') 

if __name__ == '__main__':
  update_bash_profile()
