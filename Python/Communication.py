import socket

vna = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
vna.connect(("127.0.0.1", 5001))

def datos(vna):
    vna_msg=b""
    while not (vna_msg.endswith(b'\n')):
        vna_msg+=vna.recv(4096)
        
    return vna_msg

vna.send(str.encode("*IDN?\n"))
reply=datos(vna)
print (reply)
vna.send(str.encode("SENS:FREQ:STAR?\n"))
reply=datos(vna)
print (reply)
vna.send(str.encode("SENS:FREQ:STOP?\n"))
reply=datos(vna)
print (reply)
vna.send(str.encode("SENS:FREQuency:SPAN?\n"))
reply=datos(vna)
print (reply)
vna.send(str.encode("SENS:FREQuency:CENTer?\n"))
reply=datos(vna)
print (reply)

vna.send(str.encode("SENS:SWEEP:POINT 16001\n"))
vna.send(str.encode("SENS:SWEEP:POINT?\n"))
reply=datos(vna)    
print(reply)

vna.send(str.encode("SENS:BAND 70E1\n"))
reply=datos(vna)
print (reply)
#vna.send(str.encode("CALCulate:PARameter4:FORMat SMITh\n"))
vna.close()
print ("Comunicación terminada con exito")