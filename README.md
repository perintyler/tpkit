# tpkit

## Installation

From within the tpkit repo root directory, install the package and its dependecies with `pip`.

```bash
pip3 install .
```

Then, run the `source_bash_functions.py` script, which will source `commands/bash_functions.sh` in the current OS user bash profile. This script currently only works for OSX, but could be easily modified in the future to support more operating systems.

```bash
python3 ./scripts/source_bash_functions.py
```

## System Commands

### Googling

The `google` command allows for quick googling while coding. It will open up a web browser with the google search results for the specified search terms. The default web browser is google chrome, but this can be changed by updating the value of `PATH_TO_WEB_BROWSER_APPLICATION` in `commands/bash_functions.sh`. 

```bash
google how do I install python3
```
