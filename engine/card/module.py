from abc import *

class CardModule(metaclass=ABCMeta):
    def __init__(self):
        pass
    def __call__(self, *input, **kwargs):
        try:
            return self.recognize(*input, **kwargs)
        except:
            pass

    @abstractmethod
    def recognize(self, *input, **kwargs):
        pass

        








