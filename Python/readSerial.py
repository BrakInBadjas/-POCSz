import serial
import sys
import time
import util

serial_port = '/dev/cu.usbmodem1421'
key = "KCQWKCQWKCQWKCQWKCQWKCQWKCQWKCQWKCQWKCQWKCQWKCQWKCQWKCQWKCQWKCQWKCQWKCQWKCQWKCQW"

ser = serial.Serial(
    port=serial_port,
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
        timeout=10000)

print("connected to: " + ser.portstr)

#this will store the line
seq = []

def handleInput(input):
    print(input);
    seq_input = input.rstrip().split(',')
    handled_input = {}
    for input in seq_input:
        split_input = input.split(':')
        handled_input[split_input[0]] = split_input[1]

    if(handled_input.get('server') == None):
        handleDoor(handled_input)

def handleDoor(input):
    writeSerial('server:received\n')
    if input.get('status') != None:
        if util.addDoorIfNotExists(input):
            writeSerial('server:connected')
        else:
            writeSerial('server:error')
    elif input.get('door') != None and input.get('key') != None:
        UID = input.get('key')
        print("encrypted: " +ord_String(UID));
        UID = encryptDecrypt(UID)
        print("decrypted: " +ord_String(UID));
        auth_status = util.hasPermission(UID, input['door'])
        writeSerial('server:connected,key:'+input['key']+'!,auth:'+str(auth_status))

def encryptDecrypt(input):
    output = xor_strings(input, key)
    return output

def xor_strings(s,t):
    """xor two strings together"""
    return "".join(chr(ord(a)^ord(b)) for a,b in zip(s,t))

def ord_String(string):
    output = ""
    for char in string :
        output = output + " " + str(ord(char))
    return output
    
def writeSerial(data):
    if type(data) == str:
        ser.write(data.encode('utf-8'))

while True:
    for c in ser.read():
        seq.append(chr(c))
        print(str(c))
        if chr(c) == '\n':
            seq.pop()
        joined_seq = ''.join(str(v) for v in seq) #Make a string from array
        if chr(c) == '\n': # Read full line
            handleInput(joined_seq)
            seq = []
            break

ser.close()