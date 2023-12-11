import tkinter as tk
import customtkinter as s
from tkinter import ttk
from pymodbus.client import ModbusTcpClient
import serial
import serial.tools.list_ports

# Função para listar portas seriais disponíveis
def listar_portas():
    return [port.device for port in serial.tools.list_ports.comports()]

# Função para conectar à porta serial selecionada
def conectar_serial():
    global ser
    porta = porta_combobox.get()
    baud_rate = int(baud_rate_entry.get())
    try:
        ser = serial.Serial(porta, baud_rate)
        status_serial_label.config(text=f"Conectado a {porta}")
    except serial.SerialException:
        status_serial_label.config(text="Erro ao conectar à porta serial")

# Função para enviar dados pela porta serial
def enviar_dados():
    if ser:
        dados = dados_entry.get()
        ser.write(dados.encode())

# Função para ler dados da porta serial
def ler_dados():
    if ser:
        dados = ser.read(ser.in_waiting).decode()
        dados_recebidos_label.config(text=f"Recebido: {dados}")

# Função para conectar ao dispositivo Modbus
def conectar_modbus():
    ip_dispositivo = ip_entry.get()
    porta_modbus = int(porta_modbus_entry.get())
    try:
        client = ModbusTcpClient(ip_dispositivo, porta_modbus)
        client.connect()
        status_modbus_label.config(text=f"Conectado a {ip_dispositivo}:{porta_modbus} (Modbus TCP)")
        return client
    except Exception as e:
        status_modbus_label.config(text=f"Erro ao conectar ao Modbus TCP: {str(e)}")
        return None

# Função para ler um registro no dispositivo Modbus
def ler_registro():
    client = conectar_modbus()
    if client:
        endereco = int(endereco_modbus_entry.get())
        quantidade = int(quantidade_modbus_entry.get())
        resultado = client.read_holding_registers(endereco, quantidade)
        valor_lido_modbus_label.config(text=f"Valor lido: {resultado.registers}")
        client.close()

# Função para escrever um valor em um registro no dispositivo Modbus
def escrever_registro():
    client = conectar_modbus()
    if client:
        endereco = int(endereco_modbus_entry.get())
        valor = int(valor_modbus_entry.get())
        client.write_register(endereco, valor)
        status_modbus_label.config(text=f"Valor {valor} escrito no registrador {endereco}")
        client.close()

# Configuração da janela principal
root = tk.Tk()
root.title("Comunicação Serial e Modbus")

# Cria um notebook para abas
notebook = ttk.Notebook(root)

# Cria a aba de Comunicação Serial
aba_serial = ttk.Frame(notebook)
notebook.add(aba_serial, text="Comunicação Serial")

porta_label = tk.Label(aba_serial, text="Porta Serial:")
porta_combobox = ttk.Combobox(aba_serial, values=listar_portas())
baud_rate_label = tk.Label(aba_serial, text="Baud Rate:")
baud_rate_entry = tk.Entry(aba_serial)
connect_button = tk.Button(aba_serial, text="Conectar", command=conectar_serial)
status_serial_label = tk.Label(aba_serial, text="Desconectado")
dados_label = tk.Label(aba_serial, text="Enviar Dados:")
dados_entry = tk.Entry(aba_serial)
enviar_button = tk.Button(aba_serial, text="Enviar", command=enviar_dados)
ler_button = tk.Button(aba_serial, text="Ler Dados", command=ler_dados)
dados_recebidos_label = tk.Label(aba_serial, text="Recebido:")

porta_label.pack()
porta_combobox.pack()
baud_rate_label.pack()
baud_rate_entry.pack()
connect_button.pack()
status_serial_label.pack()
dados_label.pack()
dados_entry.pack()
enviar_button.pack()
ler_button.pack()
dados_recebidos_label.pack()

# Cria a aba de Comunicação Modbus
aba_modbus = ttk.Frame(notebook)
notebook.add(aba_modbus, text="Comunicação Modbus")

ip_label = tk.Label(aba_modbus, text="IP do Dispositivo:")
ip_entry = tk.Entry(aba_modbus)
porta_modbus_label = tk.Label(aba_modbus, text="Porta Modbus:")
porta_modbus_entry = tk.Entry(aba_modbus)
status_modbus_label = tk.Label(aba_modbus, text="")
endereco_modbus_label = tk.Label(aba_modbus, text="Endereço do Registro:")
endereco_modbus_entry = tk.Entry(aba_modbus)
quantidade_modbus_label = tk.Label(aba_modbus, text="Quantidade de Registros:")
quantidade_modbus_entry = tk.Entry(aba_modbus)
ler_modbus_button = tk.Button(aba_modbus, text="Ler Registro", command=ler_registro)
valor_modbus_label = tk.Label(aba_modbus, text="Novo Valor:")
valor_modbus_entry = tk.Entry(aba_modbus)
escrever_modbus_button = tk.Button(aba_modbus, text="Escrever Registro", command=escrever_registro)
valor_lido_modbus_label = tk.Label(aba_modbus, text="")

ip_label.pack()
ip_entry.pack()
porta_modbus_label.pack()
porta_modbus_entry.pack()
status_modbus_label.pack()
endereco_modbus_label.pack()
endereco_modbus_entry.pack()
quantidade_modbus_label.pack()
quantidade_modbus_entry.pack()
ler_modbus_button.pack()
valor_modbus_label.pack()
valor_modbus_entry.pack()
escrever_modbus_button.pack()
valor_lido_modbus_label.pack()

notebook.pack()

# Variável global para a porta serial
ser = None

# Loop principal da interface gráfica
root.mainloop()