# tpkit

`tpkit` is a python package for defining fun or useful commands that can be called from a terminal prompt, such as a `google` command. It also includes utility functions that I've found myself frequently needing, which are useful for scripting.

## Installation

From within the tpkit repo root directory, install the package and its dependecies with `pip`.

```bash
pip3 install .
```

Then, run the `source_bash_functions.py` script, which will source `commands/bash_functions.sh` in the current OS user bash profile. This script currently only works for OSX, but could be easily modified in the future to support more operating systems.

```bash
python3 ./scripts/source_bash_functions.py
```

Or, use the convenience script, which installs the package and sources the bash functions for you. (Make sure python3 is installed before running this script).

```bash
bash setup.sh
```

__NOTE:__ as of now, this script will only work for OSX users.
__TODO:__ improve the script so it works for all operating systems.

## System Commands

### Googling

The `google` command allows for quick googling while coding. It will open up a web browser with the google search results for the specified search terms. The default web browser is google chrome, but this can be changed by updating the value of `PATH_TO_WEB_BROWSER_APPLICATION` in `commands/bash_functions.sh`. 

```bash
google how do I install python3
```

### Texting

```bash
text 2024561111 "hey, this is a text message send from my command line"
```

To make this easier to use, add functions to `commands/bash_functions.sh` to text individual people. Something like this:

```bash
function text_cornelius()
{
  message = "@";
  text 2129631234 $message;
}

```

### Start Work

The `start_work` command will navigate to the current project directory (define in `bash_commands.sh` -- TODO: create a config file), clear the terminal window and its scrollback, print the weather of the current location (which is determined using IP address information), then prints out a random quote. It looks something look this:

```bash
Hello, Tyler.


It is currently 63.7 degrees with a windspeed of 10.0. Expect partly cloudy skies and overcast.


It is better to understand a little than to misunderstand a lot.
  - Anatole France


Good Luck :)


tylerperin@Tylers-MBP tpkit % 
```

## Testing

`tpkit` uses the `pytest` unit-testing framework. All tests can be found in `tests.py`, which is located in the root directory of this repository. To run the unit tests:

```bash
pytest tests.py
```
