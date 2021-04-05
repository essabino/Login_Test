from PySimpleGUI import PySimpleGUI as sg
#layout
sg.theme('Reddit')
layout=[
    [sg.Text('Usuário'),sg.Input(key='usuario',size=(50,1))],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*',size=(50,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
layout2=[
    [sg.Text('Bem-vindo a Dev Aprender!',size=(50,1))],
    [sg.Text('Oportunidade de fazer inovação',size=(50,1))]
]
#Janela
janela=sg.Window('Tela de Login',layout)
#ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario']=='eduardo' and valores['senha']=='123456':
            #print('Bem-vindo a Dev Aprender!')
            janela=sg.Window('Tela Bem Vindo!!!!',layout2)
