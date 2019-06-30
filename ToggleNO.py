# $language = "python"
# $interface = "1.0"

# NoToggle.py
#
# Description: This will grab a line that does NOT have a 'no' infront, and paste it with a 'No' perfix.
# conversly, if you have a 'no' infront of the line, the script will copy and paste without the 'no'

# Port of NoToggle.vbs

objTab = crt.GetScriptTab()

strLines = objTab.Screen.Selection

if not strLines.strip():
	crt.Dialog.MessageBox("No Text Selected!")


for line in strLines.splitlines():
	if line.startswith("no "):
		objTab.Screen.Send (line[3:]+'\r')
	else:	
		objTab.Screen.Send ("no "+line+ '\r')