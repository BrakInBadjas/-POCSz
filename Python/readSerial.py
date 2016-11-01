import serial
import time
import util

ser = serial.Serial(
    port='/dev/cu.usbmodem1421',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
        timeout=0)

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

    print(handled_input)
    if(handled_input.get('server') == None):
        handleDoor(handled_input)
    elif(handled_input.get('auth') != None):
        print(input)

def handleDoor(input):
    writeSerial('server:received')
    if input.get('status') != None:
        writeSerial('\n')
        if util.addDoorIfNotExists(input):
            writeSerial('server:connected')
        else:
            writeSerial('server:error')
    elif input.get('door') != None and input.get('key') != None:
        writeSerial('\n')
        auth_status = util.hasPermission(input['key'], input['door'])
        writeSerial('server:connected,key:'+input['key']+',auth:'+str(auth_status))
    
def writeSerial(data):
    if type(data) == str:
        print(data)
        ser.write(data.encode('utf8'))

while True:
    for c in ser.read():
        seq.append(chr(c)) #convert from ANSII
        joined_seq = ''.join(str(v) for v in seq) #Make a string from array

        if chr(c) == '\n': # Read full line
            handleInput(joined_seq)
            seq = []
            break

ser.close()