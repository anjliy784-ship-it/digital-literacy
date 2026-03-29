from phising import detect_phising
from password import check_password
from quiz import start_quiz
from tips import show_tip 

def main () :
    while True :
        print("\n1. Phising Check")
        print("2. Password Check ")
        print("3. Quiz")
        print("4. Tip")
        print("5. Exit")

        choice = input("Enter choice : ")

        if choice == "1" :
            msg = input("Enter message : ")
            print(detect_phising(msg))
        
        elif choice == "2" :
            pwd = input("Enter password :" )

            print(check_password(pwd))
        
        elif choice == "3" :
            start_quiz()

        elif choice == "4" :
            show_tip()
        
        elif choice == "5" :
            break 
        else :
            print("Invalid choice")


if __name__ == "__main__":
    main()

        

