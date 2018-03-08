from subprocess import call
import time

call(["su"])
time.sleep(0.5)
call(["odroid"])

call(["source", "~/odroid/prefix/default/setup_env.sh"])

call(["python", "~/AntennaCharacterization/AntChar/main.py"])
