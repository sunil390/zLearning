# Snippets


## Download files from url
```
import urllib2
import string

print "let's download all the GSEUK21 slides we can..."
#for i in string.digits:
for i in ['1','2','3','4','5','6']:
    for a in ['A','B','C']:
        for b in string.ascii_uppercase:
            for ext in ['pdf', 'ppt', 'pptx', 'doc']:
                deck = "%s%s%s.%s" % (i,a,b,ext)
                url = "http://conferences.gse.org.uk/2021/presentations/%s" % deck
                print "Trying to get %s" % url,
                status = "ok"
                try:
                    coolslidesdata = urllib2.urlopen(url)
                except:
                    status = "meh"
                    print " Meh"
                if status == "ok":
                    print " Gotcha!"
                    coolslides = coolslidesdata.read()
                    with open(deck, 'wb') as slidedeck:
                        slidedeck.write(coolslides)
```
