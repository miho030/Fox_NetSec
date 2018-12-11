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
print"+==================================================+\n\n\n"

print"[*] ", "Start network Secure Modules.../"

# main Script

# file read machine
def File_reader():

    if os.path.isfile("/homefoxwomb/projects/sysctl.conf"):
        print"[!] ", "sysctl.conf file is detected! Start the secure modules...\n\n"
    else:
        print"sysctl file is not exist! check your linux system now!!"
        print"Start secure module shutdown"


    filedata = open("/home/foxwomb/projects/sysctl.conf", mode='r+t')
    Fox_lines = filedata.read()

    filedata.write("\n\n#  (C) CopyRight 2018 by Misty; KISA KUCIS SeaHawk chairman\n")
    filedata.write("#  FOX_NETSEC's original SOURCE = http://github.com/mihho030/Fox_NetSec  \n")
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


    print"all of Network secure code are having. now is safe!!"
    print" Thanks for using my security program!^^"
    filedata.close()

File_reader()
