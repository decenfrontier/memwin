import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

from memwin.xprocess import XProcess


def test_create_process():
    #  -Xss2m -Xms128m -Xmx256m -Dfile.encoding=GB2312 -verbose:gc -cp . 
    app_path = r"D:\倚天剑与屠龙刀\bin\seasky.exe"
    lpCommandLine = r"  -Xss2m -Xms128m -Xmx256m -Dfile.encoding=GB2312 -verbose:gc -cp . senv.xload.XLoad applib htp seasky.zar:hero.zar hero.fore.Start seaskyWin=true startAt=hero1.zar fps=true dcAddress=82.157.27.48 volumesAddress=http://ytsl.linekong.cn/line/YTVolumes123S20"
    cwd = r"D:\倚天剑与屠龙刀"
    pid = XProcess.create_process(lpCommandLine, cwd, app_path)
    print(f"pid: {pid}")
    assert pid != 0
    
def test_get_hwnd_by_pid():
    pid = 26276
    hwnd = XProcess.get_hwnd_by_pid(pid)
    assert hwnd == 727028