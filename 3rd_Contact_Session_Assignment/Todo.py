# Build a to-do list in python and use Postgres for persistent storage.


from psycopg2 import connect
from dotenv import load_dotenv
import os

load_dotenv('.env')

'''
todo:
1. add to  list
2. delete from list
3. completed 
4. edit todo
'''
DATABASE = os.getenv('DATABASE')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
PORT = os.getenv('PORT')
HOST = os.getenv('HOST')


class Todo:
    conn = None
    Name = None
    Email = None

    def __init__(self, Name, Email):
        self.Name = Name
        self.Email = Email
        try:
            print(DATABASE)
            self.conn = connect(
                dbname=DATABASE,
                user=USER,
                password=PASSWORD,
                host=HOST,
                port=PORT
            )
            print("Connection successful")
        except Exception as e:
            print(f"Error: {e}")

    def CreateUser(self) -> bool:
        if self.is_User_in_db() != []:
            return True
        try:
            cur = self.conn.cursor()
            cur.execute(
                f"""
                    INSERT INTO users(name,email,created_at)
                    VALUES('{self.Email}', '{self.Email}', CURRENT_TIMESTAMP);
                """
            )
            self.conn.commit()
            cur.close()
            return True
        except Exception as e:
            print(e)
            return False

    def Create_Task(self, Task, User_id):
        cur = self.conn.cursor()
        cur.execute(
            f"""
                INSERT INTO tasks(task,user_id,created_at)
                VALUES('{Task}',{User_id},CURRENT_TIMESTAMP);
            """
        )
        self.conn.commit()
        cur.close()

    def Delete_from_db(self,id):
        cur = self.conn.cursor()
        cur.execute(
            f"""
        DELETE FROM tasks
        WHERE id = {id};
            """
        )
        self.conn.commit()
        cur.close()

    def Mark_as_completed(self,id,mark_as_Uncompleted=False):
        cur = self.conn.cursor()
        cur.execute(
                f"""
                UPDATE tasks
                SET completed = {False if mark_as_Uncompleted else True}
                WHERE id = {id}
                """
        )
        self.conn.commit()
        cur.close()

    def Edit_Todo(self,NewTask,id):
        cur = self.conn.cursor()
        cur.execute(
            f"""
                UPDATE tasks
                SET task = {NewTask}
                WHERE id = {id}
            """
        )
        self.conn.commit()
        cur.close()

    def getTasks(self, User_id,is_completed=False):
        cur = self.conn.cursor()
        cur.execute(
            f"""
                SELECT id,task, completed from tasks WHERE user_id = {User_id}
            """
        )
        rows = cur.fetchall()
        self.conn.commit()
        cur.close()
        for row in rows:
            print(f"ID:{row[0]} Task: {row[1]} completed: {row[2]}")

    def is_User_in_db(self, print_data=False) -> list:
        cur = self.conn.cursor()
        cur.execute(
            f"""
                SELECT name,email,id FROM users WHERE email = '{self.Email}'
            """
        )
        rows = cur.fetchall()
        self.conn.commit()
        cur.close()
        if print_data:
            print(rows)
        return rows





def StartTodo():
    print('Welcome  to OCC Todo App')
    print()
    Name = input('Please enter your name\n')
    Email = input('Please enter your email\n')
    User = Todo(Name,Email)
    User.CreateUser()
    is_user_in_db = User.is_User_in_db()

    option = '' 
    while True:
        if option == '6':
            break
        print('What Operation do you want to perform today?')
        print("""
        Enter:
            1 for get tasks.
            2 for add tasks
            3 for mark as completed
            4 update task
            5 delete task
            6 exit

            """)
        option = input('enter option: ')
        if option == '1':
            User.getTasks(is_user_in_db[0][2])
        elif option == '2':
            Task = input('Enter Task\n')
            User.Create_Task(Task=Task,User_id=is_user_in_db[0][2])
        elif option == '3':
            ID = input('Enter the task id: ')
            User.Mark_as_completed(ID)
        elif option == '4':
            newTask = input('Enter the new Task\n')
            ID = print('Enter the id of task to update: ')
            User.Edit_Todo(id=ID,NewTask=newTask)
        elif option == '5':
            ID = input('Enter the id of the task to delete: ')
            User.Delete_from_db(ID)
        else: 
            continue


if __name__ == '__main__':
    StartTodo()
