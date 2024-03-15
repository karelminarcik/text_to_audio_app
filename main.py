from gtts import gTTS
import os
from customtkinter import *
from PIL import Image


# text_to_audio = open('demo.txt', 'r', encoding='utf-8').read().replace('\n', ' ')
# output = gTTS(text_to_audio, lang='cs', slow=False)
# output.save('audio.mp3')

# os.system('start audio.mp3')


app = CTk()
app.geometry("300x300")
app.title('Konvertor textu na řeč')

set_appearance_mode('dark')

# Functions
def translate_text(entry, language, audio_file_name):
    try:
        text_to_audio = entry
        output = gTTS(text_to_audio, lang=language, slow=False)
        output.save(f'{audio_file_name}.mp3')
        os.system(f'start {audio_file_name}.mp3')
    except Exception as e:
        print(f'Nastala chyba {e}')

# Main Label
main_label = CTkLabel(app, text='Konvertor', font=("Arial", 20))
main_label.grid(row=0, column=1, pady=10)

# Language section
language_label = CTkLabel(app, text='Jazyk')
language_label.grid(row=1, column=0, pady=10)

combobox = CTkComboBox(app,state='readonly', width=150, values=['en', 'cs'], fg_color='#0093E9', dropdown_fg_color='#0093E9')
combobox.grid(row=1, column=1)

# Text section

text_label = CTkLabel(app, text='Text')
text_label.grid(row=2, column=0,pady=10)

text_entry = CTkTextbox(app,  width=150, height=70, fg_color='#0093E9')
text_entry.grid(row=2, column=1)

# Audio file section
audio_label = CTkLabel(app, text='Název souboru: ')
audio_label.grid(row=3, column=0,pady=10, padx=5)

audio_entry = CTkEntry(app, width=150, fg_color='#0093E9')
audio_entry.grid(row=3, column=1)

# Button section
button_img = Image.open("google.png")
translate_button = CTkButton(app, text='Přeložit', corner_radius=32,fg_color='transparent',hover_color='#0093E9',border_color='#0093E9', border_width=2,image=CTkImage(dark_image=button_img, light_image=button_img), command=lambda:translate_text(text_entry.get('0.0', 'end'), combobox.get(), audio_entry.get() ))
translate_button.grid(row=4, column=1, pady=10)

app.mainloop()