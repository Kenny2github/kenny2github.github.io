import re, lxml.html as lx, sys
from cStringIO import StringIO
def do(html, _GET={}, _POST={}, **_EXTRAS):
    __scripts__ = re.findall(r'<\?pphp.*?\?>', html, re.DOTALL) #get all the scripts
    __outputs__ = [] #outputs
    for __script__ in __scripts__:
        __pre__ = sys.stdout #backup of sys.stdout so that we can restore it later
        sys.stdout = StringIO()
        echo = sys.stdout.write
        exec __script__[7:-2] #execute code (without the tag)
        __output__ = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = __pre__
        __outputs__.append(__output__) #store the output
    for out in __outputs__:
        html = re.sub(r'<\?pphp.*?\?>', str(out), html, count=1, flags=re.DOTALL) #replace each script with its output
    return html
