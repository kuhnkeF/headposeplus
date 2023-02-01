# Simple class to create tables for GitHub markdown
# https://github.com/kuhnkeF/headposeplus
import os

class Table():

    def __init__(self, header_row:list):
        self.header_row = header_row
        self.table_dict = {}
        for header in header_row:
            self.table_dict[header] = []

    def write_file(self, path):
        text = self.render(False)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        outfile = os.path.join(path, 'results.md')
        with open(outfile, 'w') as f:
            f.write(text)

    def add(self, di:dict):
        for key, value in di.items():
            if key not in self.table_dict:
                raise NameError('can not find ', key, ' in headings')
        for key in self.header_row:
            if key in di:
                self.table_dict[key].append(di[key])
            else:
                self.table_dict[key].append('/')

    def add_horizontal_line(self):
        for key in self.header_row:
            self.table_dict[key].append(' ')

    def render(self, print_out=True):
        text = '| '

        for heading in self.header_row:
            text += ' ' + heading + ' |'
        text += '\n|'
        for heading in self.header_row:
            text += ' :--- |'
        text += '\n'

        num_entries = len(self.table_dict[self.header_row[0]])

        for i in range(num_entries):
            text += '| '
            for heading in self.header_row:
                value = self.table_dict[heading][i]
                if isinstance(value, str):
                    text += ' ' + value + ' |'
                elif isinstance(value, float):
                    text += ' ' + "{:.2f}".format(value) + ' |'
                elif isinstance(value, int):
                    text += ' ' + str(value) + ' |'
                elif isinstance(value, bool):
                    raise NotImplementedError('todo use checks and crosses special chars')
                else:
                    raise NameError('unknown value type', value)
            text += '\n'

        if print_out:
            print(text)
        return text

    @staticmethod
    def yes():
        return '✔'

    @staticmethod
    def no():
        return '✖'

    @staticmethod
    def bool(b):
        if b:
            return Table.yes()
        else:
            return Table.no()
