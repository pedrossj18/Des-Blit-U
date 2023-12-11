from pymodbus.client import ModbusSerialClient as ModbusClient

# Configurar o cliente Modbus para Windows com adaptador RS485 para USB
client = ModbusClient(method='rtu', port='COM1', baudrate=9600, stopbits=1, bytesize=8, parity='N')
client.connect()

# Ler um registrador (por exemplo, registrador 0x0001)
result = client.read_holding_registers(1, 1, unit=1)
value = result.registers[0]

# Fechar a conexão
client.close()