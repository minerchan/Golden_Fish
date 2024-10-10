import pyautogui
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import time

# =================================== IMPORTANT FUNCTIONS AND VARIABLES  =================================================

window = Tk()

canvas = Canvas(
    window,
    bg = "#8165AA",
    height = 970,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)


def begin():
    screen_width, screen_height = pyautogui.size()
    left_region = (0, 0, screen_width // 2, screen_height)
    pyautogui.click(left_region)
    time.sleep(1)
    return left_region

def update_text(text):
    canvas.itemconfig(display, text=text)
    
def update_items(items):
    canvas.itemconfig(items, text=str("x" + items))
    
def update_money(money):
    canvas.itemconfig(money, text=str("R$" + money))

def move_1():
    
    press('K')
    time.sleep(0.2)
    press('K')
    
def move_2():
    press('K')
    time.sleep(0.2)
    press('D')
    press('K')

def move_3():
    press('K')
    time.sleep(0.2)
    press('S')
    press('K')
    
def move_4():
    press('K')
    time.sleep(0.2)
    press('D')
    press('S')
    press('K')
    
    
def click_on_pokeball():
    pokeball = (404, 467, 130, 25)
    pyautogui.moveTo(pokeball, duration=0.2)
    pyautogui.click()
    # Tempo da ball rolar 3x
    time.sleep(7)



# Esta função espera uma string no 1 argumento um number no 2
def keep_press(tecla, segundos):
    # aperta a tecla
    pyautogui.press(tecla)
    # Pressiona a tecla '...'
    pyautogui.keyDown(tecla)
    # Aguarda 2 segundos
    time.sleep(segundos)
    # Solta a tecla '...'
    pyautogui.keyUp(tecla)



def going_to_the_pokecenter(display_text):
    update_text("Using teleport...")
    press('7')
    time.sleep(4)
    update_text("Healing pokemons...")
    keep_press('K', 0.5)
    time.sleep(1)
    keep_press('K', 0.5)
    time.sleep(3)
    keep_press('K', 0.5)
    time.sleep(0.5)
    update_text("Walking to the beach...")
    keep_press('S', 2.7)
    time.sleep(1)
    
def press(tecla):
    pyautogui.press(tecla)
    
# =================================== CORE =================================================

def fishing():
    pokemon_killed_by_payday = 0
    average_money_per_pokemon = 487
    left_region = begin()
    thief = 25
    payday = 20
    going_to_the_pokecenter()
    keep_press('A', 1.6)
    keep_press('S', 2)
    keep_press('D', 0.2)
    #  HORA DE PESCAR
    farmed_item = 0
    controle_geral = False
    while controle_geral is False:
        if(thief == 0 or payday == 0):
            going_to_the_pokecenter()
            thief = 25
            payday = 20
            keep_press('A', 1.6)
            keep_press('S', 2)
            keep_press('D', 0.2)
        # =================================== BLOCO PARA CONFERIR SE TEM ITEM NO POKÉMON ================================================    
        contador_de_item_segurado = 0
        controle_de_item_segurado = False
        while controle_de_item_segurado is False:
            try:
                item_segurado = pyautogui.locateOnScreen('./imagens/itemsegurado.png', confidence=0.9)
                farmed_item = farmed_item + 1
                update_text("Storing the stolen item")
                pyautogui.moveTo(item_segurado)
                pyautogui.click()
                time.sleep(0.5)
                keep_press('S', 0.3)
                press('K')
                time.sleep(0.5)
                controle_de_item_segurado = True
            except pyautogui.ImageNotFoundException:
                contador_de_item_segurado = contador_de_item_segurado + 1
                if(contador_de_item_segurado == 10):
                    controle_de_item_segurado = True
        
    # =================================== BLOCO PARA PESCAR ATÉ ENTRAR EM LUTA ================================================
        controle_de_pesca = False
        while controle_de_pesca is False:
            try:
                entramos_em_luta = pyautogui.locateOnScreen('./imagens/entrouemluta.png', confidence=0.8, region=(left_region))
                print("Entramos em luta")
                controle_de_pesca = True
                # tempo para interface descansar
                time.sleep(1)
            except pyautogui.ImageNotFoundException:
                keep_press('8', 0.5)
                time.sleep(3)
                press('K')
        
    # =================================== BLOCO DE IDENTIFICAÇÃO ================================================
        controle_de_identificacao = False
        contador_de_checagem_luvdisc = 0
        while controle_de_identificacao is False:
            try:
                luvdisc = pyautogui.locateOnScreen('./imagens/luvdisc.png', confidence=0.8, region=(left_region))
                print("É um luvdisc")
                controle_pra_ver_se_foge_ou_mata = False
                controle_de_identificacao = True
            except pyautogui.ImageNotFoundException:
                contador_de_checagem_luvdisc = contador_de_checagem_luvdisc + 1
                time.sleep(0.1)
                if(contador_de_checagem_luvdisc == 10):
                    "Não era um luvdisc"
                    controle_de_identificacao = True
                    controle_pra_ver_se_foge_ou_mata = True
                    
    # =================================== BLOCO PARA VER SE FOGE OU MATA ================================================
        if(controle_pra_ver_se_foge_ou_mata is False):
            print("Vou farmar item tirei")
            time.sleep(2)
            move_2()
            thief = thief - 1
            print("Temos " + str(thief) + " moves de thief")
            time.sleep(10)
            print("Aqui acaba o tempo de espera pós luvdisc")
            
        else:
            print("Vou farmar dinheiro")
            move_1()
            payday = payday - 1
            print("Temos " + str(payday) + " moves de payday")
            pokemon_killed_by_payday = pokemon_killed_by_payday + 1
            update_money(str(pokemon_killed_by_payday * average_money_per_pokemon))
            print("Dinheiro farmado com itens e pokes R$:" + str(((farmed_item * 7000) + (pokemon_killed_by_payday * average_money_per_pokemon))))
            time.sleep(9)
            
        
        print("Número de itens farmados: " + str(farmed_item))
        
        print("==============================")


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Samuel\Desktop\GOLDEN_FISH\build\assets\frame0")

def create_rounded_rect(canvas, x1, y1, x2, y2, radius=10, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)
def on_enter(event):
    canvas.config(cursor="hand2")

def on_leave(event):
    canvas.config(cursor="")

def stop_function(event):
    controle_geral = True

def start_function(event):
    print("start")
    canvas.itemconfig(display, text="start")

def bind_cursor(elements, function):
    for element in elements:
        canvas.tag_bind(element, "<Enter>", on_enter)
        canvas.tag_bind(element, "<Leave>", on_leave)
        canvas.tag_bind(element, "<Button-1>", function)
        
    
largura_da_janela = 900
altura_da_janela = 970
largura_da_tela, altura_da_tela = pyautogui.size()
posicao_x = largura_da_tela - largura_da_janela - 15
posicao_y = 2        


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)




window.geometry(f"{largura_da_janela}x{altura_da_janela}+{posicao_x}+{posicao_y}")
window.configure(bg = "#8165AA")




canvas.place(x = 0, y = 0)

window.title("Goldenfish")

meowth_image = PhotoImage(file=relative_to_assets("meowth.png"))
heart_scale_image = PhotoImage(file=relative_to_assets("heartscale.png"))
gold_image = PhotoImage(file=relative_to_assets("gold.png"))
github_image = PhotoImage(file=relative_to_assets("github.png"))
start_image = PhotoImage(file=relative_to_assets("start.png"))
stop_image = PhotoImage(file=relative_to_assets("stop.png"))


canvas.create_text(
    19.0,
    6.0,
    anchor="nw",
    text="Goldenfish",
    fill="#F9D662",
    font=("Jaro Regular", 96 * -1)
)

canvas.create_image(640, 327, image=meowth_image, anchor="center")

canvas.create_rectangle(
    0.0,
    735.0,
    900.0,
    970.0,
    fill="#2A2433",
    outline="")

# Sombra
create_rounded_rect(canvas, 655.0,
    642.0,
    876.0,
    722.0, radius=20, fill="#4B3F72")

# Botão
button = create_rounded_rect(canvas,   655.0,
    642.0,
    876.0,
    718.0, radius=20, fill="#9B3220")

texto = canvas.create_text(
    752.0,
    654.0,
    anchor="nw",
    text="STOP",
    fill="#F8F9FA",
    font=("Jaro Regular", 36 * -1)
)

figure = canvas.create_image(703, 678, image=stop_image, anchor="center")

bind_cursor([button, texto, figure], stop_function) 

# Sombra
create_rounded_rect(canvas, 399.0,
    642.0,
    621.0,
    722.0, radius=20, fill="#4B3F72")

# Botão
button2 = create_rounded_rect(canvas,   399.0,
    642.0,
    621.0,
    718.0, radius=20, fill="#A04E26")

texto2 = canvas.create_text(
    472.0,
    654.0,
    anchor="nw",
    text="START",
    fill="#F8F9FA",
    font=("Jaro Regular", 36 * -1)
)

figure2 = canvas.create_image(436, 678, image=start_image, anchor="center")

bind_cursor([button2, texto2, figure2], start_function)
 


canvas.create_image(68.5, 250.5, image=heart_scale_image, anchor="center")

display_items = canvas.create_text(
    119.0,
    213.0,
    anchor="nw",
    text="x 0",
    fill="#F8F9FA",
    font=("Jaldi", 48 * -1)
)

money = canvas.create_text(
    119.0,
    412.0,
    anchor="nw",
    text="R$ 0",
    fill="#F8F9FA",
    font=("Jaldi", 48 * -1)
)

canvas.create_text(
    99.0,
    645.0,
    anchor="nw",
    text="minerchan",
    fill="#F8F9FA",
    font=("Jaldi", 48 * -1)
)


canvas.create_image(63.5, 450.5, image=gold_image, anchor="center")

canvas.create_text(
    34.0,
    160.0,
    anchor="nw",
    text="ITEMS",
    fill="#FFFEDF",
    font=("Jaldi Regular", 32 * -1)
)

canvas.create_text(
    34.0,
    351.0,
    anchor="nw",
    text="MONEY",
    fill="#FFFEDF",
    font=("Jaldi Regular", 32 * -1)
)

canvas.create_image(45.5, 683.5, image=github_image, anchor="center")

display = canvas.create_text(
    19.0,
    735.0,
    anchor="nw",
    text="",
    fill="#F8F9FA",
    font=("Jaldi", 96 * -1)
)




window.resizable(False, False)
window.mainloop()
