import pyautogui as ag
from time import sleep
import datetime as dt
import keyboard
import sys

#Função responsavel por formatar a data.
def formata_data(): 
    data_atual = dt.date.today()
    dia_atual = data_atual.day
    mes_atual = data_atual.month
    mes_anterior = data_atual.month - 1
    ano_atual = data_atual.year

    #Trata o dia o numero de um digito para dois. ex: 9 => 09
    def formata_dia(dia_atual): 
        if dia_atual > 0 and dia_atual < 10:
            dia_atual = "0{}".format(dia_atual)
        return dia_atual
    
    #Trata o mes final, numero de um digito para dois. ex: 7 => 07
    def formata_mes_atual(mes_atual):
        if mes_atual > 0 and mes_atual < 10:
            mes_atual = "0{}".format(mes_atual)
        return mes_atual
    
    #Trata o mes inicial
    def formata_mes_anterior(mes_anterior, mes_atual, ano_atual):
        #Trata o mes ainicial quando o ano vira
        if mes_atual == 1:
            mes_anterior = 12
            ano_anterior = (ano_atual - 1)
        #Trata o mes inicial, numero de um digito para dois. ex: 7 => 07
        elif mes_anterior >= 1 and mes_anterior <= 9:
            mes_anterior = "0{}".format(mes_anterior)
            ano_anterior = ano_atual
        return mes_anterior, ano_anterior
    
    #Chamado das funções para obter o dia, mes e ano necessarios afim de setar o periodo.
    dia_atual = formata_dia(dia_atual)
    mes_anterior, ano_anterior = formata_mes_anterior(mes_anterior, mes_atual, ano_atual)
    mes_atual = formata_mes_atual(mes_atual)
    
    #Retorno das 4 variaveis necessarias.
    return dia_atual, mes_atual, mes_anterior, ano_atual, ano_anterior

#Função responsavel pela automatização da abertura do navegador utilizado.
def abre_navegador():
    ag.click(947,524, duration=1)
    ag.write('google')
    sleep(0.5)
    ag.press('enter')
    return 0

#Função responsavel pela automatização da abertura do whatsapp (ferramenta de comunicação).
def abre_whatsapp():
    keyboard.press_and_release('ctrl+l')
    sleep(0.3)
    ag.write('https://web.whatsapp.com/')
    ag.press('enter')
    return 0

#Função responsavel por abrie e configurar os filtros do painel de chamados 
# (ferramenta gerencial de trabalho).
def abre_configura_painel():
    keyboard.press_and_release('ctrl+t')
    sleep(0.5)
    keyboard.press_and_release('ctrl+l')
    ag.write(link_1)
    keyboard.press_and_release('shift+/')
    ag.write(link_2)
    ag.press('enter')
    return 0

#Abre uma janela aninima para o whatsapp pessoal caso necessario.
def abre_whatsapp_pessoal():
    keyboard.press_and_release('ctrl+shift+n')
    sleep(0.5)
    keyboard.press_and_release('ctrl+l')
    sleep(0.3)
    ag.write('https://web.whatsapp.com/')
    ag.press('enter')
    sleep(0.3)
    keyboard.press_and_release('alt+tab')
    return 0

#Função responsavel por abri a ferramenta de acesso remoto no trabalho.
def abre_anydesk():
    caminho_any = "C:/Users/User/Downloads/anydesk (1).exe"
    keyboard.press_and_release('windows+r')
    sleep(0.5)
    ag.write(caminho_any)
    sleep(0.3)
    ag.press('enter')
    return 0

#Set das variaveis e chamado da função para obter o dia os messes e o ano necessarios para encontrar o periodo.
dia_format, mes_atual_format, mes_passado_format, ano, ano_passado= formata_data()

#Link padrão para acesso ao painel de chamados.
#'format' para se ajustar a data atual automaticamente.
link_1 = "https://painel.topsoft.cloud/chamado"
link_2 = "chamado_id=&cliente_id=&filial_id=&tipo_periodo=previsao&periodo_inicial={}%2F{}%2F{}&periodo_final={}%2F{}%2F{}&status=pendente&status_pos=&setor=1&sistema_id=&modulo_id=&funcionario_id=".format(dia_format,mes_passado_format,ano_passado,dia_format,mes_atual_format,ano)

#Tempo de espera para esperar o computador iniciar e rodar tranquilamente o programa.
sleep(7)

#Chamado das funções para automatizar a abertura e configuração das ferramentas utilizadas no trabalho.
abre_navegador()
sleep(3)
abre_whatsapp()
sleep(0.5)
abre_configura_painel()
sleep(2)
abre_whatsapp_pessoal()
sleep(2)
abre_anydesk()

sys.exit()