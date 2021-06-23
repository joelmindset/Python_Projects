import webbrowser
import webGenGUI


def Webpage(self):
    #open html in web browser
    url = 'deals.html'
    webbrowser.open_new(url)

def webpageWrite(self):
    #get entry variable
    self.var2= self.entry.get()
    #rewrite the web page
    self.f = open("deals.html", "w")
    self.f.write("""<html>
        <body>
            <h1>
            {}
            </h1>
        </body>
    </html>""".format(self.var2))
    self.f.close()

   

if __name__ == '__main__':
    pass
