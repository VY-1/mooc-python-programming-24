# Write your solution here
# If you use the classes made in the previous exercise, copy them here
from scripts.regsetup import description


class Task:
    id = 0
    @classmethod 
    def new_id(cls):
        Task.id += 1
        return Task.id
 
    def __init__(self, description, programmer, workload):
        self.programmer = programmer
        self.description = description
        self.workload = workload
        self.id = Task.new_id()
        self.finished = False
    
    def is_finished(self):
        return self.finished 
 
    def mark_finished(self):
        self.finished = True
 
    def __str__(self):
        status = "NOT FINISHED" if not self.finished else "FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"
 
class OrderBook:
    def __init__(self):
        self.__tasks = []
 
    def add_order(self, description, programmer, workload):
        self.__tasks.append(Task(description, programmer, workload))
 
    def all_orders(self):
        return self.__tasks
 
    def programmers(self):
        return list(set([t.programmer for t in self.__tasks]))
 
    def mark_finished(self, id: int):
        for task in self.__tasks:
            if task.id == id:
                task.mark_finished()
                return
        
        # not incorrect
        raise ValueError("wrong id")
    
    def unfinished_orders(self):
        return [t for t in self.__tasks if not t.is_finished()]
 
    def finished_orders(self):
        return [t for t in self.__tasks if t.is_finished()]
 
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError("Programmer does not exists")
        
        finished_tasks = [t for t in self.__tasks if t.programmer == programmer and t.is_finished() ]
        not_finished_tasks = [t for t in self.__tasks if t.programmer == programmer and not t.is_finished() ]
 
        finished_hours = sum(t.workload for t in finished_tasks)
        not_finished_hours = sum(t.workload for t in not_finished_tasks)
 
        return (len(finished_tasks), len(not_finished_tasks), finished_hours, not_finished_hours)
    
class OrderBookApplication:
    def __init__(self):
        self.order_book = OrderBook()

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        description = input("description: ")
        programmer_and_workload = input("programmer and workload estimated: ").split(" ")
        if len(programmer_and_workload) !=2:
            print("erroneous input")
            return
        try:
            programmer = programmer_and_workload[0]
            workload = int(programmer_and_workload[1])
        except:
            print("erroneous input")
            return

        self.order_book.add_order(description, programmer, workload)
        print("added!")

    def finished_tasks(self):
        if len(self.order_book.finished_orders()) == 0:
            print("no finished tasks")
        else:
            for task in self.order_book.finished_orders():
                print(task)

    def unfinished_tasks(self):
        if len(self.order_book.unfinished_orders()) == 0:
            print("no unfinished tasks")
        else:
            for task in self.order_book.unfinished_orders():
                print(task)

    def mark_finished(self):
        
        try:
            id = int(input("id: "))
            self.order_book.mark_finished(id)
            print("marked as finished")
        except:
            print("erroneous input")
            return

    def programmers(self):
        for programmer in self.order_book.programmers():
            print(programmer)

    def status_of_programmer(self):
        programmer = input("programmer: ")
        try:
            status = self.order_book.status_of_programmer(programmer)
        except:
            print("erroneous input")
            return
        print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")

    def execute(self):
        self.help()
        while True:
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.finished_tasks()
            elif command == "3":
                self.unfinished_tasks()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.programmers()
            elif command == "6":
                self.status_of_programmer()


app = OrderBookApplication()
app.execute()