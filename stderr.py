##Writing error to a file:

import sys

error_file = open("error_file.txt","w")
#Assigning error stream to a file  
sys.stderr = error_file

sys.stderr.write("An error occured")
error_file.close()
