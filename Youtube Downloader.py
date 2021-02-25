from pytube import YouTube
from playsound import playsound
import tkinter as tk

WINDOW_HEIGHT = 120
WINDOW_WIDTH = 500
WINDOW_TITLE = "Youtube downloader"
BUTTON_CLICK_SOUND = "clicks.m4a"


class YoutubeDownloader:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.window.configure(bg="#d80059")
        self.window.title(WINDOW_TITLE)

        # Create Labels
        self.link_label = tk.Label(self.window, text="Download Link")
        self.link_label.grid(column=0, row=0)
        self.link_label = tk.Label(self.window, text="Save File As")
        self.link_label.grid(column=0, row=1)
        self.link_label = tk.Label(self.window, text="Save File Path")
        self.link_label.grid(column=0, row=2)
        self.link_label = tk.Label(self.window, text="File extension")
        self.link_label.grid(column=0, row=3)

        # Create Entry
        self.link_entry = tk.Entry(master=self.window, width=40)
        self.link_entry.grid(column=1, row=0)
        self.name_entry = tk.Entry(master=self.window, width=40)
        self.name_entry.grid(column=1, row=1)
        self.save_path = tk.Entry(master=self.window, width=40)
        self.save_path.grid(column=1, row=2)
        self.ext_entry = tk.Entry(master=self.window, width=40)
        self.ext_entry.grid(column=1, row=3)

        # Create Buttons
        self.download_button = tk.Button(self.window, text="Download", command=self.get_link)
        self.download_button.grid(column=1, row=4)

        return

    @staticmethod
    def __downloader(link, save_path="", save_name="", extension="mp4"):
        yt = YouTube(link)
        yt_stream = yt.streams.filter(progressive=True, file_extension=extension).order_by('resolution').desc()\
            .first().download(output_path=save_path, filename_prefix=save_name)

        return

    def get_link(self):
        link = self.link_entry.get()
        path = self.save_path.get()
        name = self.name_entry.get()
        ext = self.ext_entry.get()

        self.__downloader(link, path, name, ext)

        return

    def run_app(self):
        self.window.mainloop()
        return


if __name__ == "__main__":
    app = YoutubeDownloader()
    app.run_app()
