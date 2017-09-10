Python PPHP: Hypertext Preprocessor.

PPHP

This is a spinoff of PHP (PHP: Hypertext Preprocessor) that uses Python instead of the PHP language.

How to use it:

To host the server, simply run ``python -m PPHPServer``

To execute Python code inside a file, use:

``<?pphp #code here (line breaks permitted) ?>``

and output will be recorded in the same way as PHP - through stdout.

Example:

``<p>Request method: <?pphp echo(_SERVER['REQUEST_METHOD']) ?></p>``

Some special globals:

* ``echo(text)`` - this is equivalent to sys.stdout.write(text)
* ``__script__`` - this is the entire script currently being executed
* ``__db__`` - this is the server's database, more documentation below
* ``_GET`` - this is the GET data as a dictionary
* ``_POST`` - this is the POST data as a dictionary
* ``_REQUEST`` - this is a combination of _GET and _POST
* ``_SERVER`` - this is the equivalent of PHP's $_SERVER, with some exceptions described below.

In _SERVER, the keys ``REQUEST_TIME, HTTP_ACCEPT, HTTP_ACCEPT_CHARSET, HTTP_HOST, HTTP_REFERER, HTTPS, REMOTE_HOST, SERVER_ADMIN, SERVER_SIGNATURE, SCRIPT_NAME, and SCRIPT_URI`` are all not available; and the key ``GATEWAY_INTERFACE`` returns the version of the ``cgi`` module, not the gateway interface.

Data for a server can be stored using the global ``__db__``. This is simply a dictionary - you can store and retrieve values as such. Data in ``__db__`` is stored as JSON in the file ``__DATABASE__.json``, under ``~/.pphp`` on Mac or Linux or ``%appdata%/.pphp`` on Windows. Changes to ``__db__`` will only show up in ``__DATABASE__.json`` after all scripts have finished running. **WARNING**: Moving the file will reset that script's data!

Thanks to:

* `banana439monkey <https://github.com/banana439monkey>`_ for help in thinking of the name.
* `StackOverflow <https://stackoverflow.com>`_ for help with the many problems I experienced.
* `Python <https://python.org>`_ (duh) for having such awesome batteries included.
