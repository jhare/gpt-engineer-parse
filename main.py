import re
import os
import sys

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

def extract_readme(lines):
    # Iterate through lines to find the first triple backticks,
    # saving all the lines before it into new variable readme
    readme = ''
    readmeLines = []

    for i, line in enumerate(lines):
        if line.startswith('```'):
            lastLine = i
            readmeLines.pop()
            print(f'found last line of readme section at {lastLine}')
            break
        else: # having else here drops off the first line of next
            readmeLines.append(line)

    readme = '\n'.join(readmeLines)
    print(readme)
    return (readme, lastLine)


def main():
    destPath = 'output';
    # Define the multiline regular expression pattern
    pattern = r'(\w+)\.(\w+)\n```[a-z]+\n((?:.|\n)+?)\n```'

    # assume we're piped or redirected
    input_data = sys.stdin.read()
    lines = input_data.splitlines();

    (readme, lastLine) =  extract_readme(lines)

    linesWithBlocks = lines[lastLine-1:]
    concatenatedLines = '\n'.join(linesWithBlocks)

    print('lines with blocks')
    print(linesWithBlocks)

    # Find all matches using the pattern
    matches = re.findall(pattern, concatenatedLines, re.MULTILINE)

    if not matches:
        print('Warning: No matching gpt-engineer codeblocks found in input!')
        exit()

    # Create the "output" subdirectory if it doesn't exist
    if not os.path.exists(destPath):
        os.makedirs(destPath)

    # Iterate through the matches and create separate files
    for match in matches:
        filename, extension, file_contents = match
        output_file = os.path.join(destPath, f'{filename}.{extension}')
        with open(output_file, 'w') as file:
            file.write(file_contents)

    # write the readme file
    with open(f'{destPath}/README.md', 'w') as file:
        file.write(readme)


if __name__ == '__main__':
    main()
