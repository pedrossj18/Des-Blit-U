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

#////// Tabview //////#
def tabview():
    tabview = s.CTkTabview(janela, width=1030, height=260, border_width=1)
    tabview.place(x=10, y=112)

# ABA CONFIGURAÇÃO #
    def aba_configuracao():
        tabview.add("Configuração")
        frame_configuracao = s.CTkFrame(tabview.tab("Configuração"))
        frame_configuracao.pack(fill="both", expand=True)

        # PRIMEIRA COLUNA
        codigo_produto_label = s.CTkLabel(frame_configuracao, text='CODIGO PRODUTO =',width=10, height=10, font=('arial bold', 12)).place(x=30, y=3)
        codigo_produto_textbox = s.CTkTextbox(frame_configuracao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=160, y=1)
        #
        endereco_serial_label = s.CTkLabel(frame_configuracao, text='ENDEREÇO SERIAL =',width=10, height=10, font=('arial bold', 12)).place(x=30, y=33)
        endereco_serial_textbox = s.CTkTextbox(frame_configuracao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=160, y=28)
        #
        boud_rate_label = s.CTkLabel(frame_configuracao, text='BAUD RATE =',width=10, height=10, font=('arial bold', 12)).place(x=30, y=63)
        boud_rate_menu = s.CTkOptionMenu(frame_configuracao, values=["9600", "19200", "38400", "57600", "115200"],height=20, fg_color="white", text_color="black",font=('arial bold', 12)).place(x= 160, y=60)
        #
        unidade_dist_label = s.CTkLabel(frame_configuracao, text='UNIDADE DIST =',width=10, height=10, font=('arial bold', 12)).place(x=30, y=93)
        unidade_dist_menu = s.CTkOptionMenu(frame_configuracao, values=["cm", "m", "mm"],height=20, fg_color="white", text_color="black",font=('arial bold', 12)).place(x= 160, y=90)
        #
        unidade_vaz_label = s.CTkLabel(frame_configuracao, text='UNIDADE VAZ =',width=10, height=10, font=('arial bold', 12)).place(x=30, y=123)
        unidade_vaz_menu = s.CTkOptionMenu(frame_configuracao, values=["L/s", "L/min", "L/h", "m³/s", "m³/min", "m³/h", "gal/s", "gal/min", "gal/h"],height=20, fg_color="white", text_color="black",font=('arial bold', 12)).place(x= 160, y=120)
        #
        resolucao_prim_label = s.CTkLabel(frame_configuracao, text='RESOLUÇÃO PRIM =',width=10, height=10, font=('arial bold', 12)).place(x=30, y=153)
        resolucao_prim_textbox = s.CTkTextbox(frame_configuracao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=160, y=149)
        #
        resoluca_sec_label = s.CTkLabel(frame_configuracao, text='RESOLUÇÃO SEC =',width=10, height=10, font=('arial bold', 12)).place(x=30, y=183)
        resoluca_sec_textbox = s.CTkTextbox(frame_configuracao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=160, y=178)
        

        # SEGUNDA COLUNA
        fator_ajuste_label = s.CTkLabel(frame_configuracao, text='FATOR DE AJUSTE =',width=10, height=10, font=('arial bold', 12)).place(x=370, y=3)
        fator_ajuste_textbox = s.CTkTextbox(frame_configuracao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=490, y=1)
        #
        distancia_maxima_label = s.CTkLabel(frame_configuracao, text='DISTÂNCIA MAXIMA =',width=10, height=10, font=('arial bold', 12)).place(x=370, y=33)
        distancia_maxima_textbox = s.CTkTextbox(frame_configuracao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=490, y=29)
        label = s.CTkLabel(frame_configuracao, text='mm',width=10, height=10, font=('arial bold', 10)).place(x=620, y=33)
        #
        distancia_minima_label = s.CTkLabel(frame_configuracao, text='DISTANCIA MINIMA =',width=10, height=10, font=('arial bold', 12)).place(x=370, y=63)
        distancia_minima_textbox = s.CTkTextbox(frame_configuracao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=490, y=60)
        label = s.CTkLabel(frame_configuracao, text='mm',width=10, height=10, font=('arial bold', 10)).place(x=620, y=63)
        #
        coluna_em_04mA_label = s.CTkLabel(frame_configuracao, text='COLUNA ME 04mA =',width=10, height=10, font=('arial bold', 12)).place(x=370, y=93)
        coluna_em_04mA_textbox = s.CTkTextbox(frame_configuracao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=490, y=90)
        label = s.CTkLabel(frame_configuracao, text='var.',width=10, height=10, font=('arial bold', 10)).place(x=620, y=93)
        #
        coluna_em_20mA_label = s.CTkLabel(frame_configuracao, text='COLUNA EM 20mA =',width=10, height=10, font=('arial bold', 12)).place(x=370, y=123)
        coluna_em_20mA_textbox = s.CTkTextbox(frame_configuracao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=490, y=120)
        label = s.CTkLabel(frame_configuracao, text='var.',width=10, height=10, font=('arial bold', 10)).place(x=620, y=123)
        #
        offset_em_04mA_label = s.CTkLabel(frame_configuracao, text='OFFSET EM 04mA =',width=10, height=10, font=('arial bold', 12)).place(x=370, y=153)
        offset_em_04mA_textbox = s.CTkTextbox(frame_configuracao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=490, y=149)
        label = s.CTkLabel(frame_configuracao, text='bits',width=10, height=10, font=('arial bold', 10)).place(x=620, y=153)
        #
        offset_em_20mA_label = s.CTkLabel(frame_configuracao, text='OFFSET EM 20mA =',width=10, height=10, font=('arial bold', 12)).place(x=370, y=183)
        offset_em_20mA_textbox = s.CTkTextbox(frame_configuracao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=490, y=178)        
        label = s.CTkLabel(frame_configuracao, text='bits =',width=10, height=10, font=('arial bold', 10)).place(x=620, y=183)


        # TERCEIRA COLUNA
        modo_resposta_label = s.CTkLabel(frame_configuracao, text='MODO RESPOSTA =',width=10, height=10, font=('arial bold', 12)).place(x=730, y=3)
        modo_resposta_menu = s.CTkOptionMenu(frame_configuracao, values=["AMORTECIDO", "RAPIDO"], height=20, fg_color="white", text_color="black",font=('arial bold', 12)).place(x= 850, y=1)
        #
        dump_label = s.CTkLabel(frame_configuracao, text='DUMP =',width=10, height=10, font=('arial bold', 12)).place(x=730, y=33)
        dump_textbox = s.CTkTextbox(frame_configuracao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=850, y=29)
        label = s.CTkLabel(frame_configuracao, text='s',width=10, height=10, font=('arial bold', 12)).place(x=980, y=33)
        #
        funcao_rele_label = s.CTkLabel(frame_configuracao, text='FUNÇAO DE RELÉ =',width=10, height=10, font=('arial bold', 12)).place(x=730, y=63)
        funcao_rele_menu = s.CTkOptionMenu(frame_configuracao, values=["LIMITE ALTO", "LIMITE BAIXO", "LIMITE ALTO/BAIXO"],height=20, fg_color="white", text_color="black",font=('arial bold', 12)).place(x= 850, y=60)
        #
        limite_baixo_label = s.CTkLabel(frame_configuracao, text='LIMITE BAIXO =',width=10, height=10, font=('arial bold', 12)).place(x=730, y=93)
        limite_baixo_textbox = s.CTkTextbox(frame_configuracao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=850, y=90)
        label = s.CTkLabel(frame_configuracao, text='var.',width=10, height=10, font=('arial bold', 12)).place(x=980, y=93)
        #
        limite_alto_label = s.CTkLabel(frame_configuracao, text='LIMITE ALTO =',width=10, height=10, font=('arial bold', 12)).place(x=730, y=123)   
        limite_alto_textbox = s.CTkTextbox(frame_configuracao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=850, y=120)
        label = s.CTkLabel(frame_configuracao, text='var.',width=10, height=10, font=('arial bold', 12)).place(x=980, y=123)
    aba_configuracao()
    # Fim #

    # ABA APLICAÇÃO #
    def aba_aplicacao():
        tabview.add("Aplicação")
        frame_aplicacao = s.CTkFrame(tabview.tab("Aplicação"))
        frame_aplicacao.pack(fill="both", expand=True)

        label = s.CTkLabel(frame_aplicacao, text='APLICAÇÃO =', width=10, height=10, font=('arial bold', 12)).place(x=30, y=3)
        tanques_options = ["TANQUE CILINDRICO FUNDO RETO", "TAQUE CILINDRICO FUNDO CÔNICO", "TANQUE RETANGULAR VERTICAL RETO", 
        "TANQUE RETANGULAR VERTICAL COM CALHA", "CALHA PARSHALL", "CERTEDOURO TRAPEZOIDAL"]
        tanques_menu_var = tk.StringVar(value=tanques_options[0])  

        menu1 = s.CTkOptionMenu(frame_aplicacao, variable=tanques_menu_var, values=tanques_options, width=250, height=20, fg_color="white", text_color="black", font=('arial bold', 12))
        menu1.place(x=140, y=0)

        imagem_label1 = s.CTkLabel(frame_aplicacao, text=" ")
        imagem_label1.pack()  # place(x=450, y=0)  # Posição da primeira caixa de imagem

        imagem_label2 = s.CTkLabel(frame_aplicacao, text=" ")
        imagem_label2.place(x=690, y=45)

        def tanques1(*args):
            tanque_selecionado = tanques_menu_var.get()
            imagem_path1, imagem_path2 = obter_caminho_da_imagem(tanque_selecionado)

            imagem1 = Image.open(imagem_path1)
            photo1 = ImageTk.PhotoImage(imagem1)
            imagem_label1.configure(image=photo1)
            imagem_label1.image = photo1

            imagem2 = Image.open(imagem_path2)
            photo2 = ImageTk.PhotoImage(imagem2)
            imagem_label2.configure(image=photo2)
            imagem_label2.image = photo2

        def obter_caminho_da_imagem(tanque):
            mapeamento_imagens = {
                "TANQUE CILINDRICO FUNDO RETO": ("C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/coreAPP00.png", "C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/CoreAPP00_DIM.png"),
                "TAQUE CILINDRICO FUNDO CÔNICO": ("C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/coreAPP01.png", "C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/CoreAPP01_DIM1.png"),
                "TANQUE RETANGULAR VERTICAL RETO": ("C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/CoreAPP02_DIM.png", "C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/CoreAPP02_DIM.png"),
                "TANQUE RETANGULAR VERTICAL COM CALHA": ("C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/CoreAPP03.png", "C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/CoreAPP03_DIM.png"),
                "CALHA PARSHALL": ("C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/CoreAPP09.png", "C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/CoreAPP09_1.png"),
                "CERTEDOURO TRAPEZOIDAL": ("C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/CoreAPP12.png", "C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/CoreAPP12_1.png"),

            }
            return mapeamento_imagens.get(tanque)

        # Adiciona a função tanques1 para ser chamada sempre que o valor do menu for alterado
        tanques_menu_var.trace_add('write', tanques1)

        # Adicione outros widgets e configurações conforme necessário
        label = s.CTkLabel(frame_aplicacao, text='PARÂMETRO [0] =',width=10, height=10, font=('arial bold', 12)).place(x=30, y=33)
        textbox1 = s.CTkTextbox(frame_aplicacao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=140, y=29)
        label = s.CTkLabel(frame_aplicacao, text='var.',width=10, height=10, font=('arial bold', 12)).place(x=270, y=33)
        #
        label = s.CTkLabel(frame_aplicacao, text='PARÂMETRO [1] =',width=10, height=10, font=('arial bold', 12)).place(x=30, y=63)
        textbox2 = s.CTkTextbox(frame_aplicacao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=140, y=60)
        label = s.CTkLabel(frame_aplicacao, text='var.',width=10, height=10, font=('arial bold', 12)).place(x=270, y=63)
        #
        label = s.CTkLabel(frame_aplicacao, text='PARÂMETRO [2] =',width=10, height=10, font=('arial bold', 12)).place(x=30, y=93)
        textbox3 = s.CTkTextbox(frame_aplicacao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=140, y=90)
        label = s.CTkLabel(frame_aplicacao, text='var.',width=10, height=10, font=('arial bold', 12)).place(x=270, y=90)
        #
        label = s.CTkLabel(frame_aplicacao, text='PARÂMETRO [3] =',width=10, height=10, font=('arial bold', 12)).place(x=30, y=123)
        textbox4 = s.CTkTextbox(frame_aplicacao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=140, y=120)
        label = s.CTkLabel(frame_aplicacao, text='var.',width=10, height=10, font=('arial bold', 12)).place(x=270, y=120)
        #
        label = s.CTkLabel(frame_aplicacao, text='PARÂMETRO [4] =',width=10, height=10, font=('arial bold', 12)).place(x=30, y=153)
        textbox5 = s.CTkTextbox(frame_aplicacao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=140, y=150)
        label = s.CTkLabel(frame_aplicacao, text='var.',width=10, height=10, font=('arial bold', 12)).place(x=270, y=150)
        #
        label = s.CTkLabel(frame_aplicacao, text='PARÂMETRO [5] =',width=10, height=10, font=('arial bold', 12)).place(x=30, y=183)     
        textbox6 = s.CTkTextbox(frame_aplicacao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=140, y=180)
        label = s.CTkLabel(frame_aplicacao, text='var.',width=10, height=10, font=('arial bold', 12)).place(x=270, y=180)
    aba_aplicacao() 
    # Fim #

    # ABA OPERAÇÃO #
    def aba_operacao():
        tabview.add("Operação")
        frame_operacao = s.CTkFrame(tabview.tab("Operação"))
        frame_operacao.pack(fill="both", expand=True)
        # Coluna 1
        label = s.CTkLabel(frame_operacao, text="COLUNA DE AR = ", width=10, height=10, font=('arial bold', 11)).place(x=30, y=5)
        textbox1 = s.CTkTextbox(frame_operacao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=160, y=1)
        label = s.CTkLabel(frame_operacao, text="var.", width=10, height=10, font=('arial bold', 11)).place(x=290, y=5)
        #
        label = s.CTkLabel(frame_operacao, text="COLUNA DE FLUIDO = ", width=10, height=10, font=('arial bold', 11)).place(x=30, y=33)
        textbox12 = s.CTkTextbox(frame_operacao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=160, y=30)
        label = s.CTkLabel(frame_operacao, text="var. ", width=10, height=10, font=('arial bold', 11)).place(x=290, y=33)
        #
        label = s.CTkLabel(frame_operacao, text="VOLUME DE FLUIDO = ", width=10, height=10, font=('arial bold', 11)).place(x=30, y=66)
        textbox1 = s.CTkTextbox(frame_operacao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=160, y=60)
        label = s.CTkLabel(frame_operacao, text="var.", width=10, height=10, font=('arial bold', 11)).place(x=290, y=66)
        #
        label = s.CTkLabel(frame_operacao, text="TOTAL PARCIAL = ", width=10, height=10, font=('arial bold', 11)).place(x=30, y=97)
        textbox1 = s.CTkTextbox(frame_operacao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=160, y=90)
        label = s.CTkLabel(frame_operacao, text="var.", width=10, height=10, font=('arial bold', 11)).place(x=290, y=97)
        #
        label = s.CTkLabel(frame_operacao, text="TOTAL ETERNO = ", width=10, height=10, font=('arial bold', 11)).place(x=30, y=125)
        textbox1 = s.CTkTextbox(frame_operacao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=160, y=120)
        label = s.CTkLabel(frame_operacao, text="var.", width=10, height=10, font=('arial bold', 11)).place(x=290, y=125)


        # Colona2
        label = s.CTkLabel(frame_operacao, text="VAZAO = ", width=10, height=10, font=('arial bold', 11)).place(x=500, y=5)
        textbox1 = s.CTkTextbox(frame_operacao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=635, y=1)
        label = s.CTkLabel(frame_operacao, text="var.", width=10, height=10, font=('arial bold', 11)).place(x=765, y=5)
        #
        label = s.CTkLabel(frame_operacao, text="VELOCIDADE DO SOM = ", width=10, height=10, font=('arial bold', 11)).place(x=500, y=33)
        textbox1 = s.CTkTextbox(frame_operacao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=635, y=30)
        label = s.CTkLabel(frame_operacao, text="m/s", width=10, height=10, font=('arial bold', 11)).place(x=765, y=33)
        #
        label = s.CTkLabel(frame_operacao, text="TEMPERATURA = ", width=10, height=10, font=('arial bold', 11)).place(x=500, y=66)
        textbox1 = s.CTkTextbox(frame_operacao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=635, y=60)
        label = s.CTkLabel(frame_operacao, text="ºC", width=10, height=10, font=('arial bold', 11)).place(x=765, y=66)
        #
        label = s.CTkLabel(frame_operacao, text="BURST DELAY = ", width=10, height=10, font=('arial bold', 11)).place(x=500, y=97)
        textbox1 = s.CTkTextbox(frame_operacao, width=125, height=9, border_width=1, corner_radius=1, fg_color="white", font=('arial bold', 9)).place(x=635, y=90)
        label = s.CTkLabel(frame_operacao, text="ms", width=10, height=10, font=('arial bold', 11)).place(x=765, y=97)
    aba_operacao()
    # Fim #

    # ABA PARAMETROS #
    def aba_parametros():
        tabview.add("Parâmetros")
        frame_parametros = s.CTkFrame(tabview.tab("Parâmetros"))
        frame_parametros.pack(fill="both", expand=True)
        
        btn_parametros = s.CTkButton(frame_parametros, height=50, text="Retorno Acústico", fg_color="grey")
        btn_parametros.place(x=850, y=160)
    aba_parametros()
    # Fim #
tabview()
# Fim #

janela.mainloop()