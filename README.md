
				
## PLATFORM: 
- DistAlgo version -- 1.0.9 
- Python Implementation CPython 3.6.3
- Operating System: macOS Sierra 10.12.6 (16G29)
- PyNacl: 1.1.2
   
		   
## INSTRUCTIONS:
- Install Python3
- Install Distalgo: "sudo pip3 install pyDistAlgo"
- Install PyNacl: "sudo pip3 install pynacl"


## MAIN FILES.  
			       
- BCR.da : This file contains code for master to read configuration file from command line and initiate Olympus and Clients.
- client.da :This file contains code for clients to send client requests and receive client responses, configuration request & response to Olympus
- olympus.da : This file contains code for olympus to initiate replicas and handle re-configuration requests from clients
- replica.da : This file contains code for replicas to handle client requests and other replica messages.
- testconfigs : This folder contains test config files of various failure scenarios.


## SINGLE PROCESS SETUP
- running for particular test scenario and generating a log file called "testcasename.txt"
   - python3 -m da --logfile --logfilename testcasename.txt --logfilelevel 'info' --message-buffer-size size_bytes BCR.da test1.txt
