from subprocess import call
import time

#antchar_path = "~/AntennaCharacterization/gr-antchar/"
call(["cd", "gr-antchar"])
call(["mkdir", "build"])
call(["cd", "build"])
call(["cmake", "../"])
call(["make"])
call(["sudo", "make", "install"])  
call(["sudo", antchar_path, "ldconfig"])
