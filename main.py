import tkinter as tk
from tkinter import messagebox

def validar_cpf():
    cpf_usuario = entrada_cpf.get()

    # Remove caracteres não numéricos
    filtro = ''.join(filter(str.isdigit, cpf_usuario))

    # Verifica se o CPF tem exatamente 11 dígitos
    if len(filtro) != 11:
        messagebox.showerror("Erro", "CPF deve conter 11 números.")
        return

    # Obtém os primeiros 9 dígitos
    nove_digitos = filtro[:9]

    contador_regressivo_1 = 10
    resultado_digito1 = 0

    # Cálculo do primeiro dígito
    for digito in nove_digitos:
        resultado_digito1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1

    digito_1 = (resultado_digito1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    # Cálculo do segundo dígito
    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11
    resultado_digito2 = 0

    for digito in dez_digitos:
        resultado_digito2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1

    digito_2 = (resultado_digito2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    # CPF gerado pelo cálculo
    cpf_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    # Verificação final
    if filtro == cpf_calculo:
        messagebox.showinfo("Sucesso", f'O CPF {cpf_usuario} é VÁLIDO.')
    else:
        messagebox.showerror("Erro", "CPF inválido.")

# CONFIG INTERFACE
janela = tk.Tk()
janela.title("Validador de CPF")
janela.geometry("400x250")
janela.resizable(False, False)


bg_image = tk.PhotoImage(file='image/image-cpf.png')
bg_label = tk.Label(janela, image=bg_image)
bg_label.place(x=-2, y=-2)


tk.Label(janela, text="Digite o CPF:", fg="#000080", font=("Arial", 15)).pack(pady=10)
entrada_cpf = tk.Entry(janela, width=13, font=("Arial", 20))

entrada_cpf.pack(pady=5)

btn_validar = tk.Button(janela, text="Validar CPF", command=validar_cpf, bg="green", fg="white", font=("Arial", 14))
btn_validar.pack(pady=20)

janela.mainloop()
