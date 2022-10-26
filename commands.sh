# tpkit/commands.sh

PREFERRED_TEXT_EDITOR_FOR_CODING="sublime text" # application name

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