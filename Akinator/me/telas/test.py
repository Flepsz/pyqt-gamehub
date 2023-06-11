def handle_yes(self):
    self.update_answer(Answer.Yes)


def handle_no(self):
    self.update_answer(Answer.No)


def handle_idk(self):
    self.update_answer(Answer.Idk)


def handle_ps(self):
    self.update_answer(Answer.Probably)


def handle_pn(self):
    self.update_answer(Answer.ProbablyNot)