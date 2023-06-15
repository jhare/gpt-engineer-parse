import os
import re
from typing import Dict

class MarkdownSplitter:
    def __init__(self, input_text: str):
        self.input_text = input_text

    def split_files(self) -> Dict[str, str]:
        files_dict = {}
        lines = self.input_text.split("\n")
        current_filename = "README.md"
        opened = False
        current_file_contents = ""
        for i, line in enumerate(lines):
            if line.startswith("```"):
                opened = not opened

                if current_file_contents:
                    files_dict[current_filename] = current_file_contents
                    current_file_contents = ""

                # If ChatGPT is being fancy it says Your file: `file.py`
                # other times it's on the line ending with :
                # this is scratch work for now so we're seeing all the possibilities still
                if opened:
                    foundMatch = re.search("`(.*)`", lines[i-1])
                    if foundMatch:
                        current_filename = foundMatch.group(1)
                    else:
                        current_filename = lines[i-1].strip().replace(":", "")

                continue
            current_file_contents += line + "\n"
        if current_file_contents:
            files_dict[current_filename] = current_file_contents
        return files_dict

    def write_files(self, output_dir: str) -> None:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        for filename, contents in self.split_files().items():
            with open(os.path.join(output_dir, filename), "w") as f:
                f.write(contents)
