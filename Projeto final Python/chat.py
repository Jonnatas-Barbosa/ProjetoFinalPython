from unittest import case
import webbrowser


nome = ''
curso = ''
periodo = ''
opcao = ''

print("Olá eu sou o seu assistente estudantil virtual, FADBA ON")
nome = input("Qual é o seu nome? ")

print("Oi ", nome, "como vai você? espero que bem.\nAgora ", nome, "a qual curso vc pertence?")
curso = input()

if (curso == "GTI" or curso == "Gestão da Tecnologia da Informação"):
    print("Oh temos um TI na área")
    periodo = input("Qual periodo? ")

    if (periodo == "3"):
        print("Ok ", nome, "no que eu posso te ajudar?")

        print("1 - Quais são as atv da semana\n",
              "2 - Quando serão as proximas provas?\n")
        opcao = input()
        if (opcao == 1):
          webbrowser.open_new('https://pt.duolingo.com/')
 