import customtkinter
import functionality
import threading


class VideoAudioScreen(customtkinter.CTk):
    def __init__(self, conversion_choice):
        super().__init__()
        self.conversion_choice = conversion_choice
        self.selected_file = None
        self.audio_format = "wav"

        self.title("Converter")
        self.geometry("800x450")
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 3), weight=1)

        self.button_1 = customtkinter.CTkButton(self, text="Convert", command=self.start_convert)
        self.button_1.grid(row=3, column=0, padx=20, pady=20, columnspan=3, sticky="ew")

        self.status = customtkinter.CTkLabel(self, corner_radius=10, text="No file selected", fg_color="gray", text_color="black")
        self.status.grid(row=2, column=0, ipadx=20)

        self.option_info = customtkinter.CTkLabel(self, corner_radius=10, text="Choose the audio format", fg_color="gray", text_color="black")
        self.option_info.grid(row=1, column=2, pady=5)

        if self.conversion_choice == "Video to Audio" or self.conversion_choice == "Audio to Audio":
            self.optionMenu = customtkinter.CTkOptionMenu(self, values=["wav", "mp3", "flac", "aac"], command=self.format_choice)

        elif self.conversion_choice == "Video to Video":
            self.option_info.configure(text="Choose the video format")
            self.optionMenu = customtkinter.CTkOptionMenu(self, values=["mp4", "mkv", "wmv", "gif"], command=self.format_choice)

        self.optionMenu.grid(row=2, column = 2)

        self.button_2 = customtkinter.CTkButton(self, text="Choose the file", command=self.browse_file)
        self.button_2.grid(row=0, column=1, padx=20, pady=20)

    def start_convert(self):
        self.button_1.configure(state="disabled")
        self.button_2.configure(state="disabled")
        self.optionMenu.configure(state="disabled")
        self.status.configure(text="The conversion is happening please wait...")

        thread = threading.Thread(target=self.convert, daemon=True)
        thread.start()

    def convert(self):
        functionality.convert_video_to_audio(self.selected_file, self.audio_format)
        self.status.configure(text="The converted file should be in the same directory of the choosen file")
        self.button_1.configure(state="normal")
        self.button_2.configure(state="normal")
        self.optionMenu.configure(state="normal")

    def browse_file(self):
        self.selected_file = functionality.browse_file(self.conversion_choice)
        if self.selected_file:
            self.status.configure(text="You have selected a file!", fg_color="green")
        self.button_1.configure(state="normal")

    def format_choice(self, choice):
        self.audio_format = choice

class MainScreen(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conversion_choice = "Video to Audio"

        self.title("Converter")
        self.geometry("800x450")

        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.conversion_option = customtkinter.CTkOptionMenu(self, values=["Video to Audio", "Video to Video", "Audio to Audio"], command=self.choice)
        self.conversion_option.grid(row=0, column=0)

        self.conversion_option_button = customtkinter.CTkButton(self, text="Video to Audio", command=self.app_choice)
        self.conversion_option_button.grid(row=1, column=0)

    def app_choice(self):
        if self.conversion_choice == "Video to Audio":
            videoToAudio = VideoAudioScreen(self.conversion_choice)
            videoToAudio.mainloop()
        elif self.conversion_choice == "Audio to Audio":
            videoToAudio = VideoAudioScreen(self.conversion_choice)
            videoToAudio.mainloop()
        elif self.conversion_choice == "Video to Video":
            videoToAudio = VideoAudioScreen(self.conversion_choice)
            videoToAudio.mainloop()

    def choice(self, choice):
        self.conversion_choice = choice
        self.conversion_option_button.configure(text=f"{self.conversion_choice}")
