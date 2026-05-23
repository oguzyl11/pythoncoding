task_board = {
    "to_do": ["code login page", "design database schema","perform API testing"],
    "in_progress": ["json integration"],
    "done": ["matrix algorithm implementation", "hotel tracking algorithm implementation"]
}

def show_dashboard(board):
    for status, tasks in board.items():
        print(f"--- {status.upper()} ---")
        for task in tasks:
            print(f" * {task}")

def move_task(board ):
    task = input("Which task do you want to move?")
    from_status = input("From which status? (to_do, in_progress, done)")
    from_status = from_status.strip().lower()
    to_status = input("To which status? (to_do, in_progress, done)")
    to_status = to_status.strip().lower()
    if task in board[from_status]:
        board[from_status].remove(task)
        board[to_status].append(task)
        print(f"Task '{task}' moved from '{from_status}' to '{to_status}'.")
        show_dashboard(board)
move_task(task_board)    
    

