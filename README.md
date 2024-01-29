# Pentesting project using Metaspolt 
Objective: The objective of this project is to show my skills in Pentesting and exploit a Windows that has not been updated. 

# Network Diagram

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/8f5ad7fe-34a6-4990-bb30-a9701a49a5df)







# Locating the Target

We are doing a nmap -sS because this scan can be performed quickly and it never compeletes the TCP handshake. The scan sends a SYN packet to the target machine and awaits for a SYN/ACK packet
indicating the port is open or RST packet indicating the port is closed. 

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/4c9ab3e0-35c5-48ae-9cab-9f14531fd0fb)

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/aab3c9f4-bed5-402b-9cd1-639a2229a3ef)


![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/75f8b503-4194-4b35-aed4-4356ccc6600f)

From the scan, I could conclude with some certainty that the 10.20.0.2 is the victim’s ip address because we can see that there are a lot of services running in the pc. And, We can see that 10.20.0.1 is mostly likely a pc or not a server.


# Reconnaissance 

During this step, we are going to do more scans and gather more information about the machine. And, we are going to target ftp,smb and ssh protocol. Our goal is gather more info that we can use to exploit the machine.

In metasplot we will be using the auxliary module, this module does not excute any payload and is not directly related to exploitation. They are used for other tasks such as port scanning, DoS attacks etc. During the reconnaissance phase we will be using its scanning feature to scan the smb, ssh and ftp services. 
 
![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/98809bf6-9d82-4151-b5e2-1a6be5b7a046)

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/6e99c0f7-f373-4755-912a-74f5bb9ffe8b)


![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/e79804f5-eed8-42d5-8e50-a18ecbd04182)

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/1a9ccf0a-001c-4cab-83b0-39b17c4e5f45)

From our Metasploit scans we were able to find many key information such as we were able to brute force the administrator account password, we were able to find the smb version that they are running and we were able to list the smb shares in the machine. 

Now we will try for ftp and ssh protocol

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/df59ab7d-6ac9-422a-80ec-83d0b91d390b)

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/64b8ca23-be53-4eae-92c2-110b6b910493)

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/aba5b6e4-27ec-4a5c-a523-a2fd3bd91cf6)

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/e16d63c0-0261-4598-acdd-d1ada50cef7c)

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/b52e363f-d21c-435f-b2f7-be46de4c1090)

From the new scans in the above screenshots, we were able to brute force the ssh login credentials and the ftp credentials. And, We were able to extract which ssh verision the user is using


# Exploiting the Server

From our reasearch we could use an exploit called enternal blue ms17_010 which is a vunlunberability which is described by CVE-2017-0144 that the smb service has, on this server. ( (https://www.sentinelone.com/blog/eternalblue-nsa-developed-exploit-just-wont-die/) https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0144) 

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/71ee90ae-ffa2-4f5d-b434-2628d5015c3f)

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/e4142751-a2a0-4270-9704-0291fadd967c)

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/0e9f4f79-8913-4f21-82f6-4961786eb019)

We were unable to create a session with the windows server, but we were able to create a DoS attack for 5 mins before the server restarted. 

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/54014cf5-23c3-418d-ae1d-e30a8a8cad24)


We used the exploit ms17_010_enternalblue which we learned the computer is vulnerable to due to our nmap scans. We would have used the exploit enternal blue to create a bufferoverflow which created a blue screen and our next step would be to use a  payload option windows/x64/meterpreter/reverse_tcp to extract more information from the pc such as getting any hashes that are in the pc using the hashdump command


# Resources 

https://nmap.org/book/man-port-scanning-techniques.html

https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0144

https://www.sentinelone.com/blog/eternalblue-nsa-developed-exploit-just-wont-die/

https://darknetdiaries.com/transcript/54/















