import speech_recognition as sr
import os

def ouvir_microfone():

    microfone = sr.Recognizer()
    assistente_ativo = False  # Inicialmente, o assistente não está ativo

    while True:  # Loop principal
        with sr.Microphone() as source:
            if not assistente_ativo:
                print("Diga 'assistente' para começar: ")

            audio = microfone.listen(source)  # Escuta a entrada de voz

        try:
            frase = microfone.recognize_google(audio, language='pt-BR')

            if "assistente" in frase:  # Verifica a frase de ativação
                assistente_ativo = True
                print("Comandos ativados. Aguardando instruções...")

            if assistente_ativo:
                comando = frase.lower()  # Transforma a frase em minúsculas para facilitar a comparação

                # Executa os comandos baseados nas palavras-chave
                if "navegador" in comando:
                    os.system("start Chrome.exe")
                elif "excel" in comando:
                    os.system("start Excel.exe")
                elif "powerpoint" in comando:
                    os.system("start POWERPNT.exe")
                elif "fechar" in comando:
                    return False  # Encerra a execução do assistente ao mencionar "Fechar"

        except sr.UnknownValueError:
            print('Não entendi')  # Trata o erro se não compreender a fala
            assistente_ativo = False  # Reinicia o assistente se não entender
    return False

ouvir_microfone()  # Chama a função para iniciar o assistente de voz


