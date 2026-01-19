import pyvisa


ADDRESS = 'TCPIP0::127.0.0.1::5001::SOCKET'



try:
    print(f"Intentando conectar a {ADDRESS}...")
    rm = pyvisa.ResourceManager()
    vna = rm.open_resource(ADDRESS)
    
    
    vna.timeout = 5000  
    vna.read_termination = '\n'
    vna.write_termination = '\n'

    
    identificacion = vna.query('*IDN?')
    print("-" * 40)
    print(f"✅ ¡CONEXIÓN EXITOSA!\nEquipo: {identificacion}")
    print("-" * 40)

    vna.close()

except Exception as e:
    print(f"Error de conexión: {e}")
   