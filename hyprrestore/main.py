import sys
import save
import restore

def main() :
    if len(sys.argv) < 2 :
        print("Usage: python main.py [save | restore]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "save" :
        save.save_session()

    elif command == "restore" :
        restore.restore_session()

    else :
        print(f"Unknown command: {command}")
        print("Usage: python main.py [save | restore]")
        sys.exit(1)

if __name__ == "__main__" :
    main()
