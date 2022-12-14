 #!/bin/sh 

MY_NAME="Tyler"

PREFERRED_TEXT_EDITOR_FOR_CODING="sublime text" # application name

PATH_TO_WEB_BROWSER_APPLICATION="/Applications/Google Chrome.app"

WORK_DIRECTORY="~/garage"

function clear_scrollback()
{
  printf '\33c\e[3J'; # https://stackoverflow.com/questions/2198377/how-can-i-clear-previous-output-in-terminal-in-mac-os-x
}

function clear_all() 
{
  clear;
  clear_scrollback;
}

function lets_code() 
{
  open -a $PREFERRED_TEXT_EDITOR_FOR_CODING $1;
}

function chrome()
{
  /usr/bin/open -a $PATH_TO_WEB_BROWSER_APPLICATION $1;
}

function google() 
{
  KEY_WORDS="$@";
  QUERY=${KEY_WORDS// /"+"};
  SEARCH_RESULTS_URL=http://google.com/search?q=$QUERY;
  chrome $SEARCH_RESULTS_URL;
}

function print_weather()
{
  python3 -m tpkit.weather;
}

function print_random_quote()
{
  python3 -m tpkit.quotes;
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