 class CodeBuilder:
    indent_size = 2
    
    def __init__(self, root_name):
        self._root_name = root_name
        self._fields = []

    def add_field(self, type, name):
        self._fields.append((type, name))
        return self

    def __str__(self):
        # todo
        lines = []
        curr_indent = 0
        
        # Add class name
        idt = curr_indent * ' '
        lines.append(idt + "class " + self._root_name + ":")
        curr_indent += 2
        idt = curr_indent * ' '
        
        if len(self._fields) == 0:
            lines.append(idt + "pass")
        else:
            # Add classmethod
            lines.append(idt + "def __init__(self):")
            curr_indent += 2
            idt = curr_indent * ' '
            
            # Add class attributes
            for (type, name) in self._fields:
                lines.append(idt + "self." + str(type) + " = " + str(name))
                
        return '\n'.join(lines)


def main():
    cb = CodeBuilder('Person').add_field('name', '""') \
                          .add_field('age', '0')
    print(cb)


if __name__ == "__main__":
    main()