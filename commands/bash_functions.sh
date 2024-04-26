 #!/bin/sh 

BASH_FUNCTIONS_FILEPATH="$TPKIT_PATH"/commands/bash_functions.sh # path to this file

function clear_scrollback()
{
  printf '\33c\e[3J'; # https://stackoverflow.com/questions/2198377/how-can-i-clear-previous-output-in-terminal-in-mac-os-x
}

function clearall() 
{
  clear;
  clear_scrollback;
}

function lets_code() 
{
  open -a $PREFERRED_TEXT_EDITOR_FOR_CODING $1;
}

function browse()
{
  /usr/bin/open -a $PATH_TO_WEB_BROWSER_APPLICATION $1;
}

function google() 
{
  KEY_WORDS="$@";
  QUERY=${KEY_WORDS// /"+"};
  SEARCH_RESULTS_URL=http://google.com/search?q=$QUERY;
  browse $SEARCH_RESULTS_URL;
}

function tpkit_python()
{
  silently . $TPKIT_PATH/$TPKIT_PYTHON_VENV_DIRECTORY/bin/activate
  $TPKIT_PYTHON "$@"
  silently deactivate
}

function weather()
{
  tpkit_python -m tpkit.weather
}

function quote()
{
  tpkit_python -m tpkit.quotes
}

function start_work() 
{
  cd $WORK_DIRECTORY;
  clear_all;
  echo Hello, $MY_NAME.
  echo;
  echo;
  print_weather; 
  echo;
  echo;
  print_random_quote;
  echo;
  echo;
  echo "Good Luck :)";
  echo;
  echo;
}

function silently() {
  $@ > /dev/null
}

function tpkit() 
{
  if [ -z "$1" ]; then
    cd $TPKIT_PATH
  elif [ "$1" = "help" ]; then
    cat $BASH_FUNCTIONS_FILEPATH
  elif [ "$1" = "new" ]; then
    lets_code $BASH_FUNCTIONS_FILEPATH
  else
    echo "Error: unknown tpkit command $1"
  fi
}

function setupkit() 
{
  bash $TPKIT_PATH/setup.sh
  source $BASH_PROFILE
}

function makecommand() 
{
  subl $BASH_FUNCTIONS_FILEPATH
}

function putTextInClipboard() 
{
  echo $@ | pbcopy
}

function clip() 
{
  putTextInClipboard "$@"
}

function clear_pip()
{
  python3 -m pip freeze | xargs python3 -m pip uninstall -y;
}

function pyactivate() 
{
  . $TPKIT_PYTHON_VENV_DIRECTORY/bin/activate
}

function silent_pyactivate() 
{
  silently pyactivate
}

function silent_pydeactivate() 
{
  deactivate > /dev/null
}

function vpython()
{
  silent_pyactivate
  $TPKIT_PYTHON "$@"
  silent_pydeactivate
}

function pykit() {
  silent_pushd $TPKIT_PATH
  vpython "$@"
  silent_popd
}

function newbashscript()
{
  touch $1
  sudo chmod 755 "$1"
}

# interactive git rebase
function irebase()
{
  if [ -z "$1" ]; then
    echo "the 'irebase' command requires an positional argument indicating how many commits to rebase"
  else
    git rebase -i HEAD~$1
  fi
}

function stderr() { 
  printf "%s\n" "$*" >&2
}

function findpath()
{
  args="$@";
  find . -type f -name $args;
}

# stdouts 1 if file exists, 0 if not
function file_exists() 
{
  if [ -z "$1" ]; then
    stderr "Error: provide file path (e.g. 'file_exists ./myfile.ext'"
  elif test -f $env_file; then
    echo 1
  else
    echo 0
  fi
}

function silent_pushd() {
  pushd "$@" > /dev/null
}

function spushd() 
{ 
  silent_pushd "$@" 
}

function silent_popd() {
  popd "$@" > /dev/null
}


function spopd() 
{ 
  silent_popd "$@" 
}

function home() {
  cd ~
}

