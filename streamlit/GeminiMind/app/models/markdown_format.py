import re
import textwrap
import markdown


def to_markdown(text: str, indent_char="> ", indent_width=4) -> str:
    """Converts plain text to well-formatted Markdown with consistent indentation.

    Args:
        text (str): The plain text to be formatted.
        indent_char (str, optional): The character to use for indentation. Defaults to "> ".
        indent_width (int, optional): The number of spaces to use for each level of indentation. Defaults to 4.

    Returns:
        str: The formatted Markdown text.
    """

    # Replace bullet points efficiently using a regular expression
    text = re.sub(r"^\s*•", f"{indent_char} *", text, flags=re.MULTILINE)

    # Indent the entire text with consistent spacing
    indented_text = textwrap.indent(text, indent_char * indent_width, predicate=lambda _: True)

    # Convert the indented text to Markdown using the `markdown` library
    formatted_markdown = markdown.markdown(indented_text)

    return formatted_markdown

# Example usage
# text = """This is some plain text.

# * This is a bullet point.
# * This is another bullet point."""

# formatted_markdown = to_markdown(text)
# print(formatted_markdown)