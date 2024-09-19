#!/bin/bash
# Check if the PYFILE environment variable is set
if [ -z "$PYFILE" ]; then
echo "Error: PYFILE environment variable is not set."
exit 1
fi

# Check if the specified file exists and is executable
if [ ! -f "$PYFILE" ]; then
echo "Error: The file specified in PYFILE does not exist."
exit 1
fi

# Run the Python script
python3 "$PYFILE"
