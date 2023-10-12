#usuario tem 3 tentativas para acessar sua rede social, a senha correta é "Proz@2022"


senhacorreta= "Proz@2022"
x=0
while x <4:
  senha= input("Digite sua senha:")
  x=x+1

  if senha == senhacorreta:
    print("Senha correta, acesso concedido")
  else:
    print("Digite novamente")
