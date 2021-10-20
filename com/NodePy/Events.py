class Event:
    def __init__(self, func, params):
        self.result = None
        self.func = func
        self.params = params
        self._callback = None
        self.is_set = False
        self.is_active = False

    def set_active(self):
        self.is_active = True

    def release(self):
        pass

    def emit(self):
        self.result = self.func(*self.params)
        self.is_set = True
        if self._callback is not None:
            self._callback(self.result)
        # self._thread.Event().set()

    def then(self, callback):
        self._callback = callback

    def resolve(self):
        return self.result
