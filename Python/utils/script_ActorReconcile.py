import unreal
import os
import sys
import ueUtils as util

# Access argument vector from UE BP.
hism = str(sys.argv[1])
print("HISM: " + hism)

util.logSelectedActors()

# Delineator for visual clarity
unreal.log_warning("-------------------------")