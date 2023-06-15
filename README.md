# gpteng-output-breakout
Separate the files from [gpt-engineer] output.

It creates the following structure

```
$> tree output
output
├── hello.js
├── index.html
└── README.md
```

from this prompt's [https://github.com/jhare/gpt-engineer](gpt-engineer) output

```
write a jquery based html5 web page that produces the output of fizzbuzz.
perform the javascript in a separate file included by the index.
calculate fizzbuzz from 100
do so on a button click
externally link jquery from a cdn
from this output of the bot
```

So now you have code in files.

Some file names come with extra decoration: "Markdown splitter file: `markdown_splitter.py`"

It still just pulls the filename based on where ticks are, but you never know. GPT output can vary.
