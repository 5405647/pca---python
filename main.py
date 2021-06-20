import PySimpleGUI as sg

def janelaPrincipal():
    sg.theme('Dark Green 3')
    layout = [
        [sg.Text('Jogo de Perguntas e Respostas', font=("Unispace", 25))],
        [sg.Text('\nVocê sabia que as chances de contrair a Covid-19 é proporcional ao seu conhecimento sobre ela?\nSerá que você está fazendo todas as medidas de segurança corretamente? É isso que nós vamos ver agora!',
            font=("Arial", 13))],
        [sg.Text('\nInstruções sobre o jogo', font=("Arial", 15, 'underline'))],
        [sg.Text('Será elencado 15 questões sobre os meios de segurança para reduzir as chances de infecção pela Covid-19. Você\ndeve responder se a questão é um fato ou fake onde, após responder, será exibida a informação sobre a resposta correta.',
            font=("Arial", 12))],
        [sg.Text('\nPronto para começar?', font=("Arial", 15))],
        [sg.Button('Sim', size=(10, 1)), sg.Button('Não', size=(10, 1))]

    ]
    window = sg.Window('Falcões Memoráveis', layout, element_justification='c', modal=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Não':
            break
        if event == 'Sim':
            window.close()
            pergunta1()
            break

def pergunta1():
    sg.theme('Dark Green 3')
    layout = [
        [sg.Text('1. Tudo bem compartilhar objetos, tipo o celular, pois o novo coronavírus não se transmite dessa forma.')],
        [sg.Button('Fato'), sg.Button('Fake')]
    ]
    window = sg.Window('Falcões Memoráveis', layout, element_justification='c', font=('Arial', 14), modal=True)

    while True:
        event, values = window.read()
        if event == 'Fato':
            [sg.Popup('Errou! Estudos já comprovaram que o novo coronavírus pode sobreviver em diversos tipos diferentes de objetos e superfícies.',  font=('Arial', 13))]
            window.close()
            pergunta2()
            break
        else:
            [sg.Popup('Acertou! Estudos já comprovaram que o novo coronavírus pode sobreviver em diversos tipos diferentes de objetos e superfícies.',  font=('Arial', 13))]
            window.close()
            pergunta2()
            break

def pergunta2():
    sg.theme('Dark Green 3')
    layout = [
        [sg.Text('2. Não preciso me preocupar em higienizar as compras do mercado, afinal, eu mesmo peguei da prateleira com as mãos limpas.')],
        [sg.Button('Fato'), sg.Button('Fake')]
    ]
    window = sg.Window('Falcões Memoráveis', layout, element_justification='c', font=('Arial', 14), modal=True)


    while True:
        event, values = window.read()
        if event == 'Fato':
            [sg.Popup('Errou! Apesar de recentemente esse tipo de contaminação ter se revelado menos comum, higiene nunca é demais.',  font=('Arial', 13))]
            window.close()
            pergunta3()
            break
        else:
            [sg.Popup('Acertou! Apesar de recentemente esse tipo de contaminação ter se revelado menos comum, higiene nunca é demais.',  font=('Arial', 13))]
            window.close()
            pergunta3()
            break

def pergunta3():
    sg.theme('Dark Green 3')
    layout = [
        [sg.Text('3. Em caso de sintomas gripais e estando em locais públicos, o mais indicado a se fazer é cobrir a boca com o antebraço ou o cotovelo ao espirrar e/ou tossir.')],
        [sg.Button('Fato'), sg.Button('Fake')]
    ]
    window = sg.Window('Falcões Memoráveis', layout, element_justification='c', font=('Arial', 14), modal=True)


    while True:
        event, values = window.read()
        if event == 'Fato':
            [sg.Popup('Errou! Fora de cada devemos usar máscara o tempo todo (exceto na hora de comer e beber) e respeitar o distanciamento. Além disso, com qualquer sintoma de gripe ou resfriado, o mais indicado é ficar em casa!',  font=('Arial', 13))]
            window.close()
            pergunta4()
            break
        else:
            [sg.Popup('Acertou! Fora de cada devemos usar máscara o tempo todo (exceto na hora de comer e beber) e respeitar o distanciamento. Além disso, com qualquer sintoma de gripe ou resfriado, o mais indicado é ficar em casa!',  font=('Arial', 13))]
            window.close()
            pergunta4()
            break

def pergunta4():
    sg.theme('Dark Green 3')
    layout = [
        [sg.Text('4. Se me sinto bem e tomo todos os cuidados, tudo bem abraçar e beijar as pessoas com quem moro.')],
        [sg.Button('Fato'), sg.Button('Fake')]
    ]
    window = sg.Window('Falcões Memoráveis', layout, element_justification='c', font=('Arial', 14), modal=True)


    while True:
        event, values = window.read()
        if event == 'Fato':
            [sg.Popup('Acertou! Porém, baixar a guarda em casa é possível somente se todos estiverem respeitando as orientações sanitária. Caso contrário, mesmo se cuidado, você pode estar em risco dentro da sua própria casa.',  font=('Arial', 13))]
            window.close()
            pergunta5()
            break
        else:
            [sg.Popup('Errou! Baixar a guarda em casa é possível somente se todos estiverem respeitando as orientações sanitária. Caso contrário, mesmo se cuidado, você pode estar em risco dentro da sua própria casa.',  font=('Arial', 13))]
            window.close()
            pergunta5()
            break

def pergunta5():
    sg.theme('Dark Green 3')
    layout = [
        [sg.Text('5. Os sintomas mais comuns da Covid-19 são: febre, tosse, cansaço, dor de cabeça e alteração do olfato.')],
        [sg.Button('Fato'), sg.Button('Fake')]
    ]
    window = sg.Window('Falcões Memoráveis', layout, element_justification='c', font=('Arial', 14), modal=True)


    while True:
        event, values = window.read()
        if event == 'Fato':
            [sg.Popup('Acertou! Mas fique atento(a): os sintomas não ocorrem no mesmo instante da infecção.',  font=('Arial', 13))]
            window.close()
            pergunta6()
            break
        else:
            [sg.Popup('Errou! Esses são os sintomas mais comuns, mas fique atento(a): os sintomas não ocorrem no mesmo instante da infecção.',  font=('Arial', 13))]
            window.close()
            pergunta6()
            break

def pergunta6():
    sg.theme('Dark Green 3')
    layout = [
        [sg.Text('6. É possível estar com a Covid-19 por até 14 dias antes de apresentar os sintomas.')],
        [sg.Button('Fato'), sg.Button('Fake')]
    ]
    window = sg.Window('Falcões Memoráveis', layout, element_justification='c', font=('Arial', 14), modal=True)


    while True:
        event, values = window.read()
        if event == 'Fato':
            [sg.Popup('Acertou! O período de incubação varia entre 2 e 14 dias. E a média é de 5 dias.',  font=('Arial', 13))]
            window.close()
            pergunta7()
            break
        else:
            [sg.Popup('Errou! O período de incubação varia entre 2 e 14 dias. E a média é de 5 dias.',  font=('Arial', 13))]
            window.close()
            pergunta7()
            break

def pergunta7():
    sg.theme('Dark Green 3')
    layout = [
        [sg.Text('7. Com mais de um ano de pandemia, já há medicamentos específicos e eficazes para o tratamento da Covid-19.')],
        [sg.Button('Fato'), sg.Button('Fake')]
    ]
    window = sg.Window('Falcões Memoráveis', layout, element_justification='c', font=('Arial', 14), modal=True)


    while True:
        event, values = window.read()
        if event == 'Fato':
            [sg.Popup('Errou! Ainda não há medicamento ideal para o combate ao vírus - em qualquer fase da doença - e automedicar-se é bastante perigoso, podendo levar à morte.',  font=('Arial', 13))]
            window.close()
            pergunta8()
            break
        else:
            [sg.Popup('Acertou! Ainda não há medicamento ideal para o combate ao vírus - em qualquer fase da doença - e automedicar-se é bastante perigoso, podendo levar à morte.',  font=('Arial', 13))]
            window.close()
            pergunta8()
            break

def pergunta8():
    sg.theme('Dark Green 3')
    layout = [
        [sg.Text('8. Mesmo uma pessoa sem sintomas da COVID-19 pode contaminar outras.')],
        [sg.Button('Fato'), sg.Button('Fake')]
    ]
    window = sg.Window('Falcões Memoráveis', layout, element_justification='c', font=('Arial', 14), modal=True)


    while True:
        event, values = window.read()
        if event == 'Fato':
            [sg.Popup('Acertou! É importante lembrar que existe a possibilidade de uma pessoa transportar e transmitir o vírus por gotículas respiratórias e pelas mãoes contaminadas, sem estar apresentando qualquer sintoma da COVID-19.',  font=('Arial', 13))]
            window.close()
            pergunta9()
            break
        else:
            [sg.Popup('Errou! É importante lembrar que existe a possibilidade de uma pessoa transportar e transmitir o vírus por gotículas respiratórias e pelas mãoes contaminadas, sem estar apresentando qualquer sintoma da COVID-19.',  font=('Arial', 13))]
            window.close()
            pergunta9()
            break

def pergunta9():
    sg.theme('Dark Green 3')
    layout = [
        [sg.Text('9. Usando máscara não é possível ser infectado.')],
        [sg.Button('Fato'), sg.Button('Fake')]
    ]
    window = sg.Window('Falcões Memoráveis', layout, element_justification='c', font=('Arial', 14), modal=True)


    while True:
        event, values = window.read()
        if event == 'Fato':
            [sg.Popup('Errou! O uso da máscara é fundamental, mas precisa estar em conjunção com aqueles outros cuidados: distanciamento social e higienização constante das mãos.',  font=('Arial', 13))]
            window.close()
            pergunta10()
            break
        else:
            [sg.Popup('Acertou! O uso da máscara é fundamental, mas precisa estar em conjunção com aqueles outros cuidados: distanciamento social e higienização constante das mãos.',  font=('Arial', 13))]
            window.close()
            pergunta10()
            break

def pergunta10():
    sg.theme('Dark Green 3')
    layout = [
        [sg.Text('10. A COVID-19 é mais perigosa para indivíduos acima dos 60 anos ou debilitados, portadores de doenças crônicas e crianças.')],
        [sg.Button('Fato'), sg.Button('Fake')]
    ]
    window = sg.Window('Falcões Memoráveis', layout, element_justification='c', font=('Arial', 14), modal=True)

    while True:
        event, values = window.read()
        if event == 'Fato':
            [sg.Popup('Errou! Crianças não estão no grupo de risco, mas nada de relaxar os cuidados. Mesmo sendo mais raros, muitos casos graves em crianças têm sido relatados.',  font=('Arial', 13))]
            window.close()
            pergunta11()
            break
        else:
            [sg.Popup('Acertou! Crianças não estão no grupo de risco, mas nada de relaxar os cuidados. Mesmo sendo mais raros, muitos casos graves em crianças têm sido relatados.',  font=('Arial', 13))]
            window.close()
            pergunta11()
            break

def pergunta11():
    sg.theme('Dark Green 3')
    layout = [
        [sg.Text('11. Enquanto não temos vacina suficiente para toda a população, a imunização de rebanho se mostra uma boa estratégia.')],
        [sg.Button('Fato'), sg.Button('Fake')]
    ]
    window = sg.Window('Falcões Memoráveis', layout, element_justification='c', font=('Arial', 14), modal=True)

    while True:
        event, values = window.read()
        if event == 'Fato':
            [sg.Popup('Errou! Além de colocar em risco boa parte da população, apostar na imunidade de rebanho e deixar a epidemia avançar favoreceria o desenvolvimento de novas cepas do vírus que podem ser mais agressivas ou resistentes à vacina.',  font=('Arial', 13))]
            window.close()
            pergunta12()
            break
        else:
            [sg.Popup('Acertou! Além de colocar em risco boa parte da população, apostar na imunidade de rebanho e deixar a epidemia avançar favoreceria o desenvolvimento de novas cepas do vírus que podem ser mais agressivas ou resistentes à vacina.',  font=('Arial', 13))]
            window.close()
            pergunta12()
            break

def pergunta12():
    sg.theme('Dark Green 3')
    layout = [
        [sg.Text('12. Devo procurar hospital quando estiver espirrando.')],
        [sg.Button('Fato'), sg.Button('Fake')]
    ]
    window = sg.Window('Falcões Memoráveis', layout, element_justification='c', font=('Arial', 14), modal=True)


    while True:
        event, values = window.read()
        if event == 'Fato':
            [sg.Popup('Errou! Estar espirrando não é condição suficiente para se deslocar até o hospital. Procure atendimento médico se surgir febre ou apresentar sinais de fadiga ou desconforto para respirar.',  font=('Arial', 13))]
            window.close()
            pergunta13()
            break
        else:
            [sg.Popup('Acertou! Estar espirrando não é condição suficiente para se deslocar até o hospital. Procure atendimento médico se surgir febre ou apresentar sinais de fadiga ou desconforto para respirar.',  font=('Arial', 13))]
            window.close()
            pergunta13()
            break

def pergunta13():
    sg.theme('Dark Green 3')
    layout = [
        [sg.Text('13. É melhor sempre evitar ir ao hospital, mesmo que para controlar doenças crônicas, e diminuir as chances de exposição ao vírus.')],
        [sg.Button('Fato'), sg.Button('Fake')]
    ]
    window = sg.Window('Falcões Memoráveis', layout, element_justification='c', font=('Arial', 14), modal=True)

    while True:
        event, values = window.read()
        if event == 'Fato':
            [sg.Popup('Errou! Várias situações, como dor torácica, falta de ar, palpitações, desmaio, perda de força, convulsão, dor abdominal intensa e hemorragias, exigem atendimento médico imediato e não procurá-lo pode ter graves consequências. Além disso, todos os cuidados no controle de doenças crônicas, como diabetes, hipertensão, insuficiência cardíaca, doenças reumatológicas, oncológicas e pulmonares, devem ser mantidos, tá?',  font=('Arial', 13))]
            window.close()
            pergunta14()
            break
        else:
            [sg.Popup('Acertou! Várias situações, como dor torácica, falta de ar, palpitações, desmaio, perda de força, convulsão, dor abdominal intensa e hemorragias, exigem atendimento médico imediato e não procurá-lo pode ter graves consequências. Além disso, todos os cuidados no controle de doenças crônicas, como diabetes, hipertensão, insuficiência cardíaca, doenças reumatológicas, oncológicas e pulmonares, devem ser mantidos, tá?',  font=('Arial', 13))]
            window.close()
            pergunta14()
            break

def pergunta14():
    sg.theme('Dark Green 3')
    layout = [
        [sg.Text('14. A vacina da gripe não protege contra a COVID-19.')],
        [sg.Button('Fato'), sg.Button('Fake')]
    ]
    window = sg.Window('Falcões Memoráveis', layout, element_justification='c', font=('Arial', 14), modal=True)


    while True:
        event, values = window.read()
        if event == 'Fato':
            [sg.Popup('Acertou! Porém é importante se vacinar para diminuir o volume de pessoas procurando atendimento médico e favorecer o diagnóstico mais rápido da COVID-19.',  font=('Arial', 13))]
            window.close()
            pergunta15()
            break
        else:
            [sg.Popup('Errou! Porém é importante se vacinar para diminuir o volume de pessoas procurando atendimento médico e favorecer o diagnóstico mais rápido da COVID-19.',  font=('Arial', 13))]
            window.close()
            pergunta15()
            break

def pergunta15():
    sg.theme('Dark Green 3')
    layout = [
        [sg.Text('15. Qualquer sabão serve para proteger as mãos do contato com o vírus.')],
        [sg.Button('Fato'), sg.Button('Fake')]
    ]
    window = sg.Window('Falcões Memoráveis', layout, element_justification='c', font=('Arial', 14), modal=True)


    while True:
        event, values = window.read()
        if event == 'Fato':
            [sg.Popup('Acertou! A boa e velha prática nunca sai de moda.',  font=('Arial', 13))]
            window.close()
            conclusao()
            break
        else:
            [sg.Popup('Errou! A boa e velha prática nunca sai de moda.',  font=('Arial', 13))]
            window.close()
            conclusao()
            break

def conclusao():
    sg.theme('Dark Green 3')     
    
    layout = [
        [sg.Text('Fim de Jogo!', font=("Unispace", 25, 'underline'))],
        [sg.Text('''Esperamos que com esse jogo você consiga ter absorvido o 
máximo de informações a respeito dessa pandemia que assola
o mundo e, com isso, adote todas as medidas necessárias para
se evitar ser contaminado pela COVID-19.''', font=("Arial", 14))],
        [sg.Text('Obrigado por participar do nosso jogo!', font=("Arial", 14))],
        [sg.Button('Sair', size=(10, 1))]

    ]
    window = sg.Window('Falcões Memoráveis', layout, element_justification='c', modal=True)

    while True:
        window, event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Sair':
            break

janelaPrincipal()
