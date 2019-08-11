from pylab import *
from tkinter import *

janela = Tk()

def bt_click():
    print("Clicado!")

    if(str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()
            and str(ed3.get()).isnumeric() and str(ed4.get()).isnumeric()
                and str(ed5.get()).isnumeric() and str(ed6.get()).isnumeric()
                    and str(ed7.get()).isnumeric() and str(ed8.get()).isnumeric()
                        and str(ed9.get()).isnumeric() and str(ed10.get()).isnumeric()):

        zero = int(ed1.get())
        um = int(ed2.get())
        dois = int(ed3.get())
        tres = int(ed4.get())
        quatro = int(ed5.get())
        cinco = int(ed6.get())
        seis = int(ed7.get())
        sete = int(ed8.get())
        oito = int(ed9.get())
        nove = int(ed10.get())

        pos = arange(10)                             # posiçoes

        bar(pos, (zero, um, dois, tres, quatro, cinco, seis, sete, oito, nove),         # Gera colunas no centido vertical
            align='center', color='#696969')

        tick_params(axis='x', colors='#696969')
        tick_params(axis='y', colors='#696969')
        xlabel('Numeros', color='blue')
        ylabel('Frequencia', color='blue')
        title('Histograma de Frequencia dos Digito de (0 á 9)', color='blue')
        subplots_adjust(bottom=.16, right=.99)
        xticks(pos, size='small')                    # Tamanho de fonte no eixo 'x'

        grid()                                       # Coloca grade de referencia no grafico
        show()                                       # Mostrar o grafico


    else:
        #lb["text"] = "Valores invalidos."
        lb["text"] = "Aceito apenas numeros \n positivos inteiros."

lb0 = Label(janela, text = "GERADOR DE GRÁFICO DE FREQUENCIA", bg = "#C0C0C0")
lb0.place(x = 90, y = 10)

lb1 = Label(janela, text = "ZERO", bg = "#C0C0C0")
lb1.place(x = 50, y = 45)
ed1 = Entry(janela)
ed1.place(x = 110, y = 45)

lb2 = Label(janela, text = "UM", bg = "#C0C0C0")
lb2.place(x = 50, y = 70)                            # distancia nome da caixa
ed2 = Entry(janela)
ed2.place(x = 110, y = 70)                           # distancia caixa

lb3 = Label(janela, text = "DOIS", bg = "#C0C0C0")
lb3.place(x = 50, y = 95)
ed3 = Entry(janela)
ed3.place(x = 110, y = 95)

lb4 = Label(janela, text = "TRÊS", bg = "#C0C0C0")
lb4.place(x = 50, y = 120)
ed4 = Entry(janela)
ed4.place(x = 110, y = 120)

lb5 = Label(janela, text = "QUATRO", bg = "#C0C0C0")
lb5.place(x = 50, y = 145)
ed5 = Entry(janela)
ed5.place(x = 110, y = 145)

lb6 = Label(janela, text = "CINCO", bg = "#C0C0C0")
lb6.place(x = 50, y = 170)
ed6 = Entry(janela)
ed6.place(x = 110, y = 170)

lb7 = Label(janela, text = "SEIS", bg = "#C0C0C0")
lb7.place(x = 50, y = 195)
ed7 = Entry(janela)
ed7.place(x = 110, y = 195)

lb8 = Label(janela, text = "SETE", bg = "#C0C0C0")
lb8.place(x = 50, y = 220)
ed8 = Entry(janela)
ed8.place(x = 110, y = 220)

lb9 = Label(janela, text = "OITO", bg = "#C0C0C0")
lb9.place(x = 50, y = 245)
ed9 = Entry(janela)
ed9.place(x = 110, y = 245)

lb10 = Label(janela, text = "NOVE", bg = "#C0C0C0")
lb10.place(x = 50, y = 270)
ed10 = Entry(janela)
ed10.place(x = 110, y = 270)

bt = Button(janela, text = "GERAR GRÁFICO", width = 20, command = bt_click, bg = "#696969")
bt.place(x = 230, y = 350)

lb = Label(janela, text = "STATUS", bg = "#C0C0C0")
lb.place(x = 50, y = 315)

lb11 = Label(janela, text = "DICA: Use Tab para navegar!", bg = "#C0C0C0")
lb11.place(x = 230, y = 310)

janela["bg"] = "#C0C0C0"
janela. geometry("400x400+50+50")
janela.mainloop()