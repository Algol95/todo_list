from seed import seed_users, seed_states
from views.task_view import runMenu

def main():
    seed_users()
    seed_states()

    runMenu()

if __name__ == "__main__":
    main()
