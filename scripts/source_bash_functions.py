"""
  tpkit/scripts/source_bash_functions.py
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This installation script makes the bash functions implemented in 
`tpkit/commands/bash_functions.sh` and the environment variables 
defined in `config.env` available via command line
"""

import os
import sys
import pwd
import pathlib

DEFAULT_BASH_PROFILE = '.zshrc'

BASH_FUNCTIONS_FILENAME = 'bash_functions.sh'

ENVIRONMENT_VARIABLES_FILENAME = 'config.env'

def get_user_directory():
  osx_user_id = os.getuid()
  osx_user_account = pwd.getpwuid(osx_user_id)
  osx_username = osx_user_account.pw_name
  return pathlib.Path('/Users').joinpath(osx_username)

def get_bash_profile():
  user_input = input(f'Enter the name of your bash profile or press enter to use the default value ({DEFAULT_BASH_PROFILE}): ')

  return get_user_directory().joinpath(
    user_input if user_input else DEFAULT_BASH_PROFILE
  )

def get_path_to_bash_functions(path_to_tpkit: pathlib.Path):
  return (
    path_to_tpkit.joinpath('commands') \
    .joinpath(BASH_FUNCTIONS_FILENAME) \
    .resolve()
  )

def get_path_to_environment_variables(path_to_tpkit: pathlib.Path):
  return (
    path_to_tpkit.joinpath(ENVIRONMENT_VARIABLES_FILENAME)
  )

def update_bash_profile(bash_profile: str = None):
  """
  sources 'bash_functions.sh' in the OS user's bash profile, so the functions included in
  the file can be called as terminal commands. if the file is already sourced in the profile, 
  this function does nothing.
  """

  path_to_bash_profile = pathlib.Path(bash_profile) if bash_profile else ask_user_for_bash_profile()
  print(f"Setting up your bash profile to support tpkit ('{path_to_bash_profile}').")
  
  path_to_tpkit = pathlib.Path(__file__).parent.parent
  path_to_bash_functions = get_path_to_bash_functions(path_to_tpkit)
  path_to_environment_variables = get_path_to_environment_variables(path_to_tpkit)

  commands_are_sourced = False
  variables_are_sourced = False 

  # check if the bash functions are already sourced in the bash profile, and if it is,
  # return nothing to exit the function to avoid duplicate `source` commands
  with open(path_to_bash_profile) as bash_profile_file:
    bash_profile = bash_profile_file.read()
    for command in bash_profile.splitlines():
      if command.startswith('source') and command.endswith(str(path_to_bash_functions)):
        commands_are_sourced = True
      if command.startswith('source') and command.endswith(str(path_to_environment_variables)):
        variables_are_sourced = True

  if commands_are_sourced and variables_are_sourced:
    return

  # open the bash profile in append mode and add a command sourcing our bash functions
  with open(path_to_bash_profile, 'a') as bash_profile_file:
    if not variables_are_sourced:
      source_env_variables_command = f'source {path_to_environment_variables}'
      print(f"sourcing environment variables: '{source_env_variables_command}'")
      bash_profile_file.write('\n' + source_env_variables_command + '\n') 
    if not commands_are_sourced:
      source_bash_functions_command = f'source {path_to_bash_functions}'
      print(f"sourcing bash functions: '{source_bash_functions_command}'")
      bash_profile_file.write('\n' + source_bash_functions_command + '\n') 

if __name__ == '__main__':
  try:
    bash_profile_provided_via_cli_arg = sys.argv[1] if len(sys.argv) > 1 else None
    update_bash_profile(bash_profile=bash_profile_provided_via_cli_arg)
    print('Your bash profile now supports `tpkit`!')
  except Exception as exception:
    print(f'Setup for `tpkit` failed: {exception}')


# ------------ Govdash Specific Commands Below ------------

function test_govdash() 
{
  silentpush_repo
  npm test "$@"
  silent_popd
}

function ut() 
{
  test_govdash "$@"
}

function authorize_govdash()
{
  if [ -z "$1" ]; then
    user_id="$1"
  else
    user_id=$GOVDASH_DEFAULT_USER
  fi

  silentpush_repo
  echo set sessions:$user_id $user_id | redis-cli
  silent_popd
}

function reset_govdash()
{
  echo 'Re-setting your local govdash environment.'
  pushdb --force-reset
  newdb
  authorize_govdash
  capturejobs
  echo 'Successfully re-set your govdash environment'.    
}

function govdash() 
{
  if [ -z "$1" ]; then
    cd $GOVDASH_REPO_PATH
  elif [ "$1" = "ui" ]; then
    cd $GOVDASH_REPO_PATH/components
  elif [ "$1" = "pages" ]; then
    cd $GOVDASH_REPO_PATH/pages
  elif [ "$1" = "samgov" ]; then
    cd $GOVDASH_REPO_PATH/server/samgov
  elif [ "$1" = "routes" ]; then
    cd $GOVDASH_REPO_PATH/server/routers
  elif [ "$1" = "workflows" ]; then
    cd $GOVDASH_REPO_PATH/server/workflows
  elif [ "$1" = "go" ]; then
    cd $GOVDASH_REPO_PATH
    npm run dev
  elif [ "$1" = "auth" ]; then
    authorize_govdash
  elif [ "$1" = "reset" ]; then
    reset_govdash
  elif [ "$1" = "test" ]; then
    test_govdash
  else
    echo "Error: unknown govdash command $1"
    return 0
  fi
}

function gd() 
{
  govdash "$@"
}

function go() 
{
  govdash go
}

function silentpush_repo() 
{
  silent_pushd $GOVDASH_REPO_PATH
}

# temporal cli
function t() 
{
  temporal workflow start "$@"
}

function job() 
{
  if [ -z "$1"]; then 
    echo "Error: no job type provided as argument (e.g. 'job storeAttachmentsInS3')"
    return 0
  else
    t --task-queue unlimited --type "$@"
  fi
}

function datajob() 
{
  if [ -z "$1"]; then 
    echo "Error: no job type provided as argument (e.g. 'job storeAttachmentsInS3')"
    return 0
  else
    t --task-queue data_collection --type "$@"
  fi
}

function capturejobs() {
  silentpush_repo
  datajob storeNoticesFromActiveArchives
  datajob putMissingAttachmentsInS3
  silent_popd
}

# prisma cli
function p() {
  ARGS="$@";
  silentpush_repo;
  npx prisma $ARGS;
  silent_popd;
}

# prisma studio
function studio() {
  p studio;
}

function migrate() {
  silentpush_repo;
  npx prisma migrate dev;
  silent_popd;
}

function newdb() {
  silentpush_repo
  dropdb govdash
  createdb govdash
  psql govdash < $GOVDASH_DATABASE_DUMP
  silent_popd
}

function resetdb() {
  silentpush_repo
  npx prisma migrate reset
  silent_popd
}

function pushdb() {
  silentpush_repo
  npx prisma db push "$@"
  silent_popd
}

# force reset db
function fresetdb() {
  p migrate reset -f
}

# opens posgres cheat sheet
function pghelp() {
  browse https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546
}
