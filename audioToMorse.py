from morse_audio_decoder.morse import MorseCode
hexToMorse = {'0': "-----", '1': ".----", '2': "..---", '3': "...--", '4': "....-", '5': ".....", '6': "-....", '7': "--...", '8': "---..", '9': "----.", 'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".", 'F': "..-."}
morseDic = {"-----": '0', ".----": '1', "..---": '2', "...--": '3', "....-": '4', ".....": '5', "-....": '6', "--...": '7', "---..": '8', "----.": '9', ".-": 'A', "-...": 'B', "-.-.": 'C', "-..": 'D', ".": 'E', "..-.": 'F'}

fileName = input("File: ")
morse_code = MorseCode.from_wavfile(fileName)
out = morse_code.decode()
outStr = ''.join(list(map(lambda x: hexToMorse[x] + " ", out)))
print(outStr)