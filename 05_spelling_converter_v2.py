import easygui

while True:
    word = easygui.enterbox('Enter a word:')
    if word is None:
        break
    elif 'our' in word:
        word = word.replace('our', 'or')
        easygui.msgbox(f'US spelling: {word}')
    elif 'ise' in word or 'yse' in word:
        word = word.replace('s', 'z')
        easygui.msgbox(f'US spelling: {word}')
    else:
        easygui.msgbox('No change in spelling')

    continue_or_exit = easygui.buttonbox('Do you want to convert another word?', choices=['Continue', 'Exit'])
    if continue_or_exit == 'Exit':
        break
easygui.msgbox("Thanks, Goodbye!")
