from subprocess import call
import time

call(["su"])
time.sleep(0.5)

call(["source ", "~/prefix/default/setup_env.sh"])

call(["python ", "~/AntennaCharacterization/AntChar/main.py"])
