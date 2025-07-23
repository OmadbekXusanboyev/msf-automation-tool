# #!/bin/bash

# exploit=$1
# msfconsole -q -x "use $1; show options; exit" >> ./see_option_result.txt


#!/bin/bash

msfconsole -q -r all_options.rc >> see_option_result.txt

