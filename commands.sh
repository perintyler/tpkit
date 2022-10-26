# tpkit/commands.sh

function clear_scrollback()
{
    printf '\33c\e[3J'; # https://stackoverflow.com/questions/2198377/how-can-i-clear-previous-output-in-terminal-in-mac-os-x
}

function clearall() 
{
  clear;
  clear_scrollback;
}