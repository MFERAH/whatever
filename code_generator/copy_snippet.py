class copy:
    def __init__(self, code):
        self.code = code

    def copy_code(self, file_name, *args):
        dir = './snippets/{}'.format(file_name)
        with open(dir) as s:
            text = s.read().format(*args)
            self.code.seek(0, 2)
            self.code.write(text)
            self.code.writelines("\n")

    @staticmethod
    def read_code(file_name, *args):
        dir = './snippets/{}'.format(file_name)
        with open(dir) as s:
            text = s.read().format(*args)
        return text
