import os
import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod


class SmartDevice(ABC):
    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def execute_action(self):
        pass

    
    @abstractmethod
    def turn_off(self):
        pass



class SmartLight(SmartDevice):
    def __init__(self):
        super().__init__("Living room smart light")

    def execute_action(self):
        return f"{self._name}: Set brightness to 100%"

    def turn_off(self):
        return f"{self._name}: Turned OFF"


class SmartSpeaker(SmartDevice):
    def __init__(self):
        super().__init__("Alexa speaker")

    def execute_action(self):
        return f"{self._name}: Set volume to 100%"

    def turn_off(self):
        return f"{self._name}: Stopped playing audio"


class SmartOven(SmartDevice):
    def __init__(self):
        super().__init__("Kitchen Oven")

    def execute_action(self):
        return f"{self._name}: Baking"

    def turn_off(self):
        return f"{self._name}: Finish bake"



class SmartAC(SmartDevice):
    def __init__(self):
        super().__init__("Air Conditioner")

    def execute_action(self):
        return f"{self._name}: Temperature set to 22°C"

    def turn_off(self):
        return f"{self._name}: Compressor powered down"




class PolymorphicAppTemplate(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("OOP Lab: Polymorphism GUI Template")
        self.geometry("520x520")
        self.resizable(False, False)

        dir_actual = os.path.dirname(os.path.abspath(__file__))
        icon_dir = os.path.join(dir_actual, "icon.png")

        if os.path.exists(icon_dir):
            
            icon_img = tk.PhotoImage(file=icon_dir)
            self.iconphoto(False, icon_img)
            
            
            self._icon_ref = icon_img
        
       
        self.items = {
            "Light": SmartLight(),
            "Speaker": SmartSpeaker(),
            "Oven": SmartOven(),
            "AC": SmartAC()
        }

      
        self._build_interface()

    def _build_interface(self):
     
        lbl_header = tk.Label(
            self,
            text="SMART HOME POLYMORPHISM",
            font=("Arial", 15, "bold"),
            fg="#2c3e50"
        )
        lbl_header.pack(pady=10)

        group_box = tk.LabelFrame(
            self,
            text=" Select a Device ",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=10
        )
        group_box.pack(fill="x", padx=20, pady=5)

       
        first_key = list(self.items.keys())[0]
        self.selected_key = tk.StringVar(value=first_key)

        for key in self.items.keys():
            rb = ttk.Radiobutton(
                group_box,
                text=key,
                value=key,
                variable=self.selected_key
            )
            rb.pack(anchor="w", pady=2)

        
        frame_buttons = tk.Frame(self)
        frame_buttons.pack(pady=10)

      
        btn_action = tk.Button(
            frame_buttons,
            text="EXECUTE ACTION",
            command=self._handle_action,
            bg="#2980b9",
            fg="white",
            font=("Arial", 9, "bold"),
            relief="raised",
            cursor="hand2",
            padx=10,
            pady=5
        )
        btn_action.pack(side="left", padx=5)

        
        btn_turn_off = tk.Button(
            frame_buttons,
            text="TURN OFF",
            command=self._handle_turn_off,
            bg="#c0392b",
            fg="white",
            font=("Arial", 9, "bold"),
            relief="raised",
            cursor="hand2",
            padx=10,
            pady=5
        )
        btn_turn_off.pack(side="left", padx=5)

      
        self.lbl_output = tk.Label(
            self,
            text="Select a device above and choose an action.",
            font=("Arial", 9, "italic"),
            bg="#ecf0f1",
            fg="#34495e",
            relief="groove",
            height=2,
            wraplength=460,
            justify="center"
        )
        self.lbl_output.pack(fill="x", padx=20, pady=5)

        log_frame = tk.LabelFrame(
            self,
            text=" Activity Log ",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5
        )
        log_frame.pack(fill="both", expand=True, padx=20, pady=10)

        scrollbar = ttk.Scrollbar(log_frame, orient="vertical")
        self.lst_activity = tk.Listbox(
            log_frame,
            yscrollcommand=scrollbar.set,
            font=("Consolas", 9)
        )
        scrollbar.config(command=self.lst_activity.yview)

        scrollbar.pack(side="right", fill="y")
        self.lst_activity.pack(side="left", fill="both", expand=True)

    def _log_event(self, message: str):
        """Método auxiliar para actualizar la etiqueta de salida y registrar en la lista."""
        self.lbl_output.config(text=message, font=("Arial", 9, "normal"))
        self.lst_activity.insert(tk.END, message)
        self.lst_activity.see(tk.END)  # Auto-scroll hacia abajo

    def _handle_action(self):
        chosen_key = self.selected_key.get()
        active_object: SmartDevice = self.items[chosen_key]
        result_message = active_object.execute_action()
        self._log_event(f"[ACTION] {result_message}")

    def _handle_turn_off(self):
        chosen_key = self.selected_key.get()
        active_object: SmartDevice = self.items[chosen_key]
        result_message = active_object.turn_off()
        self._log_event(f"[TURN OFF] {result_message}")


if __name__ == "__main__":
    app = PolymorphicAppTemplate()
    app.mainloop()