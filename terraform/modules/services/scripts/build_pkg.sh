#!/bin/bash

echo "Building packages for $function_name"

cd $path_cwd
dir_name=lambda_dist_pkg/
mkdir $dir_name

# Create and activate virtual environment...
virtualenv -p $runtime env_$function_name
source env_$function_name/bin/activate

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
cp env_$function_name/lib/$runtime/site-packages/* $dir_name
cp -r $source_code_path/ $dir_name

# Removing virtual environment folder...
echo "Removing virtual environment folder..."
rm -rf env_$function_name

echo "Finished script execution!"
