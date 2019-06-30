# $language = "python"
# $interface = "1.0"

# change pager to 0 so you do not need to hit space bar and then runs the 'more system:running-config' command.
# once collected, it will change the pager back to 24

def Main():
	crt.Screen.Synchronous = True
	crt.Screen.Send("terminal pager 0" + chr(13))
	crt.Screen.WaitForString("#")
	crt.Screen.Send("more system:running-config" + chr(13))
	crt.Screen.WaitForString("#")
	crt.Screen.Send(chr(13))
	crt.Screen.WaitForString("#")
	crt.Screen.Send(chr(13))
	crt.Screen.WaitForString("#")
	crt.Screen.Send("termin pager 24" + chr(13))

Main()
