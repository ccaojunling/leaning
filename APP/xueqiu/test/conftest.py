import os
import signal
import subprocess

import pytest


@pytest.fixture(scope="module", autouse=True)
def record_radio():
    print("开始录制")
    command = "scrcpy --record tmp.mp4"
    p= subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    print (p)
    yield
    os.kill(p.pid,signal.CTRL_C_EVENT)
    print("录制结束")
