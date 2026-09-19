# import random_sound.py
from random_sound import RandomSound

sound_player = RandomSound()


def main():

    try:
        sound_player.initialize_mixer()
        user_music_folder = sound_player.create_audio_folder()
        extracted_files_from_folder = sound_player.extract_files_from_folder(
            user_music_folder
        )
        random_audio = sound_player.random_selection(extracted_files_from_folder)
        sound_player.play_music(str(user_music_folder), random_audio)

        # don't remove this code, otherwise script exits
        sound_player.prevent_sound_player_exit()

    except KeyboardInterrupt as e:
        print(f"Script aborted: {e}")

    finally:
        print("Shutting down, an error may have occurred if not shut down manually.")


if __name__ == "__main__":
    main()
