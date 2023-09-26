def format_string(string, formatter=None):
    """Formata uma string usando o objeto formatter, que
    espera ter um método format() que aceite uma string."""
 
    class DefaultFormatter:
        """Formata uma string em maiúsculas."""
 
        def format(self, string):
            return str(string).title()
 
    if not formatter:
        formatter = DefaultFormatter()
 
    return formatter.format(string)
 
hello_string = "hello world, how are you today?"
print(" input: " + hello_string)
print("output: " + format_string(hello_string))