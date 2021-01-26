import pexpect, tempfile
from sys import stdout

def cmd_password(cmd, password, timeout=60000):
    print(cmd)
    
    fname = tempfile.mktemp() 
    fout = open(fname, 'w')   

    child = pexpect.spawn(cmd, timeout=timeout, encoding='utf-8')    
    child.expect(['password: '])
    child.sendline(password)
    child.logfile = fout
    child.expect(pexpect.EOF)
    child.close()
    fout.close()

    fin = open(fname, 'r')    
    stdout = fin.read()  
    fin.close()          

    if 0 != child.exitstatus: 
        raise Exception(stdout)

    print(stdout)


def ssh(cmd, user='vmadmin', host='da2020w-0000.eastus.cloudapp.azure.com', password='Technion2020!', timeout=3000, bg_run=False):  
    fname = tempfile.mktemp() 
    fout = open(fname, 'w')   

    options = '-q -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -oPubkeyAuthentication=no'   
    if bg_run:
        options += ' -f'
    ssh_cmd = f'ssh {user}@{host} {options} "{cmd}"' 

    cmd_password(ssh_cmd, password)



def scp(path, dest, user='vmadmin', host='da2020w-0000.eastus.cloudapp.azure.com', password='Technion2020!', timeout=3000, bg_run=False):  
    fname = tempfile.mktemp() 
    fout = open(fname, 'w')   

    scp_cmd = f'scp {user}@{host}:{path} {dest}'

    cmd_password(scp_cmd, password)

