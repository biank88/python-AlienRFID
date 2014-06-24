

__author__ = 'joesacher'

from alien_tag import AlienTag


class AlienTagList(list):
    """
    Holds list of tags
    """

    def __init__(self, taglist_string=""):
        list.__init__(self)
        if taglist_string:
            self.string_to_taglist(taglist_string)

    def string_to_taglist(self, taglist_string):
        lines = taglist_string.split('\r\n')

        for line in lines:
            if line != '(No Tags)':
                self.add_tag(AlienTag(line))

    def add_tag(self, t):
        self.append(t)

    def filter(self, filt_text):
        raise NotImplementedError('Not Implemented')