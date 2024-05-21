# Hacker Answering Machine

An answering machine for your usb Hayes modem.

# Description:

This python program will pick an incomming call, play an audio welcoming msg,
wait for the caller to press some digits and play an audio message.

Voice messages are generated using google's text-to-speech API:

- Press 1 for the weather report for today.
- Press 2 for the weather report for tomorrow.
- Press 3 for a random fact.
- Press 4 to listen to a joke.
- Press 5 to hack the planet (play a sample from the movie Hackers).

Weather forecasts (in portuguese) provided by [IPMA](https://ipma.pt)

To use option '5' you have to create the directory `./samples/hackers` and save your samples there (I didn't include the samples due to copyright issues).

Check Pradeep Singh's blog (below) to learn how to create the samples (mono, Unsigned 8-bit PCM, 8KHz wavs).

# Credits

Author: Tiago Epifânio

Based on the code written by Pradeep Singh:
- Pradeep's blog: https://iotbytes.wordpress.com/play-audio-file-on-phone-line-with-raspberry-pi/
- Pradeep's github repo: https://github.com/pradeesi/play_audio_over_phone_line

Thanks, Pradeep. Without your code this would have been much harder.
