from tkinter import *
import tkinter as tk
from tkinter import messagebox
from string import ascii_letters
import random
from PIL import Image, ImageTk
import customtkinter as ctk
#from first_frame import first_frame


root= ctk.CTk()
bgimg =tk.PhotoImage(file='hang.img1.png')
limg = Label(root, i = bgimg)
limg.pack()

#bg =ImageTk.PhotoImage(file = 'hang.img1.png')
#Canvas1 = Canvas(root, width =400, height=300 )
#Canvas1.pack(fill ='both', expand =True )

#Canvas1.create_image(0,0 , image = bg, anchor = 'nw')



ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')
root.title('HANGMANN,Guess D Word')

#random generated words

word_list= ['village','magazine','heart', 'statement', 'activity', 'riddle', 'shatter','callous', 'sunshine', 'eternal',
             'variable' ,'portable', 'dimple', 'stranger', 'baptism', 'assume', 'repetition', 'perforate', 'aghast', 'stranded','murder',
			 'slavery','anaconda','deliberate', 'addiction', 'ceremony','stumble', 'diameter','detect', 'punish','january',"border",'blood',
			 'document', 'optimism', 'hangman', 'computer', 'trademark', 'develop', 'hybrid', 'vampire', 'humid', 'terminal',
			 'virus', 'celebrate', 'confusion', 'knife', 'depress',"image",'violence', 'encrypt', 'trial', 'family', 'pirate']
    
#images for hangman

photos = [PhotoImage(file="hang0.png"), PhotoImage(file="hang1.png"), PhotoImage(file="hang2.png"),
PhotoImage(file="hang3.png"), PhotoImage(file="hang4.png"), PhotoImage(file="hang5.png"),
PhotoImage(file="hang6.png"), PhotoImage(file="hang7.png"), PhotoImage(file="hang8.png"),
PhotoImage(file="hang9.png"), PhotoImage(file="hang10.png"), PhotoImage(file="hang11.png")]




#function to select random words

def newGame():
    global spaced_words
    global no_guesses
    no_guesses =0
    
    the_word=random.choice(word_list)
    spaced_words = " ".join(the_word)
    label_wrd.set(' '.join("_"*len(the_word)))


# function to playgame

def guess(letter):
	global no_guesses
	if no_guesses<11:	
		text = list(spaced_words)
		guessed = list(label_wrd.get())
		if spaced_words.count(letter)>0:
			for i in range(len(text)):
				if text[i]==letter:
					guessed[i]=letter
				label_wrd.set("".join(guessed))
				if label_wrd.get()==spaced_words:
					messagebox.askyesno("You Win This Game!",'Do you want to play again')
					lttr_butt.config(DISABLED)
					
                    

		else:
			no_guesses += 1
			imgLabel.config(image=photos[no_guesses])
			if no_guesses==11:
					messagebox.showwarning("Game Over",'You Lose')
					


def first_frame():
    global frame1, frame_pic1

    frame_pic1 = ctk.CTkFrame(root)
    frame_pic1.pack(expand = True, fill = "both")
    img1= ctk.CTkImage(Image.open("hang.img1.png"), size= (600, 600))
    img_label = ctk.CTkLabel(frame_pic1, text= "k", image=img1) 
    img_label.pack()
    
    frame1 = ctk.CTkFrame(frame_pic1 , fg_color = '#333333')
    frame1.place(relx= 0.5, rely=0.5,anchor= ctk.CENTER)


    label1 = ctk.CTkLabel(frame1, text = 'HANGMANN\nGUESS THE WORD',text_color= 'black',fg_color= '#55556B' ,font = ('montserrat',22, 'bold'))
    label1.grid(row= 0, column = 0 , padx= 100, pady =(180,50) )

    enter_gamebutt = ctk.CTkButton(frame1, text = 'Play Game',text_color='#FEFEFE',fg_color = '#55556B' 
                                  ,font = ('montserrat',15, 'bold'),command= newGame)
    enter_gamebutt.grid(row = 1 , column = 0)




if __name__ == '__main__':
   
	
    #root.resizable(0,0)

        

    frame2 = ctk.CTkFrame(root, fg_color =  '#000000')
   # frame2.grid(row = 0, column = 0)
    frame2.place(relx= 0.15, rely=0.15,anchor= ctk.CENTER)


    #to display hangman images

    imgLabel=Label(frame2,bg='#48483D')
    imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)

    #to display word to be guessed

    label_wrd = StringVar()
    Label(frame2, bg='#CACAFF',textvariable  =label_wrd,font=('consolas 24 bold')).grid(row=0, column=3 ,columnspan=6,padx=10)




    frame3 = ctk.CTkFrame(root, fg_color = '#333333')
    #frame3.grid(row = 1 , column = 0)
    frame3.place(relx= 0.5, rely=0.5,anchor= ctk.CENTER)

# to generate letters of the alphabet

    n=0
    for i in ascii_letters:
        
        
        lttr_butt=ctk.CTkButton(master=frame3, text=i ,text_color= 'black',fg_color= '#55556B',command=lambda i=i: guess(i),
				 font=('montserrat', 18),
			        border_color='#8B8B3A',border_spacing=15,border_width=2,width=40, height=40).grid(row=1+n//9,column=n%9)
        n+=1
	
# to play game again

    game_butt=ctk.CTkButton(master=frame3, text="Play\nGame",text_color= 'black',fg_color='#55556B',command=lambda:newGame(), 
			     width=40, height=40,
			  font=("montserrat" ,12, "bold")).grid(row=5, column=8)






   # first_frame()
    newGame()
    root.mainloop()    
