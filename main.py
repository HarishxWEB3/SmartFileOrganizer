from file_organizer import FileOrganizer
import os

def main():
    path = input("📁 Enter folder path to organize: ").strip()
    
    if not os.path.exists(path):
        print("❌ The path does not exist.")
        return

    organizer = FileOrganizer(path)
    organizer.organize()

if __name__ == "__main__":
    main()
