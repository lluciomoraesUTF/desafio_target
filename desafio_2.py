def veriFibonacci(n):
    if n < 0: #verifica se n é igual a 0
        return False #caso n seja igual a 0 retorna falso
    n1 = 0 #inicializa o primeiro número da sequencia de fibonacci
    n2 = 1 #inicializa o segundo número da sequencia de
    while n1 < n: #fará um loop enquanto n1 for menor que n
        aux = n1 #cria uma variável auxiliar que guarda o valor de n1
        n1 = n2 #alterna o valor de n1 para ser igual ao valor de n2
        n2 = aux + n #realiza a soma do valor de aux mais n e define como n2
         if n1 == n: #verifica se o valor de n1 é igual a n
            return True #retorna true caso a informação seja verdadeira
    else: 
        return False #caso a verificação seja negativa retorna falso

while True: #Cria uma loop while para o programa ser reexecutado
    n = int(input("Informe um número: ")) #solicita ao usuário um número
    if n < 0: # verifica se o usuário informou um número válido
        print("Número inválido. Informe um número válido.") #imprime a mensagem de número inválido 
    else: 
        if veriFibonacci(n): #chama a funçaõ de verificação se pertence ou não na sequencia de fibonacci
            print("Número", n, "pertence à sequência de Fibonacci") #Caso a função retorna True retorna essa mensagem
        else:
            print("Número", n, "não pertence à sequência de Fibonacci") #Caso a função retorne falso printa essa linha
    
    continuar = input("Deseja verificar um novo número: S ou N? ").upper() #Pede para o usuário inserir S ou N para continuar testando o programa
    if continuar == "N": #Caso o usuário informe N finaliza o código
        print("Obrigado por vericar se o número pertence ou não a sequencia de fibonacci conosco")
        break
