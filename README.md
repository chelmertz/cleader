# cleader - CLI READER

Store web articles as plain text. No more 'saved as' HTML (aka cURL:d) or
'printed as PDF', just extracted content in markdown, without all annoying markup.


## FEATURES
### Uses STDOUT, easy to process further:
`python cleader.py http://iamnearlythere.com/what_i_want_from_an_api/ | wc -c`

### Save to file:
`python cleader.py --save http://iamnearlythere.com/what_i_want_from_an_api/`

creates the file 'what_i_want_from_an_interface.md'

### Extract *only* the article's HTML:
`python cleader.py http://iamnearlythere.com/what_i_want_from_an_api/ | markdown_py > what_i_want_from_an_api.html`

This example requires 'pip install markdown' and is almost what html2text
does, but, again, cutting away all the cruft that's not the main article's content.

### Very create-your-own-library friendly, subjective example coming up:
`echo 'function save() { python cleader.py "$1" --save=~/favorites }' >> ~/.bashrc && . ~/bashrc`

After that setup, this CLI call:

`save http://iamnearlythere.com/what_i_want_from_an_api/`

would create *~/favorites/what_i_want_from_an_interface.md* for you
to keep around forever and ever.

### ... which could easily be turned to a nice UNIX:y archive system:
 - listing the latest 'favorites': `ls -t1 ~/favorites | head -n 5`
 - weighted search for 'css': `grep -ic css ~/favorites/* | head -n 5`
 - showing extracts: `head -n 10 ~/favorites/* | less`


## DEPENDENCIES
 - pip install -r requirements.txt
 - A (free) Readability API key, from [http://www.readability.com/developers/api/parser](http://www.readability.com/developers/api/parser)


## QUESTIONS
Read or post issues at [https://github.com/chelmertz/cleader](https://github.com/chelmertz/cleader)

Email [helmertz@gmail.com](helmertz@gmail.com)
