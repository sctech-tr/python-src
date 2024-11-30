import re

def sdml2html(text):
    """sdml - sctech's dumb markup language"""
    # convert ==text== to <b>text</b>
    text = re.sub(r"==(.+?)==", r"<b>\1</b>", text)
    
    # convert ^^text^^ to <i>text</i>
    text = re.sub(r"\^\^(.+?)\^\^", r"<i>\1</i>", text)
    
    return text

# Example usage
example_text = """
==Bold Text==
^^Italic Text^^
"""
html_output = sdml2html(example_text)
print(html_output)
