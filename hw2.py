import subprocess

def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(result.stdout)

    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False

falderin = '/home/user/tst'
falderout = '/home/user/out'
# print(checkout('cd /home/user/tst; 7z a /home/user/arh1', 'Everything is Ok'))

def test_step1():
    assert checkout(f'cd {falderin}; 7z a {falderout}/arh1', 'Everything is Ok'), 'test1 FAIL'

def test_step2():
    assert checkout(f'cd {falderin}; 7z u {falderout}/arh1', 'Everything is OK'), 'test2 FAIL'

def test_step3():
    assert checkout(f'cd {falderin}; 7z d {falderout}/arh1', 'Everything is Ok'), 'test3 FAIL'
    assert test_step4(), 'test4 Fail'
    assert test_step5(), 'test5 Fail'

def test_step4():
    cmd=f'cd{falderin};7z l {falderout}/arh1'
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(result.stdout)

    if 'File1.txt' in result.stdout and 'File2.txt' in result.stdout and result.returncode ==0:
        return True
    else:
        return False

def test_step5():
    cmd=f'cd{falderin};7z x {falderout}/arh1'
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(result.stdout)

    if 'Everything is OK' in result.stdout and 'File2.txt' in result.stdout and result.returncode ==0:
        return True
    else:
        return False