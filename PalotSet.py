# $language = "python"
# $interface = "1.0"

# This is the command that changes the 'show' commands to set as opposed to XML
# It also turns off the pager to not have to hit space bar. 

def Main():
	crt.Screen.Synchronous = True
	crt.Screen.Send("set cli pager off" + chr(13))
	crt.Screen.Send("set cli config-output set" + chr(13))
	crt.Screen.Send("configure" + chr(13))
	crt.Screen.Send("show" + chr(13))
	crt.Screen.Send("exit" + chr(13))
	crt.Screen.Send("set cli pager on" + chr(13))
Main()
