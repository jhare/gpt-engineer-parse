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
        current_file_contents = ""
        for i, line in enumerate(lines):
            if line.startswith("```"):
                if current_file_contents:
                    files_dict[current_filename] = current_file_contents
                    current_file_contents = ""
                filenameMatch =  re.search(r"file: `(.*)`", lines[i - 1])
                current_filename = filenameMatch.group(1) if filenameMatch else "unknown"
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
