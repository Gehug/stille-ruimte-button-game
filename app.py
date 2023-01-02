from gpiozero import LED, Button
from signal import pause
import random
from tkinter import Tk, Label, Button as Btn
import time


class GameGUI:

    def __init__(self, master):
        self.master = master
        master.title("Button game")

        self.current_game_button = Label(master, text=str(game.get_game_button()))
        self.current_game_button.pack()

        self.start_button = Btn(master, text="Start game", command=self.start_game)
        self.start_button.pack()

        # self.start_button = Btn(master, text="Reset", command=game.reset_game)
        # self.start_button.pack()

        self.exit_fullscreen = Btn(master, text="Exit fullscreen", command=lambda:root.attributes('-fullscreen',False))
        self.exit_fullscreen.pack()


    


        self.start_time = 0 # tijd wanneer de speler spel start of tijd wanneer de next game button wordt gekozen
        self.playing_time = 21 # tijd dat de speler heeft om de correcte button in te drukken
        self.lower_playing_time_by = 1 # zal om het nieuwe button press de spel sneller en sneller met 1 seconden per keer laten gaan

        self.time_left = Label(master, text="Time left: " + str(abs(int(self.playing_time - 1))))
        self.time_left.pack()


    def start_game(self):
        game.reset_game()
        game.start_game()

        # self.current_game_button.destroy()
        # self.start_button.destroy()
        # self.exit_fullscreen.destroy()
        # self.time_left.destroy()

        self.playing_time = 21


        self.time_left.config(text="Time left: " + str(abs(int(self.playing_time - 1))))



        # self.__init__(root)
        print("Start new game")
        



    def show_next_button(self):
        self.current_game_button.config(text=str(game.get_game_button()), fg="black")
        self.start_timer()


    def start_timer(self):
        self.start_time = time.time()
        self.playing_time -= self.lower_playing_time_by
        print("Timer set")
    

    def check_time_past(self):
        if (time.time() > self.start_time + self.playing_time and self.start_time != 0):
            self.current_game_button.config(text="Game Over", fg="red")
            game.game_status = "not_playing"
            print("Game over")

        elif self.start_time != 0:
            self.time_left.config(text="Time left: " + str( abs(int(time.time() - (self.playing_time + self.start_time)))))
            




class PlayButton(Button):


    virtual_button = 1

    button_list = []
    def __init__(self, pin=None, pull_up=True, active_state=None, bounce_time=None,
            hold_time=1, hold_repeat=False, pin_factory=None):

        super(Button, self).__init__(
            pin, pull_up=pull_up, active_state=active_state,
            bounce_time=bounce_time, pin_factory=pin_factory)
        self.hold_time = hold_time
        self.hold_repeat = hold_repeat
        self.gpio_pin = pin
        # self.when_pressed = lambda : game.check_correct_button_press(self.get_pin())
        self.virtual_button = PlayButton.virtual_button
        PlayButton.virtual_button += 1


        PlayButton.button_list.append(pin)


    def get_pin(self):
        return self.gpio_pin

    def get_virtual_button(self):
        return self.virtual_button
        
    @classmethod
    def list_objects(cls):
        return cls.button_list

    
     



class Game():
    def __init__(self, buttons):
        self.game_status = "not_started" # in welke status de game zich bevind, mogelijkheden --> not_started, started, lost, won
        self.level = 1 # welk level de game zich bevind
        self.buttons = buttons # lijst met alle instancies van de button class 

        self.previous_game_button = None
        self.current_game_button = random.choice(self.buttons)

    
    def change_game_status(self, status): # veranderen van gamestatus
        self.game_status = status

    def check_game_status(self): # checken van gamestatus
        return self.game_status

    def next_game_level(self): # laat spel over gaan naar volgene level

        self.level += 1
        self.next_button()
        print(self.current_game_button)
        my_gui.show_next_button()

    def check_game_level(self): # checken welk gamelevel het spel zich bevind
        return self.level

    def next_button(self): # geeft een random lijst van de knoppen terug


        new_button = random.choice(self.buttons)
        if self.previous_game_button == None:
            self.previous_game_button = self.current_game_button
            while new_button == self.previous_game_button:
                new_button = random.choice(self.buttons)
            self.current_game_button = new_button

        else:
    
            while new_button == self.previous_game_button:
                new_button = random.choice(self.buttons)
            self.current_game_button = new_button


            
    def get_game_button(self):
        return self.current_game_button

    

    def check_correct_button_press(self, button):
        print(f"button {button} pressed")

        if (self.check_game_status() == "started"):
            print(f"game started target {self.current_game_button}")

            if button == self.current_game_button:
                print(f"Level: {self.current_game_button} gehaald!")
                self.next_game_level()

        
    def reset_game(self):
        self.__init__(self.buttons)
        my_gui.show_next_button()

    def start_game(self):
        print("Game started")
        self.change_game_status("started")
        my_gui.start_timer()




# Game Buttons
button1 = PlayButton(4) # virtual button 1
button2 = PlayButton(17) # virtual button 2
button3 = PlayButton(27) # virtual button 3
button4 = PlayButton(22) # virtual button 4
button5 = PlayButton(10) # virtual button 5
button6 = PlayButton(9) # virtual button 6
button7 = PlayButton(11) # virtual button 7
button8 = PlayButton(5) # virtual button 8
button9 = PlayButton(6) # virtual button 9
button10 = PlayButton(13) # virtual button 10
button11 = PlayButton(26) # virtual button 11
button12 = PlayButton(23) # virtual button 12
button13 = PlayButton(24) # virtual button 13
button14 = PlayButton(25) # virtual button 14
button15 = PlayButton(8) # virtual button 15
button16 = PlayButton(7) # virtual button 16
button17 = PlayButton(12) # virtual button 17
button18 = PlayButton(16) # virtual button 18

button_obj_list = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16, button17, button18]




game = Game([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])



# Add action to the buttons



def check_button_states():

    my_gui.check_time_past()
    buttons = button_obj_list

    for button in buttons:
        if button.is_pressed:
            game.check_correct_button_press(button.get_virtual_button())

    root.after(100, check_button_states)







root = Tk()
root.attributes('-fullscreen',True)
my_gui = GameGUI(root)

root.after(100, check_button_states)
root.mainloop()