import tkinter as tk
from pymodbus.client import ModbusTcpClient
from threading import Thread
import time

def ler_dados():
    client = ModbusTcpClient("localhost", 502)
    
    try:
        response = client.read_holding_registers(0, 5, unit=0)
        
        if response.isError():
            dados_recebidos_label.config(text="Erro ao ler dados")
        else:
            dados = response.registers
            dados_recebidos_label.config(text=f"Recebido: {dados}")
    except Exception as e:
        dados_recebidos_label.config(text=f"Erro: {str(e)}")
    finally:
        client.close()

def escrever_dados():
    client = ModbusTcpClient("localhost", 502)

    try:
        # Valores que você deseja escrever no registrador
        novos_valores = [11, 22, 33, 44, 55]
        
        # Escrever os novos valores no registrador
        response = client.write_registers(0, novos_valores, unit=0)

        if response.isError():
            dados_recebidos_label.config(text="Erro ao escrever dados")
        else:
            dados_recebidos_label.config(text=f"Valores escritos com sucesso: {novos_valores}")
    except Exception as e:
        dados_recebidos_label.config(text=f"Erro: {str(e)}")
    finally:
        client.close()

def modbus_serv_TCP():
    from pymodbus.server import StartTcpServer, ModbusTcpContext, ModbusTcpServer
    from pymodbus.datastore import ModbusSequentialDataBlock
    from twisted.internet.task import LoopingCall

    store = ModbusSequentialDataBlock(0, [1, 2, 3, 4, 5])
    context = ModbusTcpContext(slaves=1, single=True)
    context[0] = store

    def update_data():
        store.setValues(0, 0, [value + 1 for value in store.getValues(0, 0, 5)])

    server = ModbusTcpServer(context, address=("localhost", 502))
    looping_call = LoopingCall(update_data)
    looping_call.start(1)
    
    # Iniciar o servidor Modbus em uma thread
    server_thread = Thread(target=lambda: StartTcpServer(server, context=context))
    server_thread.daemon = True
    server_thread.start()

# Configuração da janela principal
root = tk.Tk()
root.title("Cliente Modbus")

ler_button = tk.Button(root, text="Ler Dados", command=ler_dados)
escrever_button = tk.Button(root, text="Escrever Dados", command=escrever_dados)
dados_recebidos_label = tk.Label(root, text="Recebido:")

ler_button.pack()
escrever_button.pack()
dados_recebidos_label.pack()

# Iniciar o servidor Modbus TCP em uma thread
modbus_thread = Thread(target=modbus_serv_TCP)
modbus_thread.daemon = True
modbus_thread.start()

# Loop principal da interface gráfica
root.mainloop()