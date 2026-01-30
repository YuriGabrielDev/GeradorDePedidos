import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont
import os
#
diretorio = os.path.dirname(os.path.abspath(__file__))
entrada = os.path.join(diretorio, 'arquivos')
saida = r'E:\Users\USER\Files\Pedidos gerados\A enviar'
#
def area_reset():
    global area
    area = {}
    for lf in range(12):
        area[lf+1]= {}
        for cf in range(12):
            area[lf+1][cf+1] = True

def write(imgw, texto, pos=(0, 0), tam=50, cor=(0,0,0), rot='horizontal'):
    global entrada
    texto = str(texto)
    fonte = ImageFont.truetype(os.path.join(entrada, 'calibri-regular.ttf'), tam)
    if cor == 'branco':
        cor = (255, 255, 255)
    elif cor == 'preto':
        cor = (0, 0, 0)
    elif cor == 'vermelho':
        cor = (255, 0, 0)
    elif cor == 'verde':
        cor = (0, 255, 0)
    elif cor == 'azul':
        cor = (0, 0, 255)
    if rot == 'horizontal':
        draw = ImageDraw.Draw(imgw)
        draw.text(pos, texto, fill=cor, font=fonte)
    elif rot == 'vertical':
        pos = (imgw.height - pos[1], pos[0])
        imgwr = imgw.rotate(270, expand=1)
        draw = ImageDraw.Draw(imgwr)
        draw.text(pos, texto, fill=cor, font=fonte)
        imgw = imgwr.rotate(90, expand=1)
    return imgw

def salvar(imgs, nome):
    global saida
    if nome == '':
        nome = 'pedido'
    caminho = os.path.join(saida, nome+'.png') 
    number = 0
    while os.path.exists(caminho):
        number += 1
        caminho = os.path.join(saida, nome+str(number)+'.png')  
    imgs.save(caminho)

    
def check(altC, largC):
    global area
    retorno = None
    celula = None
    for linha in area:
        for coluna in area[linha]:
            if linha + altC -1 > 12 or coluna + largC -1> 12:
                continue
            for uniA in range(altC):
                for uniL in range(largC):
                    celula = area[linha+uniA][coluna+uniL]
                    if celula == False:
                        break
                if celula == False:
                    break
            if celula == False:
                continue
            retorno = (linha, coluna)
            break
        if retorno != None:
            break
    return retorno

def fals(linha, coluna, altura, largura):
    for l in range(altura):
        for c in range(largura):
            area[linha+l][coluna+c] = False

def jan4f(imgf, linha, coluna, alt, larg, bt): #janela 4 folhas
    global area
    if bt:
        img2 = Image.open(os.path.join(entrada, 'janela4f1.png'))
    else:
        img2 = Image.open(os.path.join(entrada, 'janela4f.png'))
    a = int(((coluna - 1) * 91.33) + 4)
    b = int(((linha - 1) * 99.16) + 420)
    imgf.paste(img2, (a + 24, b + 24))
    rest = (larg/4) % 50
    if rest > 0 and rest <= 25:
        largM = larg/4 + 50 - rest
        largF = larg/4 + rest
    else:
        largM = larg/4 + 50
        largF = larg/4
    altF = alt - 60
    altM = alt - 20
    imgf = write(imgf, str(larg), (a + 148, b + 165), 25) #largura total
    imgf = write(imgf, str(int(largF)), (a + 40, b + 140), 25) #largura fixo
    imgf = write(imgf, str(int(largF)), (a + 270, b + 140), 25) #largura fixo
    imgf = write(imgf, str(int(largM)), (a + 115, b + 140), 25) #largura móvel
    imgf = write(imgf, str(int(largM)), (a + 195, b + 140), 25) #largura móvel
    imgf = write(imgf, str(alt), (a + 2 , b + 121), 25, rot='vertical') #altura total
    imgf = write(imgf, str(altF), (a + 25, b + 121), 25, rot='vertical') #altura fixo
    imgf = write(imgf, str(altF), (a + 300, b + 121), 25, rot='vertical') #altura fixo
    imgf = write(imgf, str(altM), (a + 95, b + 121), 25, rot='vertical') #altura movel
    imgf = write(imgf, str(altM), (a + 230, b + 121), 25, rot='vertical') #altura movel
    img2.close()
    return imgf

def jan2f(imgf, linha, coluna, alt, larg, bt): #janela 2 folhas
    global area
    if bt:
        img2 = Image.open(os.path.join(entrada, 'janela2f1.png'))
    else:
        img2 = Image.open(os.path.join(entrada, 'janela2f.png'))
    a = int(((coluna - 1) * 91.33) + 4)
    b = int(((linha - 1) * 99.16) + 420)
    imgf.paste(img2, (a + 24, b + 24))
    if larg > 600:
        rest = larg / 2 % 50
        if rest > 0 and rest <= 25:
            largM = larg/2 + 50 - rest
            largF = larg/2 + rest
        else:
            largM = larg/2 + 50
            largF = larg/2
    else:
        rest = (larg / 2 + 30) % 50
        if rest > 0 and rest <= 15:
            largM = larg/2 + 30 - rest
            largF = larg/2 + rest
        else:
            largM = larg/2 + 30
            largF = larg/2
    altF = alt - 60
    altM = alt - 20
    imgf = write(imgf, str(larg), (a + 107, b + 252), 25) #largura total
    imgf = write(imgf, str(int(largF)), (a + 60, b + 229), 25) #largura fixo
    imgf = write(imgf, str(int(largM)), (a + 172, b + 229), 25) #largura móvel
    imgf = write(imgf, str(alt), (a + 2 , b + 160), 25, rot='vertical') #altura total
    imgf = write(imgf, str(altF), (a + 25, b + 160), 25, rot='vertical') #altura fixo
    imgf = write(imgf, str(altM), (a + 134, b + 160), 25, rot='vertical') #altura movel
    img2.close()
    return imgf

def prt4f(imgf, linha, coluna, alt, larg, pux): #janela 4 folhas
    global area
    if pux:
        img2 = Image.open(os.path.join(entrada, 'porta4fCP.png'))
        adic = 35
    else:
        img2 = Image.open(os.path.join(entrada, 'porta4fSP.png'))
        adic = 0
    a = int(((coluna - 1) * 91.33) + 4)
    b = int(((linha - 1) * 99.16) + 420)
    imgf.paste(img2, (a + 24, b + 24))
    rest = (larg/4+adic) % 50
    if rest > 0 and rest <= 25:
        largM = larg/4 + 50 - rest + adic
        largF = larg/4 + rest - adic
    else:
        largM = larg/4 + 50 + adic
        largF = larg/4 - adic
    altF = alt - 60
    altM = alt - 20
    imgf = write(imgf, str(larg), (a + 150, b + 245), 25) #largura total
    imgf = write(imgf, str(int(largF)), (a + 40, b + 222), 25) #largura fixo
    imgf = write(imgf, str(int(largF)), (a + 275, b + 222), 25) #largura fixo
    imgf = write(imgf, str(int(largM)), (a + 115, b + 222), 25) #largura móvel
    imgf = write(imgf, str(int(largM)), (a + 195, b + 222), 25) #largura móvel
    imgf = write(imgf, str(alt), (a + 2 , b + 170), 25, rot='vertical') #altura total
    imgf = write(imgf, str(altF), (a + 25, b + 170), 25, rot='vertical') #altura fixo
    imgf = write(imgf, str(altF), (a + 307, b + 170), 25, rot='vertical') #altura fixo
    imgf = write(imgf, str(altM), (a + 96, b + 170), 25, rot='vertical') #altura movel
    imgf = write(imgf, str(altM), (a + 232, b + 170), 25, rot='vertical') #altura movel
    img2.close()
    return imgf

def prt2f(imgf, linha, coluna, alt, larg, pux): #janela 2 folhas
    global area
    if pux:
        img2 = Image.open(os.path.join(entrada, 'porta2fCP.png'))
        adic = 35
    else:
        img2 = Image.open(os.path.join(entrada, 'porta2fSP.png'))
        adic = 0
    a = int(((coluna - 1) * 91.33) + 4)
    b = int(((linha - 1) * 99.16) + 420)
    imgf.paste(img2, (a + 24, b + 24))
    rest = (larg/2+adic) % 50
    if rest > 0 and rest <= 25:
        largM = larg/2 + 50 - rest + adic
        largF = larg/2 + rest - adic
    else:
        largM = larg/2 + 50 + adic
        largF = larg/2 - adic
    altF = alt - 60
    altM = alt - 20
    imgf = write(imgf, str(larg), (a + 70, b + 245), 25) #largura total
    imgf = write(imgf, str(int(largF)), (a + 40, b + 222), 25) #largura fixo
    imgf = write(imgf, str(int(largM)), (a + 115, b + 222), 25) #largura móvel
    imgf = write(imgf, str(alt), (a + 2 , b + 170), 25, rot='vertical') #altura total
    imgf = write(imgf, str(altF), (a + 25, b + 170), 25, rot='vertical') #altura fixo
    imgf = write(imgf, str(altM), (a + 96, b + 170), 25, rot='vertical') #altura movel
    img2.close()
    return imgf

def basc(imgf, linha, coluna, alt, larg): #basculante
    global area
    img2 = Image.open(os.path.join(entrada, 'basculante.png'))
    a = int(((coluna - 1) * 91.33) + 4)
    b = int(((linha - 1) * 99.16) + 420)
    imgf.paste(img2, (a + 24, b + 24))
    largV = larg - 10
    altV = alt - 15
    imgf = write(imgf, str(larg), (a + 70, b + 145), 25) #largura total
    imgf = write(imgf, str(int(largV)), (a + 70, b + 123), 25) #largura vidro
    imgf = write(imgf, str(alt), (a + 2 , b + 115), 25, rot='vertical') #altura total
    imgf = write(imgf, str(altV), (a + 25, b + 115), 25, rot='vertical') #altura vidro
    img2.close()
    return imgf

def Pgiro(imgf, linha, coluna, alt, larg): #porta de giro
    global area
    img2 = Image.open(os.path.join(entrada, 'portagiro.png'))
    a = int(((coluna - 1) * 91.33) + 4)
    b = int(((linha - 1) * 99.16) + 420)
    imgf.paste(img2, (a + 24, b + 24))
    largV = larg - 10
    altV = alt - 15
    imgf = write(imgf, str(larg), (a + 70, b + 275), 25) #largura total
    imgf = write(imgf, str(int(largV)), (a + 70, b + 250), 25) #largura vidro
    imgf = write(imgf, str(alt), (a + 2 , b + 170), 25, rot='vertical') #altura total
    imgf = write(imgf, str(altV), (a + 25, b + 170), 25, rot='vertical') #altura vidro
    img2.close()
    return imgf
#
lista_NO = {'Incolor':{},'Verde':{},'Fumê':{}}
janela = tk.Tk()
janela.geometry('600x560')
janela.title("Gerador de pedido")
#
text1 = tk.Label(janela, text="Cliente:")
text1.grid(row=0, column=0, padx=10, pady=10, sticky="E")
cliente = tk.Entry(janela)
cliente.grid(row=0, column=1, padx=10, pady=10)
#
opcoes = ["Janela 4 folhas", "Janela 2 folhas", "Porta 4 folhas", "Porta 2 folhas", "Basculante", 'Porta de giro']
opcao_var = tk.StringVar()
for i, opcao in enumerate(opcoes):
    botao_opcao = tk.Radiobutton(janela, text=opcao, variable=opcao_var, value=opcao)
    botao_opcao.grid(row=i%3+1, column=i//3, padx=10, pady=5, sticky="W")
#
text2 = tk.Label(janela, text="Altura mm:")
text2.grid(row=4, column=0, padx=10, pady=10, sticky="E")
altura = tk.Entry(janela)
altura.grid(row=4, column=1, padx=10, pady=10)
text3 = tk.Label(janela, text="Largura mm:")
text3.grid(row=5, column=0, padx=10, pady=10, sticky="E")
largura = tk.Entry(janela)
largura.grid(row=5, column=1, padx=10, pady=10)
#
opcoes = ["Incolor", "Verde", "Fumê"]
opcao_var1 = tk.StringVar()
for i, opcao in enumerate(opcoes):
    botao_opcao = tk.Radiobutton(janela, text=opcao, variable=opcao_var1, value=opcao)
    botao_opcao.grid(row=i+6, column=0, padx=10, pady=5, sticky="W")
#
opcao_var2 =  tk.BooleanVar()
botao_opcao = tk.Checkbutton(janela, text='Puxador', variable=opcao_var2)
botao_opcao.grid(row=9, column=0, padx=10, pady=5, sticky="W")
#
opcao_var3 =  tk.BooleanVar()
botao_opcao = tk.Checkbutton(janela, text='Bate-fecha', variable=opcao_var3)
botao_opcao.grid(row=10, column=0, padx=10, pady=5, sticky="W")
#
def adicionar_f():
    if altura.get().isdigit() and largura.get().isdigit():
        if opcao_var.get() != '' and opcao_var1.get() != '':
            extra = ''
            pux = False
            match opcao_var.get():
                case "Janela 4 folhas":
                    if opcao_var3.get():
                        extra='bate-fecha '
                        pux = True
                        pref = 4
                    else:
                        pref = 3
                case "Janela 2 folhas":
                    if opcao_var3.get():
                        extra='bate-fecha '
                        pux = True
                        pref = 8
                    else:
                        pref = 9
                case "Porta 4 folhas":
                    if opcao_var2.get():
                        extra='com puxador '
                        pux = True
                        pref = 11
                    else:
                        pref = 10
                case "Porta 2 folhas":
                    if opcao_var2.get():
                        extra='com puxador '
                        pux = True
                        pref = 7
                    else:
                        pref = 6
                case "Basculante":
                    pref = 2
                case "Porta de giro":
                    pref = 5
            lista.insert(tk.END, f'{opcao_var.get()} {opcao_var1.get()} {extra}{altura.get()} x {largura.get()}')
            lista_NO[opcao_var1.get()][len(lista_NO[opcao_var1.get()])] = {'tipo':opcao_var.get(), 'altura':int(altura.get()), 'largura':int(largura.get()), 'pref':pref, 'pux':pux}
        else:
            messagebox.showwarning("Alerta", "Selecione o tipo ou/e a cor do item")
    else:
        messagebox.showwarning("Alerta", "Use apenas números nas medidas")
adicionar = tk.Button(janela, text="Adicionar item", command=adicionar_f)
adicionar.grid(row=11, column=0, pady=10, columnspan=2)
#
def gerar_f():
    global lista_NO
    if lista_NO != {'Incolor':{},'Verde':{},'Fumê':{}}:
        add = 0
        lista_O = {'Incolor':{},'Verde':{},'Fumê':{}}
        for cor_OL in lista_NO:
            while len(lista_NO[cor_OL]) > 0:
                maior = {'pref':-1}
                for item in lista_NO[cor_OL]:
                    if lista_NO[cor_OL][item]['pref'] > maior['pref']:
                        maior = lista_NO[cor_OL][item]
                        item_out = item
                del lista_NO[cor_OL][item_out]
                del maior['pref']
                lista_O[cor_OL][f'obj{add}'] = maior
                add += 1
        limpar_f()
        area = {}
        for i in ('Incolor', 'Fumê', 'Verde'):
            while len(lista_O[i]) > 0:
                img = Image.open(os.path.join(entrada, 'folhamp.png'))
                area_reset()
                remover = []
                for obj in lista_O[i]:
                    tipo_obj = lista_O[i][obj]['tipo']
                    objeto = lista_O[i][obj]
                    match tipo_obj:
                        case "Janela 4 folhas":
                            checagem = check(2,4)
                            if checagem != None:
                                linha, coluna = checagem
                                img = jan4f(img, linha, coluna, objeto['altura'], objeto['largura'], objeto['pux'])
                                fals(linha, coluna, 2, 4)
                                remover.append(obj)
                        case "Janela 2 folhas":
                            checagem = check(3,3)
                            if checagem != None:
                                linha, coluna = checagem
                                img = jan2f(img, linha, coluna, objeto['altura'], objeto['largura'], objeto['pux'])
                                fals(linha, coluna, 3, 3)
                                remover.append(obj)
                        case "Porta 4 folhas":
                            checagem = check(3,4)
                            if checagem != None:
                                linha, coluna = checagem
                                img = prt4f(img, linha, coluna, objeto['altura'], objeto['largura'], objeto['pux'])
                                fals(linha, coluna, 3, 4)
                                remover.append(obj)
                        case "Porta 2 folhas":
                            checagem = check(3,2)
                            if checagem != None:
                                linha, coluna = checagem
                                img = prt2f(img, linha, coluna, objeto['altura'], objeto['largura'], objeto['pux'])
                                fals(linha, coluna, 3, 2)
                                remover.append(obj)
                        case 'Basculante':
                            checagem = check(2,2)
                            if checagem != None:
                                linha, coluna = checagem
                                img = basc(img, linha, coluna, objeto['altura'], objeto['largura'])
                                fals(linha, coluna, 2, 2)
                                remover.append(obj)
                        case 'Porta de giro':
                            checagem = check(3, 2)
                            if checagem != None:
                                linha, coluna = checagem
                                img = Pgiro(img, linha, coluna, objeto['altura'], objeto['largura'])
                                fals(linha, coluna, 3, 2)
                                remover.append(obj)
                for item in remover:
                    del lista_O[i][item]
                quad = Image.open(os.path.join(entrada, 'Quad.png'))
                img.paste(quad, (12, 183))
                img.paste(quad, (166, 183))
                if i == 'Incolor':
                    img.paste(quad, (361, 183))
                elif i == 'Fumê':
                    img.paste(quad, (361, 224))
                elif i == 'Verde':
                    img.paste(quad, (361, 265))
                quad = Image.open(os.path.join(entrada, 'QuadB.png'))
                img.paste(quad, (837, 178))
                img = write(img, cliente.get(), (110, 360), 30)
                salvar(img, cliente.get())
                img.close()
        quad.close()
        messagebox.showinfo("Gerador de pedidos", "O pedido foi gerado")
    else:
        messagebox.showinfo("Alerta", "Nenhum item adicionado na lista")
gerar = tk.Button(janela, text="Gerar pedido", command=gerar_f)
gerar.grid(row=12, column=0, pady=10, columnspan=2)
#
lista = tk.Listbox(janela, width=50, height=30)
lista.grid(row=0, column=3, columnspan=2, padx=10, pady=10, rowspan=12)
#
def limpar_f():
    global lista_NO
    lista.delete(0, tk.END)
    lista_NO = {'Incolor':{},'Verde':{},'Fumê':{}}
limpar = tk.Button(janela, text="Limpar lista", command=limpar_f)
limpar.grid(row=12, column=3,columnspan=2)
#
janela.mainloop()
