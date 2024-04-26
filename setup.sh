 #!/bin/sh 

repo_path=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
config_file=$repo_path/config.env
setup_step_number=0

function silently() {
  $@ > /dev/null
}

function new_setup_step() {
  setup_step_number=$((setup_step_number+1))
  echo "<> [TPKIT SETUP] | Step #$setup_step_number | $@"
}

function use_python_setup_script() {
  silently pushd $repo_path

  if [ ! -f ./$TPKIT_PYTHON_VENV_DIRECTORY ]; then
  	new_setup_step "Creating tpkit's virtual environment for $TPKIT_PYTHON ('$repo/$TPKIT_PYTHON_VENV_DIRECTORY')."
  	$TPKIT_PYTHON -m venv $TPKIT_PYTHON_VENV_DIRECTORY
  fi

  new_setup_step "Activating python virtual environment."
  . $TPKIT_PYTHON_VENV_DIRECTORY/bin/activate

  new_setup_step "Installing the tpkit python package."
  silently $TPKIT_PYTHON -m pip install $repo_path
  silently $TPKIT_PYTHON ./scripts/source_bash_functions.py $BASH_PROFILE

  new_setup_step "Deactivating tpkit's virtual environment."
  silently deactivate

  silently popd
}

if test -f $config_file; then
  echo "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
  echo "🍔 Setting up 'tpkit' 🍔"
  source $config_file
  use_python_setup_script
  echo "😀 Success! 'tpkit' is now ready to use 😀"
  echo "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
else
  echo "Error: `tpkit` config file ($config_file) does not exist. Exiting..." 
fi

