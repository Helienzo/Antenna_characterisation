from subprocess import call
import time

antchar_path = "~/AntennaCharacterization/AntChar/gr-antchar/build"
call(["cd", antchar_path])
call(["cmake", "../"])
call(["make"])
call(["sudo", "make", "install"])  
call(["sudo", antchar_path, "ldconfig"])
