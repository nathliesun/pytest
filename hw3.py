import subprocess

def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(result.stdout)

    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False
    
import time

class StatFixture:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.stat_file_path = "stat.txt"

    def after_step(self):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        files_count, file_size = self._get_file_stats()
        cpu_load_stats = self._get_cpu_load_stats()
        with open(self.stat_file_path, "a") as file:
            file.write(f"{timestamp}, {files_count}, {file_size}, {cpu_load_stats}\n")
        # print(checkout('cd /home/user/tst; 7z a /home/user/arh1', 'Everything is Ok'))


stat_fixture = StatFixture("config.txt")
falderin = '/home/user/tst'
falderout = '/home/user/out'

def test_step1():
    assert checkout(f'cd {falderin}; 7z a {falderout}/arh1', 'Everything is Ok'), 'test1 FAIL'
    stat_fixture.after_step()

def test_step2():
    assert checkout(f'cd {falderin}; 7z u {falderout}/arh1', 'Everything is OK'), 'test2 FAIL'
    stat_fixture.after_step()

def test_step3():
    assert checkout(f'cd {falderin}; 7z d {falderout}/arh1', 'Everything is Ok'), 'test3 FAIL'
    assert test_step4(), 'test4 Fail'
    assert test_step5(), 'test5 Fail'
    stat_fixture.after_step()

def test_step4():
    cmd=f'cd{falderin};7z l {falderout}/arh1'
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    stat_fixture.after_step()
    print(result.stdout)

    if 'File1.txt' in result.stdout and 'File2.txt' in result.stdout and result.returncode ==0:
        return True
    else:
        return False

def test_step5():
    cmd=f'cd{falderin};7z x {falderout}/arh1'
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    stat_fixture.after_step()
    print(result.stdout)

    if 'Everything is OK' in result.stdout and 'File2.txt' in result.stdout and result.returncode ==0:
        return True
    else:
        return False