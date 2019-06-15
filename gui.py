from tkinter import *
from tkinter import messagebox as mb
import pygame

pygame.mixer.init()

player_x_s = 0
player_o_s = 0

def winner_check(num):
    button_1.configure(text='')
    button_2.configure(text='')
    button_3.configure(text='')
    button_4.configure(text='')
    button_5.configure(text='')
    button_6.configure(text='')
    button_7.configure(text='')
    button_8.configure(text='')
    button_9.configure(text='')
    button_1.configure(image=trans)
    button_2.configure(image=trans)
    button_3.configure(image=trans)
    button_4.configure(image=trans)
    button_5.configure(image=trans)
    button_6.configure(image=trans)
    button_7.configure(image=trans)
    button_8.configure(image=trans)
    button_9.configure(image=trans)
    
    if num == 'x':
        global player_o_s
        player_o_s += 1
        if player_o_s == 10:
            mb.showinfo('Won',f'Player With {num.upper()} Wins')
            pygame.mixer.music.load('resources/audio/hit.wav')
            pygame.mixer.music.play()
            rematch()
        else:
            pygame.mixer.music.load('resources/audio/point.wav')
            pygame.mixer.music.play()
            o_marks['image'] = num_list[player_o_s]
            o_res['image'] = win_img
            x_res['image'] = lose_img
            
    elif num == '0':
        global player_x_s
        player_x_s += 1
        if player_x_s == 10:
            mb.showinfo('Won',f'Player With {num.upper()} Wins')
            pygame.mixer.music.load('resources/audio/hit.wav')
            pygame.mixer.music.play()
            rematch()
        else:
            pygame.mixer.music.load('resources/audio/point.wav')
            pygame.mixer.music.play()
            x_marks['image'] = num_list[player_x_s]
            x_res['image'] = win_img
            o_res['image'] = lose_img            
    else:
        pygame.mixer.music.load('resources/audio/point.wav')
        pygame.mixer.music.play()
        x_res['image'] = draw
        o_res['image'] = draw
        

win = Tk()
win.geometry('600x500')
win.resizable(0,0)
win.title('Tic-Tac_Toe')
win.configure(bg='white')

header = PhotoImage(file='resources/sprites/header_label.png')
Label(win, image=header,bg='grey',width=600).pack()

board = PhotoImage(file='resources/sprites/board.png')
Label(win, image=board,bg='white').pack()

counter = 0
def game(button):
    pygame.mixer.music.load('resources/audio/move.wav')
    pygame.mixer.music.play()
    global counter
    counter += 1    
    if button['text'] == '':
        
        if counter%2 == 0:
            button['text'] = '0'
            button['image'] = zero
            turn_label['image'] = turn
            turn_label.place(x=20,y=330)
            
        else:
            button['text'] = 'x'
            button['image'] = ex
            turn_label['image'] = turn
            turn_label.place(x=480,y=330)
            
    # condition 1
    if button_1['text']=='0' and button_2['text']=='0' and button_3['text']=='0':
        winner_check('0')
     # condition 2
    elif button_1['text']=='x' and button_2['text']=='x' and button_3['text']=='x':
        winner_check('x')
  # condition 3
    elif button_4['text']=='0' and button_5['text']=='0' and button_6['text']=='0':
        winner_check('0')
 # condition 4
    elif button_4['text']=='x' and button_5['text']=='x' and button_6['text']=='x':
        winner_check('x')
 # condition 5
    elif button_7['text']=='0' and button_8['text']=='0' and button_9['text']=='0':
        winner_check('0')
 # condition 6
    elif button_7['text']=='x' and button_8['text']=='x' and button_9['text']=='x':
        winner_check('x')
 # condition 7
    elif button_1['text']=='0' and button_4['text']=='0' and button_7['text']=='0':
        winner_check('0')
 # condition 8
    elif button_1['text']=='x' and button_4['text']=='x' and button_7['text']=='x':
        winner_check('x')
 # condition 9
    elif button_2['text']=='0' and button_5['text']=='0' and button_8['text']=='0':
        winner_check('0')
 # condition 10
    elif button_2['text']=='x' and button_5['text']=='x' and button_8['text']=='x':
        winner_check('x')
 # condition 11
    elif button_3['text']=='0' and button_6['text']=='0' and button_9['text']=='0':
        winner_check('0')
 # condition 12
    elif button_3['text']=='x' and button_6['text']=='x' and button_9['text']=='x':
        winner_check('x')
 # condition 13
    elif button_1['text']=='0' and button_5['text']=='0' and button_9['text']=='0':
        winner_check('0')
 # condition 14
    elif button_1['text']=='x' and button_5['text']=='x' and button_9['text']=='x':
        winner_check('x')
 # condition 15
    elif button_7['text']=='0' and button_5['text']=='0' and button_3['text']=='0':
        winner_check('0')
 # condition 16
    elif button_7['text']=='x' and button_5['text']=='x' and button_3['text']=='x':
        winner_check('x')
 # condition 17
    elif button_1['text'] != '' and button_2['text'] != '' and button_3['text'] != '' and button_4['text'] != '' and button_5['text'] != '' and button_6['text'] != '' and button_7['text'] != '' and button_8['text'] != '' and button_9['text'] != ''  :
        winner_check('draw')
        

        
        

zero = PhotoImage(file='resources/sprites/0.png')
ex = PhotoImage(file='resources/sprites/x.png')
trans = PhotoImage(file='resources/sprites/trans.png')




        


button_1 = Button(win,command=lambda: game(button_1),bd=0,bg='white',image=trans)
button_1.place(x=180,y=170)

button_2 = Button(win,command=lambda: game(button_2),bd=0,bg='white',image=trans)
button_2.place(x=260,y=170)

button_3 = Button(win, command=lambda: game(button_3),bd=0,bg='white',image=trans)
button_3.place(x=340,y=170)

button_4 = Button(win,  command=lambda: game(button_4),bd=0,bg='white',image=trans)
button_4.place(x=180,y=250)

button_5 = Button(win, command=lambda: game(button_5),bd=0,bg='white',image=trans)
button_5.place(x=260,y=250)

button_6 = Button(win,  command=lambda: game(button_6),bd=0,bg='white',image=trans)
button_6.place(x=340,y=250)

button_7 = Button(win, command=lambda: game(button_7),bd=0,bg='white',image=trans)
button_7.place(x=180,y=330)

button_8 = Button(win,  command=lambda: game(button_8),bd=0,bg='white',image=trans)
button_8.place(x=252,y=330)

button_9 = Button(win, command=lambda: game(button_9),bd=0,bg='white',image=trans)
button_9.place(x=333,y=330)


win_img = PhotoImage(file='resources/sprites/win.png')
lose_img = PhotoImage(file='resources/sprites/lose.png')
draw = PhotoImage(file='resources/sprites/draw.png')

o_res = Label(win, image=trans,bg='white')
o_res.place(x=10,y=430)
x_res = Label(win, image=trans,bg='white')
x_res.place(x=460,y=430)



num_list = [
        PhotoImage(file='resources/numbers/0.png'),
        PhotoImage(file='resources/numbers/1.png'),
        PhotoImage(file='resources/numbers/2.png'),
        PhotoImage(file='resources/numbers/3.png'),
        PhotoImage(file='resources/numbers/4.png'),
        PhotoImage(file='resources/numbers/5.png'),
        PhotoImage(file='resources/numbers/6.png'),
        PhotoImage(file='resources/numbers/7.png'),
        PhotoImage(file='resources/numbers/8.png'),
        PhotoImage(file='resources/numbers/9.png'),
    ]



player_1 = PhotoImage(file='resources/sprites/player1.png')
player_2 = PhotoImage(file='resources/sprites/player2.png')

turn = PhotoImage(file='resources/sprites/turn.png')
turn_label = Label(win, image=turn,bg='white')
turn_label.place(x=20,y=330)


Label(win, image=player_1,bg='white').place(x=1,y=160)
Label(win, image=player_2,bg='white').place(x=440,y=160)

o_marks = Label(win,image=num_list[0],bg='white')
o_marks.place(x=35,y=220)
x_marks = Label(win,image=num_list[0],bg='white')
x_marks.place(x=495,y=220)

def rematch():
    global player_x_s
    player_x_s = 0
    global player_o_s
    player_o_s = 0
    o_marks['image'] = num_list[0]
    x_marks['image'] = num_list[0]
    o_res['image'] = trans
    x_res['image'] = trans
    button_1.configure(text='')
    button_2.configure(text='')
    button_3.configure(text='')
    button_4.configure(text='')
    button_5.configure(text='')
    button_6.configure(text='')
    button_7.configure(text='')
    button_8.configure(text='')
    button_9.configure(text='')
    button_1.configure(image=trans)
    button_2.configure(image=trans)
    button_3.configure(image=trans)
    button_4.configure(image=trans)
    button_5.configure(image=trans)
    button_6.configure(image=trans)
    button_7.configure(image=trans)
    button_8.configure(image=trans)
    button_9.configure(image=trans)



    

reset = PhotoImage(file='resources/sprites/rematch.png')
Button(win, image=reset,bg='white',bd=0,command=rematch).pack()

win.mainloop()
