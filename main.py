from typing import Dict
from markdown_splitter import MarkdownSplitter

if __name__ == "__main__":
    # read input from standard input
    input_text = ""
    while True:
        try:
            line = input()
            input_text += line + "\n"
        except EOFError:
            break

    # split markdown files
    splitter = MarkdownSplitter(input_text)
    files_dict = splitter.split_files()

    # write files to output directory
    output_dir = "./output"
    splitter.write_files(output_dir)
