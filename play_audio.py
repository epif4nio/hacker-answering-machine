# Author: Tiago Epifânio
# Based on the code written by Pradeep Singh
# Pradeep's blog: https://iotbytes.wordpress.com/play-audio-file-on-phone-line-with-raspberry-pi/
#
# Thanks, Pradeep. Without your code this would have been much harder.
#
# Description:
# This python program will pick an incomming call, play an audio welcoming msg,
# wait for the caller to press some digits and play an audio message.
#
# Voice messages are generated using a voice synthetizer.
#
# Press 1 for the weather report for today.
# Press 2 for the weather report for tomorrow.
# Press 3 for a random fact.
# Press 4 to listen to a joke.
# Press 5 to hack the planet.

import serial
import time
import threading
import atexit
import sys
import re
import wave
import text_to_speech
import random_fact
import random_joke
import weather_report
import os
import random
from datetime import datetime
from datetime import timedelta

analog_modem = serial.Serial()
analog_modem.port = "/dev/ttyACM0"
analog_modem.baudrate = 57600 #9600
analog_modem.bytesize = serial.EIGHTBITS #number of bits per bytes
analog_modem.parity = serial.PARITY_NONE #set parity check: no parity
analog_modem.stopbits = serial.STOPBITS_ONE #number of stop bits
analog_modem.timeout = 3 #non-block read
analog_modem.xonxoff = False #disable software flow control
analog_modem.rtscts = False #disable hardware (RTS/CTS) flow control
analog_modem.dsrdtr = False #disable hardware (DSR/DTR) flow control
analog_modem.writeTimeout = 3 #timeout for write

# Used in global event listener
disable_modem_event_listener = True
RINGS_BEFORE_AUTO_ANSWER = 1

#=================================================================
# Initialize Modem
#=================================================================
def init_modem_settings():
	# Opean Serial Port
	try:
		analog_modem.open()
	except:
		print("# Error: Unable to open the Serial Port.")
		sys.exit()

	# Initialize
	try:
		analog_modem.flushInput()
		analog_modem.flushOutput()

		# Test Modem connection, using basic AT command.
		if not exec_AT_cmd("AT"):
			print("# Error: Unable to access the Modem")

		# reset to factory default.
		if not exec_AT_cmd("ATZ3"):
			print("# Error: Unable reset to factory default")

		# Display result codes in verbose form
		if not exec_AT_cmd("ATV1"):
			print("# Error: Unable set response in verbose form")

		# Enable Command Echo Mode.
		if not exec_AT_cmd("ATE1"):
			print("# Error: Failed to enable Command Echo Mode")

		# Enable formatted caller report.
		if not exec_AT_cmd("AT+VCID=1"):
			print("# Error: Failed to enable formatted caller report.")

		# Enable formatted caller report.
		#if not exec_AT_cmd("AT+FCLASS=8"):
		#	print "Error: Failed to enable formatted caller report."

		analog_modem.flushInput()
		analog_modem.flushOutput()

	except:
		print("# Error: unable to Initialize the Modem")
		sys.exit()

#=================================================================
# Execute AT Commands on the Modem
#=================================================================
def exec_AT_cmd(modem_AT_cmd):
	try:
		global disable_modem_event_listener
		disable_modem_event_listener = True

		cmd = modem_AT_cmd + "\r"
		analog_modem.write(cmd.encode())

		modem_response = analog_modem.readline().decode('UTF-8')
		modem_response = modem_response + analog_modem.readline().decode('UTF-8')

		print(modem_response)

		disable_modem_event_listener = False

		if ((modem_AT_cmd == "AT+VTX") or (modem_AT_cmd == "AT+VRX")) and ("CONNECT" in modem_response):
			# modem in TAD mode
			return True
		elif "OK" in modem_response:
			# Successful command execution
			return True
		else:
			# Failed command execution
			return False

	except:
		disable_modem_event_listener = False
		print("# Error: unable to write AT command to the modem...")
		return()

#=================================================================
# Recover Serial Port
#=================================================================
def recover_from_error():
	try:
		exec_AT_cmd("ATH")
	except:
		pass

	analog_modem.close()
	init_modem_settings()

	try:
		analog_modem.close()
	except:
		pass

	try:
		init_modem_settings()
	except:
		pass

	try:
		exec_AT_cmd("ATH")
	except:
		pass

def enter_voice_mode():
	# Enter Voice Mode
	print("# Enter voice mode")
	if not exec_AT_cmd("AT+FCLASS=8"):
		print("# Error: Failed to put modem into voice mode.")
		return

	# Compression Method and Sampling Rate Specifications
	# Compression Method: 8-bit linear / Sampling Rate: 8000MHz
	print("# Set compression")
	if not exec_AT_cmd("AT+VSM=1,8000"):
		print("# Error: Failed to set compression method and sampling rate specifications.")
		return

	print("# Set bit rate")
	if not exec_AT_cmd("AT+VSD=128,0"):
		print("# Error: Failed to set VSD.")
		return

	# Put modem into TAD Mode
	print("# Enter TAD Mode")
	if not exec_AT_cmd("AT+VLS=1"):
		print("# Error: Unable put modem into TAD mode.")
		return

	# Begin transmitting audio data
	print("# Begin transmitting audio data")
	if not exec_AT_cmd("AT+VTX"):
		print("# Error: Unable to begin transmitting audio data.")
		return

	time.sleep(1)
	print("# Press '1' on your phone to hear recording.")

#=================================================================
# Play wav file
#=================================================================
def play_audio(audio_file_path):
	print("# Play Audio Msg - Start")

	# Play Audio File

	global disable_modem_event_listener
	disable_modem_event_listener = True

	wf = wave.open(audio_file_path,'rb')

	chunk = 1024

	count = 1
	data = wf.readframes(chunk)
	while len(data) > 0:
		analog_modem.write(data)
		data = wf.readframes(chunk)
		# You may need to change this sleep interval to smooth-out the audio
		#time.sleep(.12)
	wf.close()

	print("# Play Audio Msg - finished sending audio file to modem")

	#analog_modem.flushInput()
	#analog_modem.flushOutput()

	cmd = "<DLE><ETX>" + "\r"
	analog_modem.write(cmd.encode())

	# timeout = time.time() + 1
	# while 1:
	# 	modem_data = analog_modem.readline().decode('UTF-8')
	# 	if "OK" in modem_data:
	# 		print("# Received OK")
	# 		break
	# 	if time.time() > timeout:
	# 		print("# Timeout")
	# 		break

	disable_modem_event_listener = False

	#cmd = "ATH" + "\r"
	#analog_modem.write(cmd.encode())

	print("# Play Audio Msg - END")
	return

def synthetize_and_play(text, language = "en"):
	play_audio(text_to_speech.save_text_to_audio_file(text, language))

def hangup():
	# End audio data (DLE ascii (0x10 = 16) character followed by the ! character)
	cmd = chr(16)+"!" + "\r"
	analog_modem.write(cmd.encode())

	# Hang up
	print("# Exit TAD mode")
	if not exec_AT_cmd("AT+VLS=0"):
		print("# Error: Failed to exit TAD mode.")
	else:
		print("# Success: exited TAD mode")

	if not exec_AT_cmd("ATH"):
		print("# Error: Busy Tone - Failed to terminate the call")
		print("# Trying to recover the serial port")
		recover_from_error()
	else:
		print("# Busy Tone: Call Terminated")


#=================================================================
# Modem Data Listener
#=================================================================
def read_data():
	global disable_modem_event_listener
	ring_data = ""
	call_is_active = False

	while 1:
		if not disable_modem_event_listener:
			modem_data = analog_modem.readline().decode('UTF-8')
			if modem_data != "":
				if "b" in modem_data.strip(chr(16)):
					# Caller hung up
					print("# Caller hung up")
					hangup()
					call_is_active = False

				if "s" == modem_data.strip(chr(16)):
					#Terminate the call
					if not exec_AT_cmd("ATH"):
						print("Error: Silence - Failed to terminate the call")
						print("Trying to recover the serial port")
						recover_from_error()
					else:
						print("Silence: Call Terminated")

					call_is_active = False

				if call_is_active and "1" in modem_data.strip(chr(16)):
					print("# Pressed '1', let's play the weather report for today.")
					synthetize_and_play(weather_report.get(), "pt")

				if call_is_active and "2" in modem_data.strip(chr(16)):
					print("# Pressed '2', let's play the weather report for tomorrow.")
					synthetize_and_play(weather_report.get(datetime.now().date() + timedelta(days=1)), "pt")

				if call_is_active and "3" in modem_data.strip(chr(16)):
					print("# Pressed '3', let's play a random fact")
					synthetize_and_play(random_fact.get())

				if call_is_active and "4" in modem_data.strip(chr(16)):
					print("# Pressed '4', let's play a random a joke")
					synthetize_and_play(random_joke.get())

				if call_is_active and "5" in modem_data.strip(chr(16)):
					print("# Pressed '5', let's hack the planet")
					samples_dir = "./samples/hackers"
					random_sample = samples_dir + "/" + random.choice(os.listdir(samples_dir))
					print("# Playing sample: " + random_sample)
					play_audio(random_sample)

				if call_is_active and "9" in modem_data.strip(chr(16)):
					hangup()
					call_is_active = False

				if "RING" in modem_data.strip(chr(16)):
					ring_data = ring_data + modem_data
					ring_count = ring_data.count("RING")
					if ring_count <= RINGS_BEFORE_AUTO_ANSWER:
						print(modem_data)
					else:
						ring_data = ""
						call_is_active = True
						enter_voice_mode()
						welcome_message = "Dial a number."
						synthetize_and_play(welcome_message)

#=================================================================
# Close the Serial Port
#=================================================================
def close_modem_port():
	print("function close_modem_port")

	try:
		exec_AT_cmd("ATH")
	except:
		pass

	try:
		if analog_modem.isOpen():
			analog_modem.close()
			print ("Serial Port closed...")
	except:
		print("Error: Unable to close the Serial Port.")
		sys.exit()
#=================================================================


init_modem_settings()

#Start a new thread to listen to modem data
data_listener_thread = threading.Thread(target=read_data)
data_listener_thread.start()


# Close the Modem Port when the program terminates
atexit.register(close_modem_port)
