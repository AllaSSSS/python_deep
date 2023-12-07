import subprocess

def test(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout

    if result.returncode == 0:
        return text in out

print(test('cat /etc/os-release', '22.04'))
print(test('cat /etc/os-release', 'xxx'))