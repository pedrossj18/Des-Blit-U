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

def tabview():
    tabview = s.CTkTabview(janela, width=1030, height=260, border_width=1)
    tabview.place(x=10, y=112)

    def aba_aplicacao():
        tabview.add("Aplicação")
        frame_aplicacao = s.CTkFrame(tabview.tab("Aplicação"))
        frame_aplicacao.pack(fill="both", expand=True)

        label = s.CTkLabel(frame_aplicacao, text='APLICAÇÃO =', width=10, height=10, font=('arial bold', 12)).place(x=30, y=3)
        tanques_options = ["TANQUE CILINDRICO FUNDO RETO", "TAQUE CILINDRICO FUNDO CÔNICO", "TANQUE RETANGULAR VERTICAL RETO",
        "TANQUE RETANGULAR VERTICAL COM CALHA", "CALHA PARSHALL", "CERTEDOURO TRAPEZOIDAL"]

        imagem_labels = {
            "TANQUE CILINDRICO FUNDO RETO": {
                "posicao": (15, 0),
                "imagem1": "C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/coreAPP00.png",
                "texto1": "Dis.",
                "texto2": "Col. ",
                "texto3": "Dis Max. ",
                "imagem2": "C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/CoreAPP00_DIM.png",
                "texto4": "Diâm. ",
                "texto5": "Dis Max."
            },
            "TAQUE CILINDRICO FUNDO CÔNICO": {
                "posicao": (15, 0),
                "imagem1": "C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/coreAPP01.png",
                "texto1": "Dis.",
                #"texto2": "Col. ",
                #"texto3": "Dis Max. ",
                "imagem2": "C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/CoreAPP01_DIM1.png",
                #"texto4": "Diâm. ",
                #"texto5": "Dis Max."
            },
            "TANQUE RETANGULAR VERTICAL RETO": {
                "posicao": (15, 0),
                "imagem1": "C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/CoreAPP02_DIM.png",
                "texto1": "Diâm.",
                "texto2": "Dis.max.",
                "texto3": "Dis Max. ",
                "imagem2": "C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/CoreAPP02_DIM.png",
                "texto4": "Diâm. ",
                "texto5": "Dis Max."
            },
            "TANQUE RETANGULAR VERTICAL COM CALHA": {
                "posicao": (15, 0),
                "imagem1": "C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/CoreAPP03.png",
                "texto1": "Diâm.",
                "texto2": "Dis.max.",
                "texto3": "Dis Max. ",
                "imagem2": "C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/CoreAPP03_DIM.png",
                "texto4": "Diâm. ",
                "texto5": "Dis Max."
            },
            "CALHA PARSHALL": {
                "posicao": (15, 0),
                "imagem1": "C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/CoreAPP09.png",
                #"texto1": "Diâm.",
                #"texto2": "Dis.max.",
                #"texto3": "Dis Max. ",
                "imagem2": "C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/CoreAPP09_1.png",
                #"texto4": "Diâm. ",
                #"texto5": "Dis Max."
            },
            "CERTEDOURO TRAPEZOIDAL": {
                "posicao": (15, 0),
                "imagem1": "C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/CoreAPP12.png",
                "texto1": "Diâm.",
                "texto2": "Dis.max.",
                "texto3": "Dis Max. ",
                "imagem2": "C:/Users/pedri/Downloads/BLIT-U-Def/Imagens/CoreAPP12_1.png",
                "texto4": "Diâm. ",
                "texto5": "Dis Max."
            },
        }

        menu1_var = tk.StringVar(value=tanques_options[0])

        tanques_menu = s.CTkOptionMenu(frame_aplicacao, variable=menu1_var, values=tanques_options, width=250, height=20, fg_color="white", text_color="black", font=('arial bold', 12))
        tanques_menu.place(x=140, y=0)

        imagem_label1 = s.CTkLabel(frame_aplicacao, text=" ")
        imagem_label1.pack()

        imagem_label2 = s.CTkLabel(frame_aplicacao, text=" ")
        imagem_label2.place(x=690, y=45)

        def tanques1(*args):
            tanque_selecionado = menu1_var.get()
            dados_tanque = imagem_labels.get(tanque_selecionado, {})
            posicao = dados_tanque.get("posicao", (0, 0))
            imagem_path1 = dados_tanque.get("imagem1", "")
            imagem_path2 = dados_tanque.get("imagem2", "")
            texto1 = dados_tanque.get("texto1", "")
            texto2 = dados_tanque.get("texto2", "")
            texto3 = dados_tanque.get("texto3", "")
            texto4 = dados_tanque.get("texto4", "")
            texto5 = dados_tanque.get("texto5", "")

            
            imagem1 = Image.open(imagem_path1)
            photo1 = ImageTk.PhotoImage(imagem1)
            imagem_label1.configure(image=photo1)
            imagem_label1.image = photo1

            imagem2 = Image.open(imagem_path2)
            photo2 = ImageTk.PhotoImage(imagem2)
            imagem_label2.configure(image=photo2)
            imagem_label2.image = photo2

            label1_imagem = s.CTkLabel(frame_aplicacao, text=texto1, font=('arial', 11)).place(x=posicao[0] + 400, y=posicao[1] + 115)
            label2_imagem = s.CTkLabel(frame_aplicacao, text=texto2, font=('arial', 11)).place(x=posicao[0] + 400,y=posicao[1] + 170)                                                                        
            label3_imagem = s.CTkLabel(frame_aplicacao, text=texto3, font=('arial', 11)).place(x=posicao[0] + 570, y=posicao[1] + 130)
            label4_imagem = s.CTkLabel(frame_aplicacao, text=texto4, font=('arial', 11)).place(x=posicao[0] + 695,y=posicao[1] + 25)
            label5_imagem = s.CTkLabel(frame_aplicacao, text=texto5, font=('arial', 11)).place(x=posicao[0] + 760,y=posicao[1] + 120)                                                                                  

        # Adiciona a função tanques_funcao_1 para ser chamada sempre que o valor do menu for alterado
        menu1_var.trace_add('write', tanques1)

        def tanques2(*args):
            tanque_selecionado = menu1_var.get()
            dados_tanque = imagem_labels.get(tanque_selecionado, {})
            posicao = dados_tanque.get("posicao", (0, 0))
            imagem_path1 = dados_tanque.get("imagem1", "")
            imagem_path2 = dados_tanque.get("imagem2", "")
            texto1 = dados_tanque.get("texto1", "")
            texto2 = dados_tanque.get("texto2", "")
            texto3 = dados_tanque.get("texto3", "")

            imagem1 = Image.open(imagem_path1)
            photo1 = ImageTk.PhotoImage(imagem1)
            imagem_label1.configure(image=photo1)
            imagem_label1.image = photo1

            imagem2 = Image.open(imagem_path2)
            photo2 = ImageTk.PhotoImage(imagem2)
            imagem_label2.configure(image=photo2)
            imagem_label2.image = photo2

            label1_imagem = s.CTkLabel(frame_aplicacao, text=texto1, font=('arial', 11)).place(x=posicao[0] + 400, y=posicao[1] + 115)
            label2_imagem = s.CTkLabel(frame_aplicacao, text=texto2, font=('arial', 11)).place(x=posicao[0] + 400,y=posicao[1] + 170)                                                                        
            label3_imagem = s.CTkLabel(frame_aplicacao, text=texto3, font=('arial', 11)).place(x=posicao[0] + 570, y=posicao[1] + 130)

        menu1_var.trace_add('write', tanques2)



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

tabview()

janela.mainloop()