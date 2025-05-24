class System:
    def __init__(self, component_manager):
        self.components = component_manager 

    def update(self, dt):
        raise NotImplementedError("System update method must be implemented in subclasses.")