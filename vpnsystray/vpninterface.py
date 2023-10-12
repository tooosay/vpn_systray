import abc

class VPNClientInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def connect(self):
        raise NotImplementedError()
    
    @abc.abstractmethod
    def disconnect(self):
        raise NotImplementedError()
    
    @abc.abstractmethod
    def status(self):
        raise NotImplementedError()
    
    @abc.abstractmethod
    def connected(self):
        raise NotImplementedError()
    
    
