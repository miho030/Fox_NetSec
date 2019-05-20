# -*- coding: utf-8 -*-



"""
This Script is Made by Misty,(Lycan Sec; KISA KUCIS development team)
This Script for Check sysctl.conf file to check secure codes are included.

you can contact me, use gmail => anonymous0korea0@gmail.com
This Script is follow GNU GPL license Ver.3

Just run this Script, then script will Check your sysctl.conf file.
Directory location is /etc/sysctl.conf....

Start Check your system!
"""

import os
import sys


print"+==================================================+"
print"=        Network File Sec Checker(Fox_NetSec)      ="
print"=                                                  ="
print"=       한국인터넷진흥원 KUCIS                     ="
print"=                                                  ="
print"=                             Made By Misty        ="
print"=            (C) Copyright 2018 By Misty           ="
print"+==================================================+\n\n"

print"[*] ", "Start network Secure Modules.../"

# main Script

# file read machine
def File_reader():

    if os.path.isfile("/etc/sysctl.conf"):
        print"[!] ", "sysctl.conf file is detected! Start the secure modules...\n"
    else:
        print"sysctl file is not exist! check your linux system now!!"
        print"Start secure module shutdown\n\n"


    filedata = open("/home/foxwomb/projects/sysctl.conf", mode='r+t')
    Fox_lines = filedata.read()

    filedata.write("\n\n#  (C) CopyRight 2018 by Misty; KISA KUCIS SeaHawk chairman\n")
    filedata.write("#  FOX_NETSEC's original SOURCE = http://github.com/miho030/Fox_NetSec  \n")
    filedata.write("#  AND This security program is GNU GPL ver3. so you can edit this script for own your system.\n")
    filedata.write("#  This file is edit by Misty's Fox_NetSec Script. \n")
    filedata.write("#  Fox_NetSec secure and check security leel about Linux/Unix server system's sysctl.conf file. \n\n\n")

    # Check IP Spoofing Protection Codes...
    if '#IP Spoofing protection' and 'net.ip4v.conf.all.rp_filter = 1' in Fox_lines:
        print"[-]", "SECURED"
    else:
        print"\n====================================================================="
        print"[!] ", "IP Spoofing Protection is NOT SECURED..."
        print"[*] ", "Starting Secure patch"
        filedata.write("#IP Spoofing protection\n")
        filedata.write("net.ipv4.conf.all.rp_filter = 1\n")
        filedata.write("net.ipv4.conf.default.rp_filter = 1\n\n")
        print"[*] ", "IP Spoofing protection patch is secured!"
        print"====================================================================="


    # Check Ignore ICMP broadcast request Protection codes...
    if '#Ignore ICMP broadcast requests' and 'net.ipv4.icmp_echo_ignore_breadcasts = 1' in Fox_lines:
        print"[-]", "SECURED"
    else:
        print"\n====================================================================="
        print"[!] ", "Igonre ICMP breaodcast requests is NOT SECURED..."
        print"[*] ", "Starting Secure patch"
        filedata.write("#Igore ICMP broadcast requests\n")
        filedata.write("net.ipv4.icmp_echo_ignore_broadcasts = 1\n\n")
        print"[*] ", "ICMP bradcating protection patch is secured!"
        print"====================================================================="


    # Check Disable source packet routing protection codes...
    if '#Disable source packet routing' and 'net.ipv4.conf.all.accept_score_route = 0' in Fox_lines:
        print"[-]", "SECURED"
    else:
        print"\n====================================================================="
        print"[!] ", "Disable source packet routing is NOT SECURED..."
        print"[*] ", "Starting Secure patch"
        filedata.write("#Disable source packet routing\n")
        filedata.write("net.ipv4.conf.all.accept_score_route = 0\n")
        filedata.write("net.ipv6.conf.all.accept_score_route = 0\n")
        filedata.write("net.ipv4.conf.default.accept_source_route = 0\n")
        filedata.write("net.ipv6.conf.default.accept_source_route = 0\n\n")
        print"[*] ", "source packet routing protection patch is secured!"
        print"====================================================================="


    # check Ignore send redirects protection coeds...
    if '#Ignore send redirects'and 'net.ipv4.conf.all.send_redirects' in Fox_lines:
        print"[-]", "SECURED"
    else:
        print"\n====================================================================="
        print"[!] ", "Ignore send redirects is NOT SECURED..."
        print"[*] ", "Starting Secure patch"
        filedata.write("#Ignore send redirects\n")
        filedata.write("net.ipv4.conf.all.send_redirects = 0\n")
        filedata.write("net.ipv6.conf.default.send_redirects = 0\n\n")
        print"[*] ", "send redirects potection patch is secured!"
        print"====================================================================="


    # Block SYN redirects protection code..../
    if '#Block SYN attacks' and 'net.ipv4.tcp.syncookies = 1' in Fox_lines:
        print"[-]", "SECURED"
    else:
        print"\n\n====================================================================="
        print"[!] ", "Block SYN attacks is NOT SECURED..."
        print"[*] ", "Starting Secure patch"
        filedata.write("#Block SYN attacks\n")
        filedata.write("net.ipv4.tcp.syncookies = 1\n")
        filedata.write("net.ipv4.tcp_max_syn_backlog = 2048\n")
        filedata.write("net.ipv4.tcp_synack_retries = 2\n")
        filedata.write("net.ipv4.tcp_syn_retries = 5\n\n")
        print"[*] ", "IP SYN attack protection patch is secured!"
        print"====================================================================="


    #Log Martians protection codes...
    if '#Log Martians' and 'net.ipv4.conf.all.log_martians = 1' in Fox_lines:
        print("[-]", "SECURED")
    else:
        print"\n====================================================================="
        print"[!] ", "Log Martians is NOT SECURED..."
        filedata.write("#Log Martians\n")
        filedata.write("net.ipv4.conf.all.log__martians = 1\n")
        filedata.write("net.ipv4.icmp_ignore_bogus_error_response = 1\n\n")
        print"[*] ", "Martians protection patch is secured!"
        print"====================================================================="


    # Ignore ICMP redirects protection codes...
    if '#Ignore ICMP redirects' and 'net.ipv4.conf.all.accept_redirects = 0' in Fox_lines:
        print"[-]", "SECURED"
    else:
        print"\n====================================================================="
        print"[!] ", "Ignore ICMP redirects is NOT SECURED..."
        print"[*] ", "Starting Secure patch"
        filedata.write("#Ignore ICMP redirects\n")
        filedata.write("net.ipv4.conf.all.accept_redirects = 0\n")
        filedata.write("net.ipv6.conf.all.accept_redirects = 0\n")
        filedata.write("net.ipv4.conf.all.default.accept_redirects = 0\n")
        filedata.write("net.ipv6.conf.default.accept_redirects = 0\n\n")
        print"[*] ", "ICMP redirects protection patch is secured!"
        print"====================================================================="


    #direct ping deny codes...
    if '#Ignore Directed pings' and 'net.ipv4.icmp_echo_ignore_all = 1' in Fox_lines:
        print"[-]", "SECURED" 
    else:
        print"\n\n====================================================================="
        print"[!] ", "Ignore Directed pings is NOT SECURED"
        print"[*] ", "Starting Secure patch"
        filedata.write("#Ignore Directed pings\n")
        filedata.write("net.ipv4.icmp_exho_ignore_all = 1\n\n")
        print"[*] ", "Directed pings protection patch is secured!"
        print"====================================================================="




# Update of New kenel parameter patch...--> 2018/12/27 th patch

    # Enables source route verification
    if '# Enables source route verification' and 'net.ipv4.conf.all.rp_filter = 1' in Fox_lines:
        print "[-]", "SECURED"
    else:
        print"\n\n====================================================================="
        print"[!] ", "Enables source route verification is NOT SECURED"
        print"[*] ", "Starting Secure patch"
        filedata.write("# Enables source route verification\n")
        filedata.write("net.ipv4.conf.all.rp_filter = 1\n\n")
        print"[*] ", "# Enables source route verification patch is secured!"
        print"====================================================================="

    if '# Disables automatic defragmentation (needed for masquerading, LVS)' and 'net.ipv4.ip_always_defrag = 0'in Fox_lines:
        print "[-]", "SECURED"
    else:
        print"\n\n====================================================================="
        print"[!] ", "Disables automatic defragmentation is NOT SECURED"
        print"[*] ", "Starting Secure patch"
        filedata.write("# Disables automatic defragmentation (needed for masquerading, LVS)\n")
        filedata.write("net.ipv4.ip_always_defrag = 0\n\n")
        print"[*] ", "Disables automatic defragmentation (needed for masquerading, LVS) patch is secured!"
        print"====================================================================="


    # 리눅스 시스템에서 수용할 수 있는 최대 접속 SYN 패킷의 갯수는 backlog queue와 관련이 깊음.
    # 그 말은 즉슨, backlog queue 값을 늘리면 그 만큼 수용할 수 있는 SYN패킷의 갯수도 늘어남.
    # 그런고로 해당 설정을 해야하는데, 일반적으로는 RAM이 128Mb인 경우, 1024로  설정하고, 아닐경우, 128로 설정한다.
    # 해당 값은 include/net/tcp.h애서 수정할 수 있다.
    if '# Disables the magic-sysrq key' and 'kernel.sysrq = 0' and 'net.ipv4.tcp_syncookies = 1' in Fox_lines:
        print "[-]", "SECURED"
    else:
        print"\n\n====================================================================="
        print"[!] ", "Disables the magic-sysrq key is NOT SECURED"
        print"[*] ", "Starting Secure patch"
        filedata.write("# Disables the magic-sysrq key\n")
        filedata.write("kernel.sysrq = 0\n\n")
        filedata.write("net.ipv4.tcp_syncookies = 1\n\n")
        print"[*] ", "Disables the magic-sysrq key patch is secured!"
        print"====================================================================="


    if '# Disable ICMP Redirect Acceptance' and 'net.ipv4.conf.all.accept_redirects = 0' in Fox_lines:
        print "[-]", "SECURED"
    else:
        print"\n\n====================================================================="
        print"[!] ", "Disable ICMP Redirect Acceptance is NOT SECURED"
        print"[*] ", "Starting Secure patch"
        filedata.write("# Disable ICMP Redirect Acceptance\n")
        filedata.write("net.ipv4.conf.all.accept_redirects = 0\n\n")
        print"[*] ", "Disable ICMP Redirect Acceptance patch is secured!"
        print"====================================================================="


    if '# Enable bad error message Protection' and 'net.ipv4.icmp_ignore_bogus_error_responses = 1' in Fox_lines:
        print "[-]", "SECURED"
    else:
        print"\n\n====================================================================="
        print"[!] ", "Enable bad error message Protection is NOT SECURED"
        print"[*] ", "Starting Secure patch"
        filedata.write("# Enable bad error message Protection\n")
        filedata.write("net.ipv4.icmp_ignore_bogus_error_responses = 1\n\n")
        print"[*] ", "Enable bad error message Protection patch is secured!"
        print"====================================================================="


    if '# Enable IP spoofing protection' and 'net.ipv4.conf.all.rp_filter = 1' in Fox_lines:
        print "[-]", "SECURED"
    else:
        print"\n\n====================================================================="
        print"[!] ", "Enable IP spoofing protection Protection is NOT SECURED"
        print"[*] ", "Starting Secure patch"
        filedata.write("# Enable IP spoofing protection\n")
        filedata.write("net.ipv4.conf.all.rp_filter = 1\n\n")
        print"[*] ", "Enable IP spoofing protection patch is secured!"
        print"====================================================================="


    # 시스템이 ip주소를 스푸핑한다고 예상하는 경우에 로그에 기록함.
    if '# Log Spoofed Packets, source Routed Packets, Redirect packets' and 'net.ipv4.conf.all.rp_filter = 1' in Fox_lines:
        print "[-]", "SECURED"
    else:
        print"\n\n====================================================================="
        print"[!] ", "Log Spoofed Packets, source Routed Packets, Redirect packets is NOT SECURED"
        print"[*] ", "Starting Secure patch"
        filedata.write("# Log Spoofed Packets, source Routed Packets, Redirect packets\n")
        filedata.write("net.ipv4.conf.all.log_martians = 1\n\n")
        print"[*] ", "Log Spoofed Packets, source Routed Packets, Redirect packets patch is secured!"
        print"====================================================================="



    """
    Server maintance/performance improve prameters...
    """

    # 서버 가상 메모리 사용시, disk access 시간을 줄여서 성능을 높인다.
    if '# Improve file system performance' and 'vm.bdflush = 100 1200 128 512 15 5000 500 1884 2' in Fox_lines:
        print "[-]", "SECURED"
    else:
        print"\n\n====================================================================="
        print"[!] ", "Improve file system performance is NOT SECURED"
        print"[*] ", "Starting Secure patch"
        filedata.write("# Improve file system performance\n")
        filedata.write("vm.bdflush = 100 1200 128 512 15 5000 500 1884 2\n\n")
        print"[*] ", "Improve file system performance patch is secured!"
        print"====================================================================="


    # 가상 메모리 사용시, 전체 메모리에서 버퍼 메모리 사용량 조절.
    if '# Improve virtual memory performance' and 'vm.buffermem = 80 10 60' in Fox_lines:
        print "[-]", "SECURED"
    else:
        print"\n\n====================================================================="
        print"[!] ", "Improve virtual memory performance is NOT SECURED"
        print"[*] ", "Starting Secure patch"
        filedata.write("# Improve virtual memory performance\n")
        filedata.write("vm.buffermem = 80 10 60\n\n")
        print"[*] ", "Improve virtual memory performance patch is secured!"
        print"====================================================================="

    # TCP, UDP 로컬 포트 지정. 일반적으로 TCP 32768, UDP 61000인듯.. 일단 그렇게 설정함.
    if '# Allowed local port range' and 'net.ipv4.ip_local_port_range = 32768 61000' in Fox_lines:
        print "[-]", "SECURED"
    else:
        print"\n\n====================================================================="
        print"[!] ", "Allowed local port range is NOT SECURED"
        print"[*] ", "Starting Secure patch"
        filedata.write("# Allowed local port range\n")
        filedata.write("net.ipv4.ip_local_port_range = 32768 61000\n\n")
        print"[*] ", "Allowed local port range patch is secured!"
        print"====================================================================="

    """
    MAX-OPEN FILE COUNT 설정 --> 굳이 하지 않아도 됨.
    서버 performance를 위해서 필요할 수도...
    
    4M일 때 256개가 일반적. 512M일 때, 32768, inode값은 32768*4=131072
    요즘 서버 램이 기본적으로 32기가 이상이니, 최솟값 32기가로 계산해보면,
    32G -> 20480000, inode값은 20480000*4=81920000
    
    즉, 파라미터 값은 아래와 같아짐...
    fs.file - max = 20480000
    fs.inode - max = 81920000
    
    극혐...
    
    if '# Improve the number of open files' and 'fs.file - max = 8192' and 'fs.inode - max = 32768' in Fox_lines:
        print "[-]", "SECURED"
    else:
        print"\n\n====================================================================="
        print"[!] ", "Improve the number of open files is NOT SECURED"
        print"[*] ", "Starting Secure patch"
        filedata.write("# Improve the number of open files\n")
        
        # 하나의 프로세서에서 열 수 있는 파일 갯수 조정은 fs.h 컺널 소스 변경해야함.
        filedata.write("# (fs.h INR_OPEN / limits.h NR_OPEN)\n")
        filedata.write("fs.file - max = 20480000\n\n")
        filedata.write("fs.inode - max = 81920000\n\n")
        print"[*] ", "Improve the number of open files patch is secured!"
        print"====================================================================="
    """

    print"all of Network secure code are having. now is safe!!"
    print" Thanks for using my security program!^^"
    filedata.close()

File_reader()
