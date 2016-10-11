import requests
import re
from lxml import html
from lxml.cssselect import CSSSelector
from urllib.parse import urljoin

class Comic:
    #the CSS selector for the "next" link
    nextSelector=None
    #the CSS selector for the comic title
    titleSelector=None
    #the CSS selector for the comic img
    imgSelector=None
    #the CSS selector for supplemental text
    siteTitle=None
    #the default directory name to download into
    defaultDirname="comics"
    #the regex for matching the URL to the Comic
    urlRegex=".*"
    @classmethod
    def match(cls, url:str):
        """Returns whether this Comic class will work for the given URL"""
        return re.search(cls.urlRegex, url)

    def __init__(self, url:str):
        """Creates a Comic object, downloads and parses the comic page"""
        self.dom=html.fromstring(requests.get(url).text)
        self.url=url

    def _getAttr(self, selector:str, attr:str):
        """Return the value of the given attribute for the first element matching the given selector"""
        if not selector:
            return ""
        sel=CSSSelector(selector)
        attrs=sel(self.dom)[0].attrib
        if(attr in attrs):
            return attrs[attr]
        return ""

    def _getText(self, selector:str):
        """Return the text of the first element matching the given selector"""
        if not selector:
            return ""
        sel=CSSSelector(selector)
        return sel(self.dom)[0].text or ""

    def getNumber(self):
        """Return the page number"""
        return 0

    def getTitle(self):
        """Return the title of this comic"""
        return self._getText(self.titleSelector)

    def getImg(self):
        """Return the image URL for this page"""
        return urljoin(
                self.url,
                self._getAttr(self.imgSelector, "src")
                )

    def getImgExtension(self):
        """Return the filename extension for the image"""
        return re.search(r'\.([a-zA-Z]+)$', self.getImg()).group(1)

    def getImgFile(self):
        """Return the filename to save the image as"""
        parts=[str(self.getNumber()).zfill(6)]
        if(self.getTitle()):
            parts.append(self.getTitle())
        return (" - ".join(parts)) + "." + self.getImgExtension()

    def getAlt(self):
        """Return the alt text for this comic"""
        return self._getAttr(self.imgSelector, "alt")

    def getNext(self):
        """Return the URL of the next page if there is one, or False otherwise"""
        return urljoin(
                self.url,
                self.getAttr(self.nextSelector, "href")
                )

    def toDict(self):
        """Returns a dict with all the important stuff"""
        return {
                "number": self.getNumber(),
                "title": self.getTitle(),
                "url": self.url,
                "imgurl": self.getImg(),
                "imgfile": self.getImgFile(),
                "alt": self.getAlt()
                }
