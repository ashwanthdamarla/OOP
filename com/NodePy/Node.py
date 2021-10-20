import threading
import queue
from Events import Event
from concurrent.futures import ThreadPoolExecutor


class NodePy(object):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.event_q = queue.Queue()
            cls.is_completed = False
            cls.event_loop = threading.Thread(name='Event-Loop-Thread', target=cls.loop_queue)
            cls.pool = ThreadPoolExecutor(6)
            cls.run_loop_forever = False
            cls.__instance = super(NodePy, cls).__new__(cls)
        return cls.__instance

    ####################
    # execute_function #
    ####################
    @classmethod
    def exec(cls, func, params):
        e = Event(func, params)
        cls.event_q.put(e)
        return e

    ###############
    # task runner #
    ###############
    def task_runner(self):
        pass

    ##############
    # event loop #
    ##############
    @classmethod
    def loop_queue(cls):
        while cls.run_loop_forever or not cls.event_q.empty():
            if cls.event_q.qsize() > 0:
                event = cls.event_q.get()
                while not event.is_active:
                    event.set_active()
                    cls.pool.submit(event.emit)

    #######################################
    # complete event loop and task runner #
    #######################################
    def finish_event_loop(self):
        self.run_loop_forever = False
        self.event_loop.join()

    ####################################
    # start event loop and task runner #
    ####################################
    def run_event_loop(self):
        self.run_loop_forever = True
        self.event_loop.start()


class NodePyExecutor(NodePy):
    def __new__(cls, func):
        cls.func = func
        return cls.__call__

    @classmethod
    def __call__(cls, *args, **kwargs):
        return super(NodePyExecutor, cls).exec(cls.func, args)
