#importando bibliotecas
import pyautogui
import openpyxl
import pyperclip

#abrir a planilha
workbook = openpyxl.load_workbook(r'C:\Users\mtsfs\Documents\Programação\Estudos-Python\Cadastro de Produtos')
sheet_produtos = workbook['produtos']
for linha in sheet_produtos.iter_rows(min_row=2,max_row=501):
    produto = linha[0].value
    fornecedor = linha[1].value
    categoria = linha[2].value
    quantidade = linha[3].value
    valor_unitario = linha[4].value
    notificar_venda = linha[5].value

    # colar dados campo produto
    pyautogui.click(1343,1397,duration=1)
    pyautogui.write(produto)

    # colar dados campo fornecedor
    pyautogui.click(1582,1398,duration=1)
    pyautogui.write(fornecedor)

    # colar dados campo categoria
    pyautogui.click(1362,1479,duration=1)
    pyperclip.copy(categoria)
    pyautogui.hotkey('ctrl','v')

    # colar dados campo valor unitário
    pyautogui.click(1552,1474,duration=1)
    pyperclip.copy(valor_unitario)
    pyautogui.hotkey('ctrl','v')

    # se notificar venda for igual a sim, marcar sim
    if notificar_venda == "Sim":
        pyautogui.click(1304,1553, duration=1)

    # se notificar venda for igual a não, marcar não
    elif notificar_venda == "Não":
        pyautogui.click(1390,1552, duration=1)

    # clicar em registrar produto
    pyautogui.click(1330,1606, duration=1)

    # clicar em ok, na mensagem de cadastro com sucesso
    pyautogui.click(1713,1252,duration=1)