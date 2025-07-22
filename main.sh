#!/bin/bash

for file in ./*.txt;
do
    > "$file"
done
echo "" > ex.rc
eho "" > all_options.rc


bash search.sh
python3 see_options.py
python3 run_see_options.py
bash see_options.sh
python3 seperate_options.py
python3 run_exploit.py
bash exploit.sh
