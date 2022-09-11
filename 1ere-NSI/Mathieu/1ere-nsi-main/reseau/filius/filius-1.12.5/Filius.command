#!/bin/bash
# 
# This script is meant as supportive start script for
# UNIX-like systems, e.g., Linux or Mac OS X
#
echo "Possible parameters:"
echo -e "\t-l\t\twrite log file 'filius.log'"
echo -e "\t-wd <path>\tchange base directory for working directory '.filius'"
echo

# change to directory where filius is installed
relpath=$0
cd ${relpath%`basename $0`}

# start filius
java -jar filius.jar $@

# change back to former directory
cd - > /dev/null
