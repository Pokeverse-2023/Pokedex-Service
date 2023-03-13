#!/bin/bash

echo "Building packages for $function_name"

cd $path_cwd
dir_name=build_pkg/
mkdir $dir_name

# Create and activate virtual environment...
python3 -m venv env
source env/bin/activate

# Installing python dependencies...
FILE=../requirements.txt

if [ -f "$FILE" ]; then
  echo "Installing dependencies..."
  echo "From: requirement.txt file exists..."
  pip install -r "$FILE"

else
  echo "Error: requirement.txt does not exist!"
fi

# Deactivate virtual environment...
deactivate

# Create deployment package...
echo "Creating deployment package..."
cp -r env/lib/$runtime/site-packages/* $dir_name
cp -r $source_code_path $dir_name

# Removing virtual environment folder...
echo "Removing virtual environment folder..."
rm -rf env

echo "Finished script execution!"
