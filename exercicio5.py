
idade  =  int ( input ( "digite a sua idade:" ))
if  15 < idade <  70 :
    peso  =  int ( input ( "digite seu peso em kg:" ))
    if  peso > 49 :
        tempodesono =  int ( input ( "Quanto tempo de sono você teve nas ultimas 24 horas:" ))
        if  tempodesono > 6 :
            
            print ( "Você esta apto a fazer a doação" )
            escolha  =  int ( input ( "Voce quer se cadastar? 1 para sim 0 para não:" ))
            if  escolha > 0 :
                Nome  =  input ( "Digite seu nome completo:" )
                Cpf  =  int ( input ( "Digite seu Cpf:" ))
                Senha  =  int ( input ( "Digite sua senha:"))   
                print ( "esses sao os dados do paciente:" , Nome , "" , cpf , "" , senha)
            else :
                print ( "obrigado por doar sangue")
        else :
            print ( "você não dormiu o suficiente para fazer a doação de sangue")
    else :
        print ( "Seu peso está abaixo do necessario para poder doar " )
else :
     print ( "você nao tem idade pra poder doar sangue" )