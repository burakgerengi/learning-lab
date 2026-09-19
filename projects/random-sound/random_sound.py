# standard library
import os
from pathlib import Path
import random
import time

# configure pygame before importing it
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

# third-party libraries
from pygame import error as PygameError
from pygame import mixer


class RandomSound:
    """handles random sound playback and audio initialization."""

    def __init__(self) -> None:
        self._mixer_initialized = False

    def create_audio_folder(self, folder_name="random-sound"):
        """create the audio folder to store user audio.

        Args:
            folder_name: name or path of the folder containing the audio file.
        """
        try:
            target = Path.home() / "Music" / "random-sound"
            print("Creating the audio folder...")
            target.mkdir(parents=True, exist_ok=True)
            print("Audio folder created")
            return str(target)

        except NotImplementedError as e:
            print("Folder creation failed: ", e)
            return ""

    def initialize_mixer(self) -> bool:
        """
        initialize the pygame audio mixer.

        Returns:
            true if initialization succeeds, otherwise false.
        """

        if self._mixer_initialized:
            return True

        try:
            print("Initializing the sound mixer...")
            mixer.init()
            print("Initializing successful.")

        except PygameError as error:
            print(f"Audio initialization failed: {error}")
            return False

        self._mixer_initialized = True
        return True

    def play_music(self, folder: str, file: str):
        """play a music file from the given folder.

        Args:
            folder: name or path of the folder containing the audio file.
            file: name of the audio file to play.
        """

        try:
            print(f"Loading audio: {file}")
            mixer.music.load(f"{folder}/{file}")
            print(f"Playing audio: {file}")
            mixer.music.play()

        except PygameError as e:
            print("Audio playing failed: ", e)

    def extract_files_from_folder(self, folder: str):
        """extract files from folder.

        Args:
            folder: name or path of the folder containing the audio file.
        """

        try:
            print("Extracting files from folder...")
            extracted_files_from_folder = [
                file for file in os.listdir(folder) if file.endswith((".mp3"))
            ]

            if extracted_files_from_folder:
                print(
                    f"{len(extracted_files_from_folder)} audio files have been loaded."
                )
                return extracted_files_from_folder

            else:
                raise FileNotFoundError(
                    "No files found matching the format, read the manual if needed."
                )

        except FileNotFoundError as e:
            print("Error:", e)
            exit()

    def random_selection(self, lst: list):
        """select a random audio file to play.
        Args:
            lst: list of audio files.
        """

        return random.choice(lst)

    def prevent_sound_player_exit(self):
        """run this method to play the sound without any issues."""
        while mixer.music.get_busy():
            time.sleep(0.1)

    def shutdown_mixer(self) -> None:
        """shut down the pygame audio mixer if it is initialized."""

        if not self._mixer_initialized:
            return

        mixer.quit()
        self._mixer_initialized = False
