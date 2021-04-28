import PySimpleGUI as sg
from pytube import YouTube

# wygląd okienka heh

sg.theme("DarkRed1")
layout = [[sg.Text("Wstaw link z youtube")],
                 [sg.InputText()],
                 [sg.Submit(), sg.Cancel()]]

window = sg.Window("Pobieranie filmiku z youtube", layout)

event, values = window.read()
window.close()

# Okienko 2

layout = [[sg.Text("Wstaw lokalizację pliku")],
                 [sg.InputText()],
                 [sg.Submit(), sg.Cancel()]]

window1 = sg.Window("Pobieranie filmiku z youtube", layout)

ewent, walues = window1.read()
window.close()

# pop up końcowy i dodatkowe przekształcenia

lokalizacja = walues[0]
text_input = values[0]
sg.popup("Pobieranie, program zrobiony przez BrzózkaTV")
lokalizacja.encode("unicode_escape")

# skrypt pobierania

yt = YouTube(text_input)
moje_video = yt.streams.first()
moje_video.download(lokalizacja)

# program zrobiony przez: (made by:) bartzszkoly@gmail.com (BrzózkaTV#5405)
# smutny taki, mało kolorowy ten program coś :-)