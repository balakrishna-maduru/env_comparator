import os
from env_comparator.compare_utils import Operands


class Compare(Operands):

    def __init__(self, input1: str, input2: str):
        super().__init__()
        self.status = []
        self._compare(input1, input2)

    def get_results(self):
        return self.status

    def _is_subset(self):
        for key, value in self._differ.items():
            if value[self.title2] == "Missing":
                return False
        return True

    def get_status(self):
        line = "-"*111
        for files_status in self.status:
            print(line)
            print(
                f"|file1 :{files_status['file']:30}|file2 :{files_status['compared_file']:30}| is subset :{str(files_status['is_subset']):21}|")
            print(line)
            print(
                f"|{'Package':^30}|{self.title1:^30}|{self.title2:^30}|{'Status':^16}|")
            print(line)
            for key, value in files_status["libraries"].items():
                print(
                    f"|{key:30}|{value.get(self.title1,''):30}|{value.get(self.title2,''):30}|{value.get('status',''):16}|")
            print(line)

    def _insert(self, requirements, title):
        for key, value in requirements.items():
            if key not in self._differ:
                self._differ[key] = {}
            self._differ[key][title] = value

    def _update_status_on_both(self, key, value):
        if value[self.title1] == value[self.title2]:
            self._differ[key]["status"] = 'OK'
        else:
            self._differ[key]["status"] = 'Version Mismatch'

    def _update_status_on_title(self, key, title):
        self._differ[key][title] = 'Missing'
        self._differ[key]["status"] = 'Not OK'

    def _update_status(self, key, value):
        if self.title1 in value and self.title2 in value:
            self._update_status_on_both(key, value)
        elif self.title1 not in value:
            self._update_status_on_title(key, self.title1)
        else:
            self._update_status_on_title(key, self.title2)

    def _read_files_and_set_titles(self, file1, file2):
        self.requirements1 = self.read_requirements(file1)
        self.requirements2 = self.read_requirements(file2)
        self.title1 = os.path.basename(file1)
        self.title2 = os.path.basename(file2)

    def _do_compare(self, file1, file2):
        self._differ = {}
        self._read_files_and_set_titles(file1, file2)
        self._insert(self.requirements1, self.title1)
        self._insert(self.requirements2, self.title2)
        for key, value in self._differ.items():
            self._update_status(key, value)
        self.status.append({"is_subset": self._is_subset(),
                            "file": self.title1,
                            "compared_file": self.title2,
                            "libraries": self._differ})

    def _compare(self, input1, input2):
        if os.path.isdir(input2):
            for folder, sub_folder, files in os.walk(input2):
                for file in files:
                    self._do_compare(input1, os.path.join(folder, file))
        else:
            self._do_compare(input1, input2)
