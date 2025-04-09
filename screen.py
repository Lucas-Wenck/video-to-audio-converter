import customtkinter
import videoToAudio
import functionality

class mainScreen(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.selected_file = None

        self.title("Video to Audio Converter")
        self.geometry("800x450")
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.button_1 = customtkinter.CTkButton(self, text="Convert", command=self.convert)
        self.button_1.grid(row=0, column=0, padx=20, pady=20)

        self.status = customtkinter.CTkLabel(self, text="No file selected", bg_color="gray", text_color="black")
        self.status.grid(row=0, column=1)

        self.button_2 = customtkinter.CTkButton(self, text="Choose the file", command=self.browse_file)
        self.button_2.grid(row=0, column=2, padx=20, pady=20)

    def convert(self):
        videoToAudio.convert_video_to_audio(self.selected_file)
        self.status.configure(text="The converted file should be in the same directory of the choosen file")

    def browse_file(self):
        self.selected_file = functionality.browse_file()
        if self.selected_file:
            self.status.configure(text="You have selected a file!", bg_color="green")

