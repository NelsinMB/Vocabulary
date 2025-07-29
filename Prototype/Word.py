class Word:
    def __init__(self, term, meanings, creation_date, last_reviewed_date, review_count):
        self.term = term
        self.meanings = meanings
        self.creation_date = creation_date
        self.last_reviewed_date = last_reviewed_date
        self.review_count = review_count
        
    def is_due_for_review(self):
        pass
    