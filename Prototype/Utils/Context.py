class Context:
    def __init__(self):
        self.current_deck_id = 1 # Not sure about this but whenever the context is initialized the parent is the master deck id
        self.deck_path = []
        
    def set_deck(self, deck_id, deck_name):
        self.current_deck_id = deck_id
        self.deck_path.append((deck_id, deck_name))
        
        
    def go_up(self):
        if self.deck_path:
            self.deck_path.pop()
            if self.deck_path:
                self.current_deck_id = self.deck_path[-1][0]
            else:
                self.current_deck_id = None
        
    
    def get_path_str(self):
        if not self.deck_path:
            return "root"
        return " > ".join(name for (_, name) in self.deck_path)