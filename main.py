import re
import os
import sys

#################################################################
# This script takes a markdown file with code blocks and
# creates separate files for each code block.

# The script also takes the first section of the markdown file
# and creates a README.md file in the output directory.

# The script assumes that the first code block is the README.md
# file and that the README.md file is the first section of the
# markdown file.

# The script assumes that the code blocks are in the format:
# ```<language>
# ```
# <code>
# ```
# ```
# <language> is the language of the code block, and <code> is
# the code itself.

# The script assumes that the markdown file is in the format:
# <README.md>
# <code block>
##################################################################


def extract_readme(lines):
    """
    Extract the first section of the markdown file as the README.md file

    :param lines: list of lin^es from the markdown file
    :return a tuple of the README.md file and the line number of the last line
            of the README.md file
    :rtype tuple
    """

    # Iterate through lines to find the first triple backticks,
    # saving all the lines before it into new variable readme
    readme = ""
    readme_lines = []

    for i, line in enumerate(lines):
        if line.startswith("```"):
            lastLine = i
            readme_lines.pop()
            break
        else: 
            readme_lines.append(line)

    readme = "\n".join(readme_lines)
    return (readme, lastLine)


def main():
    destPath = "output"
    # Define the multiline regular expression pattern
    pattern = r"(\w+)\.(\w+)(?:.{1}\:)?\n```[a-z]+\n((?:.|\n)+?)\n```"

    # assume we're piped or redirected
    input_data = sys.stdin.read()
    lines = input_data.splitlines()

    (readme, lastLine) = extract_readme(lines)

    lines_with_blocks = lines[lastLine - 1 :]
    files_after_readme = "\n".join(lines_with_blocks)

    # Find all matches using the pattern
    matches = re.findall(pattern, files_after_readme, re.MULTILINE)

    if not matches:
        print("Warning: No matching gpt-engineer codeblocks found in input!")
        exit()

    # Create the "output" subdirectory if it doesn't exist
    if not os.path.exists(destPath):
        os.makedirs(destPath)

    # Iterate through the matches and create separate files
    for match in matches:
        filename, extension, file_contents = match
        output_file = os.path.join(destPath, f"{filename}.{extension}")
        with open(output_file, "w") as file:
            file.write(file_contents)

    # write the readme file
    with open(f"{destPath}/README.md", "w") as file:
        file.write(readme)


if __name__ == "__main__":
    main()
