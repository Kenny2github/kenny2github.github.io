import re, lxml.html as lx, sys
from cStringIO import StringIO
def do(html, _GET={}, _POST={}):
    __scripts__ = re.findall(r'<\?pphp.*?\?>', html, re.DOTALL) #get all the scripts
    __outputs__ = range(0,len(__scripts__)) #generate dummy array for replacement purposes
    __dom__ = lx.fromstring(re.sub(r'<\?pphp.*?\?>', '<py></py>', html, flags=re.DOTALL)) #replace all <?pyhp?>s with an empty <py> tag for now
    for __script__ in __scripts__:
        __pre__ = sys.stdout
        sys.stdout = StringIO()
        echo = sys.stdout.write
        exec __script__[7:-2] #execute code (without the tag)
        html = lx.tostring(dom) #update DOM
        __output__ = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = __pre__
        __outputs__[__scripts__.index(__script__)] = __output__ #store the output
    for out in __outputs__:
        html = re.sub('<py></py>', out, html, count=1, flags=re.DOTALL) #replace each <py> tag with a script output
    return html
