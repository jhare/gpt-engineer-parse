# gpteng-engineer-parse

Separate the files from this prompt's [https://github.com/AntonOsika/gpt-engineer](gpt-engineer) output

## usage 
Invoke main.py and it will parse what is on standard in

`python main.py < gpt-fizzbuzz-overkill-output.md`

It produces files in `./output/`

_Note: do your best in your prompt to encourage the filenames to be on lines by themselves. Adding more parsing options
but for now the multiline regex is simple_

__Note:Get clean filenames your prompt with this help: (it's not perfect)__
```
List filename for each block by themselves on a line before the block.
Do not describe anything after the last code block.
Do not label the file name of each file in the project.
```

## output
```
$ tree output
output
├── App.js
├── Auth0Login.js
├── Button.js
├── fizzbuzz_lambda.py
├── Highlight.js
├── README.md
└── server.js

1 directory, 7 files
```


### explanation

a prompt for an overkill version of fizzbuzz:
```
write a version of fizz buzz with a react front end, using auth0 for a login.

The react application is created by create-react-app

The main view of the application contacts a lambda function to get the full fizzbuzz output string and display it in a Highlight component.

Write a lambda funtion in Python that counts Fizzbuzz from 1 to n where n is passed to the lamda function

write an ExpressJS server that offers a REST endpoint that when contacted starts the fizzbuzz lambda

The React application includes a button that contacts the rest API on Click.

List filename for each block by themselves on a line before the block.
Do not describe anything after the last code block.
Do not label the file name of each file in the project.
```

It creates the following structure in the markdown, with a preamble w clarifications
that `gpt-engineer` asks, this parses through all of that, generates a README.md

```

Core classes, functions, and methods:
- Lambda function: `fizzbuzz_lambda` - counts Fizzbuzz from 1 to n where n is passed to the lambda function
- ExpressJS server: `server` - offers a REST endpoint that when contacted starts the fizzbuzz lambda
- React application: `App` - main view of the application that contacts the lambda function to get the full fizzbuzz output string and display it in a Highlight component
- Highlight component: `Highlight` - displays the full fizzbuzz output string
- Button component: `Button` - contacts the REST API on click
- Auth0 login component: `Auth0Login` - handles user authentication using Auth0

fizzbuzz_lambda.py
[backticks here Due to Markdown limitations the full output of gpt-engineer we have to omit. Three backticks begin and the file contents proceed]

server.js
[backticksgohere]javascript
const express = require('express');
const app = express();
const aws = require('aws-sdk');

```
So now you have code in files:

```
$ tree output
output
├── App.js
├── Auth0Login.js
├── Button.js
├── fizzbuzz_lambda.py
├── Highlight.js
├── README.md
└── server.js
```

### caveats - other formats
Anything but labeling the filename on its own line right now breaks it.
I prefer to suppress the descriptions with prompt shaping, we don't need them on those lines
we are the ones that supplied the descriptions in the first place.

```
Lambda function in Python (fizzbuzz.py):
[block would be here, but this has extra stuff sometimes, sometimes quoted, sometimes not
[sometimes they make mistakes, you need to shape the prompt so that the filename is by itself]
Some file names come with extra decoration: "some desciprtio: : `markdown_splitter.py`"
```



