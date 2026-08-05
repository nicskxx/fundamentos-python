import pywhatkit as kit
import pyautogui
import time

# ---- CONFIGURAÇÕES ----
numero_destino = "+55 19 99163-2230"
mensagem_texto = "Mensagem automática em loop!"
TEMPO_CARREGAMENTO = 8  # Segundos para carregar a página
INTERVALO_ENTRE_MENSAGENS = 5  # Segundos de descanso antes de mandar a próxima
# -----------------------

print("Controle de loop iniciado. Pressione CTRL + C no terminal do PyCharm para parar.")

contador = 1

# O bloco 'while True' faz o código rodar para sempre (infinito)
while True:
    print(f"\n[Envio #{contador}] Iniciando disparo...")

    try:
        # Envia a mensagem e fecha a aba em seguida
        kit.sendwhatmsg_instantly(
            phone_no=numero_destino,
            message=f"{mensagem_texto} (Envio número {contador})",
            wait_time=TEMPO_CARREGAMENTO,
            tab_close=True
        )

        # Garante o envio apertando Enter caso a página demore
        time.sleep(1)
        pyautogui.press('enter')

        print(f"[Envio #{contador}] Concluído com sucesso. Aguardando próximo ciclo...")
        contador += 1

        # Pausa de segurança obrigatória para o computador respirar
        time.sleep(INTERVALO_ENTRE_MENSAGENS)

    except Exception as e:
        print(f"Ocorreu um erro no envio #{contador}: {e}")
        print("Tentando novamente no próximo ciclo...")
        time.sleep(5)
