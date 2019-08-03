from tkinter.filedialog import *
from StaticAnalysis import *
from BarChart import showBarChart
import matplotlib.pyplot as plt

def open_file():
    of = askopenfilename()
    file = open(of, "r")
    text1.delete(1.0,END)
    text1.insert(END, file.read())
    file.close()

def save_file():
    sf = asksaveasfilename()
    final_text = text2.get(1.0, END)
    file = open(sf, "w")
    file.write(final_text)
    file.close()

def exit_file():
    sys.exit()
#Алфавіт
def staticAnalysisAlp():
    final_text = text1.get(1.0, END)
    a = useAlp(final_text)
    showBarChart(a,"Гістограма частоти повторень одного символу(у алфавітному порядку)")

def staticAnalysisAlpS():
    final_text = text1.get(1.0, END)
    a = useAlp(final_text)
    a = dictSorted(a)
    showBarChart(a, "Гістограма частоти повторень одного символу(у порядку спадання) ")
#Біграми
def staticAnalysisB():
    final_text = text1.get(1.0, END)
    a = nGram(final_text, 2)
    a = dictSorted(a, False)
    showBarChart(a, "Гістограма 15 - ти найчастіше повторюваних біграм(у алфавітному порядку) ", 15)

def staticAnalysisBS():
    final_text = text1.get(1.0, END)
    a = nGram(final_text, 2)
    a = dictSorted(a, True)
    showBarChart(a, "Гістограма 15 - ти найчастіше повторюваних біграм(у порядку спадання)", 15)
#Триграми
def staticAnalysisT():
    final_text = text1.get(1.0, END)
    a = nGram(final_text, 3)
    a = dictSorted(a, False)
    showBarChart(a, "Гістограма 15 - ти найчастіше повторюваних триграм(у алфавітному порядку)", 15)

def staticAnalysisTS():
    final_text = text1.get(1.0, END)
    a = nGram(final_text, 3)
    a = dictSorted(a, True)
    showBarChart(a, "Гістограма 15 - ти найчастіше повторюваних триграм(у порядку спадання)", 15)
#4 - грами
def staticAnalysisF():
    final_text = text1.get(1.0, END)
    a = nGram(final_text, 4)
    a = dictSorted(a, False)
    showBarChart(a, "Гістограма 15 - ти найчастіше повторюваних 4-грам(у алфавітному порядку)", 15)

def staticAnalysisFS():
    final_text = text1.get(1.0, END)
    a = nGram(final_text, 4)
    a = dictSorted(a, True)
    showBarChart(a, "Гістограма 15 - ти найчастіше повторюваних 4-грам(у порядку спадання)", 15)

def cesarEncrypt(text, step):
    ALP = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ .,;-'")
    text2 = ''
    for i in range(len(text)):
        if (text[i]!="\n"):
            temp = text[i]
            a = ALP.index(temp)
            a = a+step
            if(a>=len(ALP)):
                a -=32
                text2 += ALP[a]
            else:
                text2 += ALP[a]
        else:
            text2 += text[i]
    return text2

def start_cesar():
    closeTool()
    btn1.grid(row=0, column=0, pady=5)
    btn2.grid(row=0, column=1, pady=5)
    btnClose.grid(row=0, column=2)
    scale1.grid(row=1, column=0, columnspan=3)

def cesar(event):
    final_text = text1.get(1.0, END)
    text = cesarEncrypt(final_text, scale1.get())
    text2.delete(1.0, END)
    text2.insert(END, text)


def cesarDecrypt(event):
    ALP = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ '-,.;")
    final_text = text1.get(1.0, END)
    a = useAlp(final_text)
    b = dictSorted(a)
    s = b.keys()
    tmp = list(s)
    tmp2 = str(tmp[0])
    index1 = ALP.index(tmp2)
    index2 = ALP.index(" ")
    index3 = index2 - index1
    text2.delete(1.0, END)
    text2.insert(END, cesarEncrypt(final_text, index3))

def cesarClose(event):
    closeTool()

def vigenereEncrypt(text, key = "SERGIY"):
    ALP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '-,.;"
    box = {}
    for i in range(len(ALP)):
        tep = ALP[i::]
        if (len(tep) == len(ALP)):
            box[ALP[i]] = tep
        else:
            index = len(ALP) - len(tep)
            for j in range(index):
                tep += ALP[j]
            box[ALP[i]] = tep

    index = len(text) // len(key)
    textKey = key * index
    if (len(text) != len(textKey)):
        tmp = len(text) - len(textKey)
        textKey += key[:tmp]

    encrypt = ""

    for i in range(len(text)):
        if(text[i]!="\n"):
            temp = box[textKey[i]]
            temp2 = ALP.index(text[i])
            encrypt += temp[temp2]
        else:
            encrypt += "\n"
    return encrypt

def vigenere_Decrypt(text, key = "SERGIY"):
    ALP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '-,.;"
    box = {}
    for i in range(len(ALP)):
        tep = ALP[i::]
        if (len(tep) == len(ALP)):
            box[ALP[i]] = tep
        else:
            index = len(ALP) - len(tep)
            for j in range(index):
                tep += ALP[j]
            box[ALP[i]] = tep

    index = len(text) // len(key)
    textKey = key * index
    if (len(text) != len(textKey)):
        tmp = len(text) - len(textKey)
        textKey += key[:tmp]

    encrypt = text1.get(1.0, END)
    decrypt = ""
    for i in range(len(text)):
        if (text[i] != "\n"):
            temp = box[textKey[i]]
            temp2 = temp.index(encrypt[i])
            decrypt += ALP[temp2]
        else:
            decrypt += "\n"
    return decrypt

def start_vigenere():
    closeTool()
    label1.grid(row=0, column=0,padx=5, pady=5)
    entry.grid(row=0, column=1, padx=5, pady=5)
    btn4.grid(row=1, column=0, padx=5, pady=5)
    btn5.grid(row=1, column=1,padx=5, pady=5)
    btnClose.grid(row=1, column=3, padx=5, pady=5)

def vigenere(event):
    final_text = text1.get(1.0, END)
    text = vigenereEncrypt(final_text, entry.get())
    text2.delete(1.0, END)
    text2.insert(END, text)

def vigenereDecrypt(event):
    final_text = text1.get(1.0, END)
    text = vigenere_Decrypt(final_text, entry.get())
    text2.delete(1.0, END)
    text2.insert(END, text)

def start_EasyR_eplacement():

    final_text = text1.get(1.0, END)
    final_text = final_text.replace("-", " ")

    ALP = {"G": "t", "O": "i", "K": "o", "C": "n", "V": "h", "T": "e", "E": "p", "J": "r",
            "H": "s", "S": "a", "B": "d", "A": "m", "'": "c", "I": "u", "W": "-", "X": "g", "U": "f",
            ".": "l", "R": "b", "L": "y", "D": "v", "N": "z", "Y": "w", "Q": ":", ";": "."}

    final_text2 = ""
    for i in range(len(final_text)):
        if final_text[i] in ALP:
            final_text2 += ALP[final_text[i]]
        elif (final_text[i] == "\n"):
            final_text2 += "\n"
        elif (final_text[i] == " "):
            final_text2 += " "
        else:
            final_text2 += final_text[i]
    final_text2 = final_text2.upper()
    text2.delete(1.0, END)
    text2.insert(END, final_text2)

def repeatPlot():
    final_text1 = text1.get(1.0, END)
    final_text2 = text2.get(1.0, END)
    x = list(dictSorted(useAlp(final_text1)).values())
    y = list(dictSorted(useAlp(final_text2)).values())
    plt.title("Графік повторення для одного символу(по спаданню) для ВТ та ШТ")
    plt.plot(x, 'k--', label = "Відкритий текст")
    plt.plot(y,  label = "Шифрований текст" )
    plt.legend(loc='upper center', shadow=True)
    plt.show()

def closeTool():
    btn1.grid_forget()
    btn2.grid_forget()
    btnClose.grid_forget()
    btn4.grid_forget()
    btn5.grid_forget()
    entry.grid_forget()
    label1.grid_forget()
    scale1.grid_forget()

root = Tk()
root.title("Cryptography")
root.resizable(False, False)
main_Menu = Menu(root)

root.configure(menu=main_Menu)
first_item = Menu(main_Menu, tearoff=0)
main_Menu.add_cascade(label="Файл", menu=first_item)
first_item.add_command(label="Відкрити", command=open_file)
first_item.add_command(label="Зберегти", command=save_file)
first_item.add_command(label="Вихід", command=exit_file)

second_item = Menu(main_Menu, tearoff=0)
main_Menu.add_cascade(label="Статистичний аналіз", menu=second_item)
second_item.add_command(label="Алфавіт", command=staticAnalysisAlp)
second_item.add_command(label="Алфавіт(у порядку спадання)", command=staticAnalysisAlpS)
second_item.add_separator()
second_item.add_command(label="Біграми(у алфавітному порядку)", command=staticAnalysisB)
second_item.add_command(label="Біграми(у порядку спадання) ", command=staticAnalysisBS)
second_item.add_separator()
second_item.add_command(label="Триграми(у алфавітному порядку)", command=staticAnalysisT)
second_item.add_command(label="Триграми(у порядку спадання) ", command=staticAnalysisTS)
second_item.add_separator()
second_item.add_command(label="4 -грами(у алфавітному порядку)", command=staticAnalysisF)
second_item.add_command(label="4 -грами(у порядку спадання) ", command=staticAnalysisFS)
second_item.add_separator()
second_item.add_command(label="Графік повторення для одного символу(по спаданню) для ВТ та ШТ", command=repeatPlot)

code_item = Menu(main_Menu, tearoff=0)
main_Menu.add_cascade(label="Шифри", menu=code_item)
code_item.add_command(label="Цезар", command=start_cesar)
code_item.add_command(label="Віженер", command=start_vigenere)
code_item.add_command(label="Проста заміна", command=start_EasyR_eplacement)

frame1 = Frame(root)
frame1.grid(row=0, column=0)
label1 = Label(frame1, text="Вхідний текст")
label1.pack(side=TOP, fill=Y)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=Y)
text1 = Text(frame1, wrap=WORD, yscrollcommand=scrollbar.set)
text1.pack()
scrollbar.config(command=text1.yview)

frame2 = Frame(root)
frame2.grid(row=0, column=1)
label2 = Label(frame2, text="Вихідний текст")
label2.pack(side=TOP, fill=Y)
scrollbar1 = Scrollbar(frame2)
scrollbar1.pack(side=RIGHT, fill=Y)
text2 = Text(frame2, wrap=WORD, yscrollcommand=scrollbar1.set)
text2.pack()
scrollbar1.config(command=text2.yview)

frame3 = Frame(root)
frame3.grid(row=1, column=0, columnspan=2)

scale1 = Scale(frame3,orient=HORIZONTAL,length=700,from_=1,to=32,tickinterval=1,resolution=1)
btn1 = Button(frame3, text="Зашифрувати")
btn2 = Button(frame3, text="Розшифрувати")
btnClose = Button(frame3, text="Вихід")

btn1.bind("<Button-1>", cesar)
btn2.bind("<Button-1>", cesarDecrypt)
btnClose.bind("<Button-1>", cesarClose)

label1 = Label(frame3, text = "Введіть ключ")
entry = Entry(frame3)
btn4 = Button(frame3, text="Зашифрувати")
btn5 = Button(frame3, text="Розшифрувати")

btn4.bind("<Button-1>", vigenere)
btn5.bind("<Button-1>", vigenereDecrypt)

root.mainloop()