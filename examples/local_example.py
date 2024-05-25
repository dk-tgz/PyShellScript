import pyshellscript


def main():
    stdout, stderr, return_code = pyshellscript.local_command_executor.run_shell_command("date")
    print("stdout: {}, stderr: {}, return_code: {}\n".format(stdout, stderr, return_code))
    stdout, stderr, return_code = pyshellscript.local_command_executor.run_shell_command("ls")
    print("stdout: {}, stderr: {}, return_code: {}\n".format(stdout, stderr, return_code))
    stdout, stderr, return_code = pyshellscript.local_command_executor.run_shell_command("pwd")
    print("stdout: {}, stderr: {}, return_code: {}\n".format(stdout, stderr, return_code))
    stdout, stderr, return_code = pyshellscript.local_command_executor.run_shell_command("seq -w 1 100", streaming=True)
    print("stdout: {}, stderr: {}, return_code: {}\n".format(stdout, stderr, return_code))
    stdout, stderr, return_code = pyshellscript.local_command_executor.run_shell_command("not_found")
    print("stdout: {}, stderr: {}, return_code: {}\n".format(stdout, stderr, return_code))


if __name__ == '__main__':
    main()
