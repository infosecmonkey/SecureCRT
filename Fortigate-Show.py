# $language = "python"
# $interface = "1.0"

# show running configuration on Fortigate in a readable manner

def Main():
	crt.Screen.Synchronous = True
	crt.Screen.Send("config" + chr(9) + "system console" + chr(13))
	crt.Screen.WaitForString(" (console) # ")
	crt.Screen.Send("set output standard" + chr(13))
	crt.Screen.WaitForString(" (console) # ")
	crt.Screen.Send("n" + chr(8) + "end" + chr(13))
	crt.Screen.WaitForString(" # ")
	crt.Screen.Send("show full" + chr(9) + chr(13))

Main()
