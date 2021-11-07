from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

# Create database file
engine = create_engine('sqlite:///todo.db?check_same_thread=False')

# Base object for table below
Base = declarative_base()


# Describe table as a class
class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


# Create table in database
Base.metadata.create_all(engine)

# Open a session to access table
Session = sessionmaker(bind=engine)
session = Session()


def add_task():
    print("Enter task")
    new_task = input()
    print("Enter deadline")
    new_deadline = datetime.strptime(input(), '%Y-%m-%d')
    new_row = Table(task=new_task,
                    deadline=new_deadline.date())
    session.add(new_row)
    session.commit()
    print("The task has been added!")


def today_tasks():
    print(f"Today {datetime.today().strftime('%#d %b')}:")
    tasks = session.query(Table).filter(Table.deadline == datetime.today().date()).order_by(Table.deadline).all()
    if not tasks:
        print("Nothing to do!\n")
    else:
        for todo in tasks:
            print(f"{todo.id}. {todo.task}")
        print()


def week_tasks():
    dl = datetime.today()
    for n_day in range(7):
        tasks = session.query(Table).filter(Table.deadline == dl.date()).order_by(Table.deadline).all()
        if not tasks:
            print(f"{dl.strftime('%A %#d %b')}:")
            print("Nothing to do!")
        else:
            for todo in tasks:
                print(f"{dl.strftime('%A %#d %b')}:")
                print(f"{todo.id}. {todo.task}")
        print()
        dl += timedelta(days=1)


def all_tasks():
    print("All tasks:")
    tasks = session.query(Table).order_by(Table.deadline).all()
    for todo in tasks:
        print(f"{todo.id}. {todo.task}. {todo.deadline.strftime('%#d %b')}")


def missed_tasks():
    print("Missed tasks:")
    tasks = session.query(Table).order_by(Table.deadline).filter(Table.deadline < datetime.today().date()).all()
    for todo in tasks:
        print(f"{todo.id}. {todo.task}. {todo.deadline.strftime('%#d %b')}")
    print()


def delete_task():
    tasks = session.query(Table).order_by(Table.deadline).all()
    if not tasks:
        print("Nothing to do!")
    else:
        print("Choose the number of the task you want to delete:")
        for todo in tasks:
            print(f"{todo.id}. {todo.task}. {todo.deadline.strftime('%#d %b')}")
        n_delete = int(input())
        raw_to_delete = tasks[n_delete - 1]
        session.delete(raw_to_delete)
        session.commit()
    print("The task has been deleted!")
    print()


while True:
    print("1) Today's tasks\n"
          "2) Week's tasks\n"
          "3) All tasks\n"
          "4) Missed tasks\n"
          "5) Add task\n"
          "6) Delete task\n"
          "0) Exit")
    choice = input()
    if choice == "1":
        today_tasks()
    elif choice == "2":
        week_tasks()
    elif choice == "3":
        all_tasks()
    elif choice == "4":
        missed_tasks()
    elif choice == "5":
        add_task()
    elif choice == "6":
        delete_task()
    elif choice == "0":
        break
    else:
        print("Bye!")
