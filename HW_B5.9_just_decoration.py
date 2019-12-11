import time

# class SecondMeter:
#     def __init__(self, func, num_runs=100):
#         self.time = None
#         self.func = func
#         self.num_runs = num_runs

#     def __enter__(self):    # возвращаем сами себя когда входим в контекст
#         return self

#     def __exit__(self, func, num_runs): # на выходе выводим на экран среднее время выполнения
#         self.time = time.time()         # стартуем отсчет времени
#         avg_time = 0                    # 
#         for _ in range(self.num_runs):
#             ### <<полезный>> код, скорость которого мы оцениваем
#             self.func(*args, **kwargs)
#             t1 = time.time()
#             avg_time += (t1 - t0)
#         avg_time /= self.num_runs
#         print("Среднее время выполнения заняло %.5f секунд" % avg_time)
      

def time_this(num_runs):
    def decorator(func):
        def wrap():
            avg_time = 0
            for _ in range(num_runs):
                t0 = time.time()
                ### <<полезный>> код, скорость которого мы оцениваем
                func()
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= num_runs
            return print("Среднее время по ", str(num_runs), "итерациям заняло %.5f секунд" % avg_time)
        return wrap
    return decorator


@time_this(num_runs=10)
def f():
    for j in range(1000000):
        pass


print(f())