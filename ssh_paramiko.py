import paramiko
client = paramiko.SSHClient()
client.load_system_host_keys()
client.load_host_keys('/home/sudeep/.ssh/known_hosts')
client.connect(hostname='127.0.0.1',username='sudeep',port=9999)
