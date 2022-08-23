import subprocess

def run_Test():
    print("============ R U N N I N G   T E S T S ================")
    cmd = "python3 -m pytest -v"
    subprocess.call(cmd, shell=True)

def check_types()-> None:
    print("=========== R U N N I N G   T Y P E  C H E C K ============")
    cmd = "mypy --ignore-missing-imports tests"
    subprocess.call(cmd, shell=True)

def run_TestAll():
    run_Test()
    check_types()

