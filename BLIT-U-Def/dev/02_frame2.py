from customtkinter import TkinterApp, TkinterWindow, TkinterLabel, TkinterEntry, TkinterButton
import minimalmodbus
import serial.tools.list_ports
import customtkinter as s
import tkinter as tk
import webbrowser
from PIL import Image, ImageTk
import serial.tools.list_ports
import minimalmodbus

janela = s.CTk()  #Criação de janela1
janela.title("Configurador BLIT-U")  # Configuração do titulo
janela.iconbitmap("C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/BLIT-U_LOGO.ico") # Imagem do icone da janela 
janela.geometry("1050x500") # Tamanho da janela 
janela.configure(fg_color="lightgrey") # Cor de da janela 
janela.maxsize(width=1050, height=550) 
janela.resizable(width=False, height=False) # Deixar janela em tamanho fixo 
font= s.CTkFont(family='arial bold', size=8)

class ModbusGUI:
    def __init__(self, master):
        self.master = master
        master.title("Modbus GUI")

        # Criar os widgets
        self.label_device_info = TkinterLabel(master, text="Informações do Dispositivo:")
        self.label_device_info.grid(row=0, column=0, columnspan=2, pady=10)

        self.label_parameter1 = TkinterLabel(master, text="Parâmetro 1:")
        self.label_parameter1.grid(row=1, column=0)
        self.entry_parameter1 = TkinterEntry(master)
        self.entry_parameter1.grid(row=1, column=1)

        self.label_parameter2 = TkinterLabel(master, text="Parâmetro 2:")
        self.label_parameter2.grid(row=2, column=0)
        self.entry_parameter2 = TkinterEntry(master)
        self.entry_parameter2.grid(row=2, column=1)

        self.connect_button = TkinterButton(master, text="Conectar", command=self.connect_device)
        self.connect_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Configurações para comunicação Modbus RTU
        self.instrument = None  # Inicializar como None até que a porta seja selecionada

    def connect_device(self):
        try:
            # Verificar automaticamente as portas seriais disponíveis
            available_ports = [port.device for port in serial.tools.list_ports.comports()]

            if not available_ports:
                print("Nenhuma porta serial disponível.")
                return

            print("Portas seriais disponíveis:")
            for i, port in enumerate(available_ports):
                print(f"{i + 1}. {port}")

            # Solicitar ao usuário que selecione a porta serial
            selected_port_index = int(input("Selecione o número da porta serial: ")) - 1
            selected_port = available_ports[selected_port_index]

            print(f"Conectando à porta {selected_port}...")

            # Configurar a comunicação Modbus RTU sobre RS485
            self.instrument = minimalmodbus.Instrument(selected_port, 1)  # Substitua pelo endereço do dispositivo

            # Leitura dos registradores do Modbus (exemplo: registradores 0 e 1)
            values = [self.instrument.read_register(0), self.instrument.read_register(1)]

            # Atualizar as caixas de texto com as informações lidas
            self.entry_parameter1.delete(0, 'end')
            self.entry_parameter1.insert(0, str(values[0]))
            self.entry_parameter2.delete(0, 'end')
            self.entry_parameter2.insert(0, str(values[1]))

            print("Conectado ao dispositivo Modbus com sucesso.")
        except Exception as e:
            print(f"Erro ao conectar ao dispositivo Modbus: {e}")

janela.mainloop()
