# Write your solution here:
# class Task:
#     id = 0
#     def __init__(self, description: str, programmer: str, workload: int):
#         self.description = description
#         self.programmer = programmer
#         self.workload = workload
#         self.complete = "NOT FINISHED"
#         Task.id += 1
#         self.identification = Task.id
#
#     def __str__(self):
#         return f"{self.identification}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.complete}"
#
#     def is_finished(self):
#         if self.complete == "NOT FINISHED":
#             return False
#         if self.complete == "FINISHED":
#             return True
#         return False
#
#     def mark_finished(self):
#         self.complete = "FINISHED"

#
# class OrderBook:
#     def __init__(self):
#         self.orders = []
#
#     def add_order(self, description: str, programmer: str, workload: int):
#         task = Task(description, programmer, workload)
#         self.orders.append(task)
#
#
#     def all_orders(self):
#         return self.orders
#
#     def programmers(self):
#         programmers_name = []
#         for order in self.orders:
#             programmers_name.append(order.programmer)
#         return list(set(programmers_name))
#
#     def mark_finished(self, id: int):
#         for order in self.all_orders():
#             if order.identification == id:
#                 order.mark_finished()
#                 return
#         raise ValueError("No task found with that id")
#
#     def finished_orders(self):
#         return [task for task in self.orders if task.is_finished()]
#
#     def unfinished_orders(self):
#         return [task for task in self.orders if not task.is_finished()]
#
#     def status_of_programmer(self, programmer: str):
#         finish = 0
#         unfinish = 0
#         finish_time = 0
#         unfinish_time = 0
#         if programmer not in self.programmers():
#             raise ValueError("Name not found")
#         for task in self.orders:
#             if task.programmer == programmer:
#                 if task.is_finished():
#                     finish += 1
#                     finish_time += task.workload
#                 else:
#                     unfinish += 1
#                     unfinish_time += task.workload
#         return (finish, unfinish, finish_time, unfinish_time)

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

if __name__ == "__main__":
    # t1 = Task("program hello world", "Eric", 3)
    # print(t1.id, t1.description, t1.programmer, t1.workload)
    # print(t1)
    # print(t1.is_finished())
    # t1.mark_finished()
    # print(t1)
    # print(t1.is_finished())
    # t2 = Task("program webstore", "Adele", 10)
    # t3 = Task("program mobile app for workload accounting", "Eric", 25)
    # print(t2)
    # print(t3)
    #
    # print()
    #
    # orders = OrderBook()
    # orders.add_order("program webstore", "Adele", 10)
    # orders.add_order("program mobile app for workload accounting", "Eric", 25)
    # orders.add_order("program app for practising mathematics", "Adele", 100)
    #
    # for order in orders.all_orders():
    #     print(order)
    #
    # print()
    #
    # for programmer in orders.programmers():
    #     print(programmer)
    #
    #
    # print()
    #
    # orders = OrderBook()
    # orders.add_order("program webstore", "Adele", 10)
    # orders.add_order("program mobile app for workload accounting", "Eric", 25)
    # orders.add_order("program app for practising mathematics", "Adele", 100)
    #
    # orders.mark_finished(1)
    # orders.mark_finished(2)
    #
    # for order in orders.all_orders():
    #     print(order)
    #
    # print()
    #
    # for order in orders.finished_orders():
    #     print(order)
    #
    # print()
    #
    # for order in orders.unfinished_orders():
    #     print(order)

    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)


    status = orders.status_of_programmer("Adele")
    print(status)

