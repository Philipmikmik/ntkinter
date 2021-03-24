from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
import hentai

Builder.load_file('ntkinter-phyton.kv')
started=0
class MyLayout(Widget):
    def press(self):
        global comic, page, started
        started = 1
        comic = hentai.Utils.get_random_hentai()
        page = 0
        artist = [artist.name for artist in comic.artist]
        artist.append("Not defined")
        tag = [tag.name for tag in comic.tag]
        tags = ""
        tt = 0
        for i in range(len(tag) - 1):
            tags = tags + str(tag[i]) + ", "
            tt += 1
            if tt >= 6:
                tags = tags + "\n"
                tt = 0
        tags = tags[:-2]
        self.ids.title.text = "Title: "+comic.title(hentai.Format.Pretty)
        self.ids.author.text = "Author: "+artist[0]
        self.ids.page.text = "Pages: "+str(len(comic.image_urls))
        self.ids.tags.text = "Tags: "+tags
        self.ids.img.source = comic.image_urls[0]
    def pageplus(self):
        global page
        if started == 1:
            if (page<len(comic.image_urls)-1):
                page +=1
                self.ids.img.source = comic.image_urls[page]
    def pageminus(self):
        global page
        if started == 1:
            if page>0:
                page -=1
                self.ids.img.source = comic.image_urls[page]
    def copy(self):
        if started == 1:
            Clipboard.copy("nhentai.net/g/"+str(comic.id))
class MainApp(App):
    def build(self):
        return MyLayout()
if __name__ == '__main__':
    app = MainApp()
    app.run()