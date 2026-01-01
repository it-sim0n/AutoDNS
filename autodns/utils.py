import subprocess
import sys
import time

SPINNER = "|/-\\"

def run(cmd, stdin=None):
    return subprocess.Popen(
        cmd,
        stdin=stdin,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True
    )

def spinner(proc, msg):
    i = 0
    while proc.poll() is None:
        sys.stderr.write(f"\r[{SPINNER[i % 4]}] {msg}")
        sys.stderr.flush()
        i += 1
        time.sleep(0.15)
    sys.stderr.write(f"\r[✓] {msg}\n")
