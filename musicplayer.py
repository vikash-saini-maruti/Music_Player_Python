import pygame
import os

# Initialize pygame
pygame.init()

# Create a function to play music
def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# List music files in a directory
def list_music_files(directory):
    music_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith((".mp3", ".wav")):
                music_files.append(os.path.join(root, file))
    return music_files

# Main function
def main():
    music_directory = "./C:/Users/vikas/Downloads/"  # Change this to your music directory
    music_files = list_music_files(music_directory)

    if not music_files:
        print("No music files found in the directory.")
        return

    print("Available songs:")
    for i, file in enumerate(music_files, start=1):
        print(f"{i}. {os.path.basename(file)}")

    while True:
        try:
            choice = int(input("Enter the number of the song you want to play (0 to exit): "))
            if choice == 0:
                pygame.mixer.music.stop()
                pygame.quit()
                break
            elif 1 <= choice <= len(music_files):
                selected_song = music_files[choice - 1]
                print(f"Playing {os.path.basename(selected_song)}...")
                play_music(selected_song)
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
