def provide_access(user):
    return {
        "user_id" : user,
        "password" : "admin"
    }

def run_match():
    user = str(input("Please give your name"))

    match user:
        case "Gireesh":
            print("User has access only to app")
            print("access will not be provided")

        case "Anjana":
            print("Anjana has access to database")
            provide_access(user)

        case "Dhinesh":
            print("User has access only to front-end code")
            print("access will not be provided")

        case _:
            print("You do not have any access to the code")






























if __name__ == "__main__":
    for i in range(3):
        run_match()
