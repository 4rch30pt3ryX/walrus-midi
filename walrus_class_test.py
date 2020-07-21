import mido, sys
import tkinter as tk

#mido.set_backend('mido.backends.pygame')
print(mido.backend)

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        # Main Window
        mako_image = tk.PhotoImage(file=r"C:\Users\laroe\Downloads\makoD1-2.PNG")
        greeting = tk.Label(
            text="\n   *WIP* Walrus Mako series D-1 Delay pedal Interface *WIP*   \n",
            fg="#e1b3f2",
            bg="black",
            image=mako_image
            )
        greeting.image = mako_image
        greeting.pack()
        
        # Defining Output Port input structure
        output_label = tk.Label(
            master = root,
            text= "Select Midi Output Port"
            )
        root.title("Mako D-1 Interface by 4rch30pt3ryX")
        #import pdb; pdb.set_trace()
        input_ports = mido.get_input_names()
        OptionList = input_ports
        OptionList.append('Debug')
        print(OptionList)
        variable = tk.StringVar(root)

        # Checks if any MIDI devices are connected and automatically quits if not
        try:
            variable.set(OptionList[0])
        except IndexError as e:
            print(e)
            sys.exit('It appears you have no Midi devices connected.')

        # function to pull the selected item from drop down    
        def callback(*args):
            variable.get()
        variable.trace("w", callback)

        # Dropdown specific functions for Output Port
        opt = tk.OptionMenu(root, variable, *OptionList)
        opt.config(width=30, font=('Helvetica', 8))
        output_label.pack()
        opt.pack()
        
        # Defining Preset input structure
        preset_frame = tk.Frame()
        preset_label = tk.Label(
            master=preset_frame, 
            text="Enter Preset 0-127"
            )
        preset = tk.Entry(
            fg="black",
            bg="#e1b3f2",
            width=14,
            )

        # Function to send user input as a midi PC message to change preset
        def preset_input():      
            usr_input = int(preset.get())
            print(usr_input)
            midi_msg = mido.Message("program_change", program=usr_input, channel=1)
            with mido.open_output() as outport:
                outport.send(midi_msg)
            if outport.closed:
                print("Yup, it's closed.")
            
        preset_button = tk.Button(
            preset_frame,
            text="Load Preset",
            width=9,
            command=preset_input,
            fg="#e1b3f2",
            bg="grey"
            )
        preset_label.pack()        
        preset.pack()
        preset_button.pack()
        preset_frame.pack()        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Walrus Audio Mako D-1")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()