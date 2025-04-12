#!/usr/bin/env python3

import paramiko as pm

credentials = [('level1', 'level1')]

def main():

    try:
        client = pm.SSHClient()
        client.set_missing_host_key_policy(pm.AutoAddPolicy())
        client.load_system_host_keys()
        username, password = credentials[0]
        client.connect(hostname='io.netgarage.org', username=username, password=password)
        _, stdout, stderr = client.exec_command('cd /levels')

        for each in [ stdout, stderr ]:
            output = each.read().decode('utf-8').strip()
            print(f"{output=}")

        _, stdout, stderr = client.exec_command('ls -lah')

        print(stdout.read().decode('utf-8'))

    except Exception as e:
        print(f"Something went wrong: {e}")

    finally:
        client.close()

if __name__ == "__main__":
    main()

