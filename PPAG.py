##-----------------------------------------------------------------------------------------------
## CARGA PPAG ##
##-----------------------------------------------------------------------------------------------
# Importando os Módulos
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time

class ExecutorCargaPPAG:
    def executarCargaPPAG():
            # ABRIR O NAVEGADOR
            navegador = webdriver.Chrome()

            # ACESSAR O SITE DO CIC:
            navegador.get('http://cic-hm.pbh/')

            # ENCONTRAR O ELEMENTO COM A TAG NAME NO HTML E ESCREVENDO NO CAMPO O LOGIN DO SISTEMA:
            navegador.find_element(By.NAME, 'josso_username').send_keys('thiago.conegundes')

            # ENCONTRAR O ELEMENTO COM A TAG NAME NO HTML E ESCREVER A SENHA PARA ACESSAR O SISTEMA:
            navegador.find_element(By.NAME, 'josso_password').send_keys('Th1505@')

            # Clicar no botão para acessar o sistema:
            navegador.find_element(By.CLASS_NAME, "botao").click()

            # Clicar na opção do Menu Cargaas de sistemas
            navegador.find_element(By.XPATH, '//*[@id="geral"]/div[2]/ul/li[5]/a').click()

            # Acessando a opção Carga de produção
            navegador.find_element(By.XPATH, '//*[@id="geral"]/div[2]/ul/li[5]/ul/li[5]/a').click()

            # Escolhendo a carga PPAG para ser ralizada:
            navegador.find_element(By.ID, "administrativo-13").click()

            # Clicar na opção do agendador
            navegador.find_element(By.ID, "datahora").click()
            # ------------------------------------------------------------------------

            ##Calculo do minuto adicional
            dataCompletaSistema = datetime.now()
            dataFormatadaString = dataCompletaSistema.strftime('%d/%m/%Y %H:%M')
            minutoSeparadoString = dataCompletaSistema.strftime('%M')
            minutoSeparadoInt = int(minutoSeparadoString)

            # Caso tradicional: Incrementar um minuto
            minutoIncrementado = (minutoSeparadoInt + 2)
            minutoIncrementado = str(minutoIncrementado)
            dataSeparadaComMinuto = dataFormatadaString[0:14]
            tempoFinal = (dataSeparadaComMinuto + minutoIncrementado)

            # Caso o minuto chegar em 58 ou 59 é necessário zerar os minutos e incrementar as horas
            if (minutoSeparadoInt == 58 or minutoSeparadoInt == 59):
                horaSeparadaString = dataCompletaSistema.strftime('%I')
                horaSeparadaInt = int(horaSeparadaString)
                horaSeparadaInt = horaSeparadaInt + 1
                horaSeparadaString = str(horaSeparadaInt)
                minutoIncrementado = 2
                minutoIncrementadoString = str(minutoIncrementado)
                novaData = dataFormatadaString[0:11]
                horaFinal = (horaSeparadaString + ':0' + minutoIncrementadoString)
                dataFinal = (novaData + horaFinal)
                navegador.find_element(By.ID, "datahora").send_keys(dataFinal)
                print(tempoFinal)

            # ----------------------------------------------------------------------------------
            # Caso estivermos no intervalo de tempo do minuto 00 à 09
            if (minutoSeparadoInt >= 0 and minutoSeparadoInt <= 7):
                minutoSeparadoInt = minutoSeparadoInt + 2
                minutoSeparadoString = str(minutoSeparadoInt)
                minutoSeparadoString = ('0' + minutoSeparadoString)
                novadata = dataFormatadaString[0:14]
                dataFinal = (novadata + minutoSeparadoString)
                print(dataFinal)
                # Escrevendo o horário no campo data hora
                navegador.find_element(By.ID, "datahora").send_keys(dataFinal)

            navegador.find_element(By.ID, "datahora").send_keys(tempoFinal)
            time.sleep(3)
            # Clicar no botão Gravar
            navegador.find_element(By.ID, "gravar").click()
            time.sleep(4000)

    try:
        executarCargaPPAG();
    except:
        executarCargaPPAG();

meuObjetoTeste = ExecutorCargaPPAG
for x in range(0,10):
    try:
        meuObjetoTeste.executarCargaPPAG()
    except:
        meuObjetoTeste.executarCargaPPAG()