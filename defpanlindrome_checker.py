def palindrome_checker():
    print("""
    ____        _      _           _                       
   |  __ \     | |    (_)         | |                      
   | |__) |__ _| |_ __ _  ___  ___| |__   ___  _ __  _   _ 
   |  ___/ _` | | '__| |/ _ \/ __| '_ \ / _ \| '_ \| | | |
   | |  | (_| | | |  | |  __/ (__| | | | (_) | | | | |_| |
   |_|   \__,_|_|_|  |_|\___|\___|_| |_|\___/|_| |_|\__,_|
              WELCOME TO PALINDROME CHECKER
                                                         
        """)
    while True:
        userinput = input('Enter any word to check (or type "exit" to quit): ')

        if userinput.lower() == 'exit':
            print("Exiting the program.")
            break

        reversedinput = userinput[::-1]

        if userinput == reversedinput:
            print(f"'{userinput}' is a palindrome.")
        else:
            print(f"'{userinput}' is not a palindrome.")

palindrome_checker()
