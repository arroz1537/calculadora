def jogar():
    print (" CALCULADORA SIMPLES ")
    a = int(input ("escolha o primeiro numero"))
    b = int(input ("escolha o segundo numero"))
    escolha = int(input("Digite 1 para somar\nDigite 2 para multiplicar\nDigite 3 para subtrarir\nDigite 4 para dividir\n"))
    if escolha == 1:
        print(a + b)
    if escolha == 2:
        print(a * b)
    if escolha == 3:
        print(a - b)    
    if escolha == 4:
        print(a / b)
def main():
    while True:  # Loop que continuará até o jogador decidir sair
        jogar()
        jogar_novamente = input("Deseja jogar novamente? (sim/não): ").lower()
        
        if jogar_novamente != 'sim':
            print("Obrigado por usar a calculadora! Até a próxima.")
            break  # Sai do loop e finaliza o jogo

# Inicia o jogo
main()