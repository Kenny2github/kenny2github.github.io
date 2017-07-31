Python PPHP: Hypertext Preprocessor.

PPHP

This is a spinoff of PHP (PHP: Hypertext Preprocessor) that uses Python instead of the PHP language.

How to implement it into your server:
In your mess of import statements, add one more:
from pphp import do
Then, in your request handler, before you send the document:
html = do(html, GET_DATA, POST_DATA, **kwargs)
where html is the text of your html file, and GET_DATA and POST_DATA are dictionaries containing the GET and POST data respectively, and **kwargs is any arguments you need to pass to your scripts.

In an HTML file, to interpret Python code:
<p><?pphp print "Hello!" ?></p>
Anything between <?pphp and ?> will be executed - and the output given is any stdout written.
Some special things:
echo(text) - this is equivalent to sys.stdout.write(text)
__script__ - this is the entire script currently being executed
_GET - this is the GET_DATA you have passed
_POST - this is the POST_DATA you have passed
_EXTRAS - this is the **kwargs you have passed
