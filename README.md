# Cybersecurity

# Pentesting project using Metaspolt 
Objective: The objective of this project is to show my skills in Pentesting and exploit a Windows that has not been updated. 

# Network Diagram 






# Locating the Target

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/4c9ab3e0-35c5-48ae-9cab-9f14531fd0fb)

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/75f8b503-4194-4b35-aed4-4356ccc6600f)

From the scan, I could conclude with some certainty that the 10.20.0.2 is the victim’s ip address because we can see that there are a lot of services running in the pc. And, We can see that 10.20.0.1 is mostly likely a pc or not a server. And, 10.20.0.2 is a much more valuable target. 


# Reconnaissance 

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/c10d8382-0332-48b4-9932-48ba26fcdf8c)

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/4e384ac7-3bcc-4592-a853-fffe4851f214)

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/98809bf6-9d82-4151-b5e2-1a6be5b7a046)

From our Metasploit scans we were able to find many key information such as we were able to brute force the administrator account password, we were able to find the smb version that they are running and we were able to list the smb shares in the machine. 

Now we will try for ftp and ssh protocol

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/df59ab7d-6ac9-422a-80ec-83d0b91d390b)

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/64b8ca23-be53-4eae-92c2-110b6b910493)

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/aba5b6e4-27ec-4a5c-a523-a2fd3bd91cf6)

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/e16d63c0-0261-4598-acdd-d1ada50cef7c)

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/b52e363f-d21c-435f-b2f7-be46de4c1090)

From the new scans in the above screenshots, we were able to brute force the ssh login credentials and the ftp credentials. We were able to extract which ssh verision the user is using


# Exploiting the Server

From our reasearch we could use an exploit called enternal blue ms17_010 which this server is vunlunberable to. 

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/71ee90ae-ffa2-4f5d-b434-2628d5015c3f)

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/e4142751-a2a0-4270-9704-0291fadd967c)

![image](https://github.com/SgtClutch/Cybersecurity/assets/59116892/0e9f4f79-8913-4f21-82f6-4961786eb019)

We used the exploit ms17_010_enternalblue which we learned the computer is vulunberable to due to our nmap scans. We would have used the exploit enternal blue to create a bufferoverflow which created a blue screen and then used our payload option windows/x64/meterpreter/reverse_tcp to extract more information from the pc such as getting any hashes that are in the pc using the hashdump command













