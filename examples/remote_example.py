import pyshellscript


def main():
    ssh = pyshellscript.SSHClient(host="localhost", port=2222, user="ubuntu", key_path="./ssh/id_rsa", password=None,
                                  sudo_password=False)
    ssh.connect(2, 15)
    stdout, stderr, return_code = ssh.execute("ls /home/ubuntu/.ssh/authorized_keys")
    print("stdout: {}, stderr: {}, return_code: {}\n".format(stdout, stderr, return_code))
    stdout, stderr, return_code = ssh.execute("cat /etc/*release*", streaming=True)
    print("stdout: {}, stderr: {}, return_code: {}\n".format(stdout, stderr, return_code))
    stdout, stderr, return_code = ssh.execute_script("./script_to_execute_on_remote_host.sh", streaming=True)
    print("stdout: {}, stderr: {}, return_code: {}\n".format(stdout, stderr, return_code))
    ssh.close()


if __name__ == '__main__':
    main()
