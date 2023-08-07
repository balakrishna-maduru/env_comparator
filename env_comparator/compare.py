import os
from env_comparator.compare_utils import Operands


class Compare(Operands):

    def __init__(self, input1: str, input2: str, title1: str = None, title2: str = None):
        super().__init__()
        self.requirements1 = self.read_requirements(input1)
        self.requirements2 = self.read_requirements(input2)
        self.title1 = title1 if title1 else os.path.basename(input1)
        self.title2 = title2 if title2 else os.path.basename(input2)
        self.status = {}
        self._compare()

    def get_results(self):
        return self.status

    def get_status(self):
        line = "-"*101
        print(line)
        print(f"|{'Package':^30}|{self.title1:^25}|{self.title2:^25}|{'Status':^16}|")
        print(line)
        for key, value in self.status.items():
            print(
                f"|{key:30}|{value.get(self.title1,''):25}|{value.get(self.title2,''):25}|{value.get('status',''):16}|")
        print(line)

    def _insert(self, requirements, title):
        for key, value in requirements.items():
            if key not in self.status:
                self.status[key] = {}
            self.status[key][title] = value

    def _update_status_ob_both(self, key, value):
        if value[self.title1] == value[self.title2]:
            self.status[key]["status"] = 'OK'
        else:
            self.status[key]["status"] = 'Version Mismatch'

    def _update_status_on_title(self, key, title):
        self.status[key][title] = 'Missing'
        self.status[key]["status"] = 'Not OK'

    def _update_status(self, key, value):
        if self.title1 in value and self.title2 in value:
            self._update_status_ob_both(key, value)
        elif self.title1 not in value:
            self._update_status_on_title(key, self.title1)
        else:
            self._update_status_on_title(key, self.title2)

    def _compare(self):
        self._insert(self.requirements1, self.title1)
        self._insert(self.requirements2, self.title2)
        for key, value in self.status.items():
            self._update_status(key, value)

    def is_subset(self):
        for key, value in self.status.items():
            if value[self.title1] == "Missing":
                return False
        return True
