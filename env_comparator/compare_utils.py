
class Operands:

    def __init__(self):
        pass

    def get_version_from_name(self, line):
        if "==" in line:
            return line.split('==')
        elif ">=" in line:
            return line.split('>=')
        elif ">" in line:
            return line.split('>')
        else:
            return [line]

    def get_version(self, line):
        if 'git+' in line or 'hg+' in line:
            return line.split('@')[-1].split('#')[0]
        else:
            d = self.get_version_from_name(line)
            if len(d) > 1:
                return d[1].split('#')[0].strip()
            else:
                return

    def get_package_name(self, line):
        if 'git+' in line or 'hg+' in line:
            return line.split('#egg=')[1]
        else:
            return self.get_version_from_name(line)[0].lower()

    def read_requirements(self, file_name):
        requirements = {}
        with open(file_name, 'r') as file:
            for line in file.readlines():
                if line.startswith('#'):
                    continue
                line = line.replace('\n', '')
                line = line.replace('\r', '')
                requirements[self.get_package_name(
                    line)] = self.get_version(line)
        return requirements
