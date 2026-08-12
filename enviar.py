import pywhatkit as kit
import time

numero_destino = "+55 19 98370-0403"
quantidade = 5
intervalo = 5

for contador in range(1, quantidade + 1):
    mensagem = f"olá#{contador}"

    try:
        kit.sendwhatmsg_instantly(
            phone_no=numero_destino,
            message=mensagem,
            wait_time=8,
            tab_close=True
        )

        print(f"Enviada: {contador}/{quantidade}")
        time.sleep(intervalo)

    except Exception as e:
        print(f"Erro na mensagem #{contador}: {e}")
        break
