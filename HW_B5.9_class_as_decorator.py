import time


class SecondMeter:
    def __init__(self, func, num_runs=100):
        self.func = func
        self.num_runs = num_runs

    def __call__(self, *args, **kwargs):
        avg_time = 0                     
        for _ in range(self.num_runs):
            t0 = time.time()
            ### <<полезный>> код, скорость которого мы оцениваем
            self.func(*args, **kwargs)
            t1 = time.time()
            avg_time += (t1 - t0)
        avg_time /= self.num_runs
        print("Среднее время выполнения при %s итерациях заняло %.5f секунд" % (self.num_runs, avg_time))
        return self.func(*args, **kwargs)


@SecondMeter
def f():
    for j in range(1000000):
        pass


f()
