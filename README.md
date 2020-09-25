# handler

.sh and .py files I use to handle between workstations.<br>
Windows <---> Ubuntu <br>
Used in conjunction w/ MobaXTerm for file transfer and remote control.

### descriptions
#### BASH
puller.sh: Bash File to automate Git pull while Standardizing Paths for Linux Machines <br>
pusher.sh: Bash File to automate Git commit & push while returning paths to Windows Formatting

#### PYTHON
pathSwap.py: .py File linked with puller.sh: Iterates through repository to find Windows-Specific paths and convert. <br>
pathSwapBack.py: .py File linked with pusher.sh: Iterates through repository to return adjusted paths to Windows Formatting

printToken.py: .py File to access and print GitHub authorization token to speed up git processing while retaining privacy
