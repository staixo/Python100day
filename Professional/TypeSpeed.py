import tkinter as tk
import random
from datetime import datetime

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        
        self.target_text = "The quick brown fox jumps over the lazy dog."
        self.current_index = 0
        self.errors = 0
        self.start_time = None
        
        self.info_label = tk.Label(root, text="Type the following text:")
        self.info_label.pack()
        
        self.target_label = tk.Label(root, text=self.target_text)
        self.target_label.pack()
        
        self.input_text = tk.Text(root, height=5)
        self.input_text.pack()
        
        self.start_button = tk.Button(root, text="Start", command=self.start_test)
        self.start_button.pack()
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
        
        self.root.bind('<Key>', self.check_key)
    
    def start_test(self):
        self.start_button.configure(state=tk.DISABLED)
        self.start_time = datetime.now()
    
    def check_key(self, event):
        if self.start_time is None:
            return
        
        if event.char == self.target_text[self.current_index]:
            self.current_index += 1
            self.target_label.configure(text=self.target_text[:self.current_index] + ' ' + self.target_text[self.current_index:])
            
            if self.current_index == len(self.target_text):
                self.finish_test()
        else:
            self.errors += 1
        
    def finish_test(self):
        self.root.unbind('<Key>')
        elapsed_time = datetime.now() - self.start_time
        minutes = elapsed_time.seconds // 60
        seconds = elapsed_time.seconds % 60
        
        accuracy = (len(self.target_text) - self.errors) / len(self.target_text) * 100
        wpm = len(self.target_text) / 5 / (elapsed_time.seconds / 60)
        
        result = f"Time: {minutes:02d}:{seconds:02d}\n"
        result += f"Accuracy: {accuracy:.2f}%\n"
        result += f"WPM: {wpm:.2f}"
        
        self.result_label.configure(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
