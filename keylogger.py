import tkinter as tk

class KeyLogger:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Key Logger")
        
        # Flag to track logging state
        self.keylogger_active = False
        
        # Create a label to toggle logging
        self.label = tk.Label(self.root, text="Click to Toggle Logging", 
                               bg="light gray", 
                               width=20, 
                               height=2)
        self.label.pack(pady=20)
        
        # Bind the label click event
        self.label.bind("<Button-1>", self.toggle_logging)
        
        # Bind key press event to the entire window
        self.root.bind("<Key>", self.on_key_press)

    def toggle_logging(self, event):
        # Toggle the logging state
        self.keylogger_active = not self.keylogger_active
        
        # Update label appearance based on logging state
        if self.keylogger_active:
            self.label.config(text="Logging ON", bg="green")
            print("LOGGING ACTIVATED")
        else:
            self.label.config(text="Logging OFF", bg="red")
            print("LOGGING DEACTIVATED")

    def on_key_press(self, event):
        # Only log keys if logging is active
        if self.keylogger_active:
            # Print the pressed key, handle special keys
            if event.char:
                print(f"Key pressed: {repr(event.char)}")
            else:
                print(f"Special key pressed: {event.keysym}")

    def run(self):
        # Start the Tkinter event loop
        self.root.mainloop()

# Create and run the application
if __name__ == "__main__":
    app = KeyLogger()
    app.run()