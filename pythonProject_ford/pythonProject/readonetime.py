import time,subprocess,signal

def readonetime():
    command = "ssh ECG fdpcat > test.fdp"

    process = subprocess.Popen(command, shell=True)
    time.sleep(2)
    process.send_signal(signal.CTRL_C_EVENT)