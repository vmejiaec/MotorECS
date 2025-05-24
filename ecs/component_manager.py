class ComponentManager:
    def __init__(self):
        # Dictionary to hold components by type
        # Example: {
        #           Position: {entity_id: Position_instance}, 
        #           Velocity: {entity_id: Velocity_instance}
        #         }
        self.components = {} 
        
    def add_component(self, entity_id, component):
        component_type = type(component)
        if component_type not in self.components:
            self.components[component_type] = {}
        self.components[component_type][entity_id] = component
    
    def get_component(self, entity_id, component_type):
        if component_type in self.components:
            return self.components[component_type].get(entity_id, None)
        return None
    
    def remove_component(self, entity_id, component_type):
        if component_type in self.components:
            if entity_id in self.components[component_type]:
                del self.components[component_type][entity_id]
                return True
        return False
    
    # Retrieve all entities with all of component types
    def get_entities_ids_with(self, *component_types):
        if not component_types:
            return []
        
        entities_ids = set(self.components.get(component_types[0], {}).keys())

        for component_type in component_types[1:]:
            entities_ids &= set(self.components.get(component_type, {}).keys())

        return list(entities_ids)

    def get_components_for(self, entity_id):
        return {
            ctype: comps[entity_id] 
            for ctype, comps in self.components.items() 
            if entity_id in comps
        }