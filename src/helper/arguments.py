from __future__ import print_function
from xml.etree import ElementTree
from argparse import ArgumentParser


class Arguments(object):


    def __init__(self):
        self.arguments_dictiorary = None
        self.arguments_dictionary_list = None
        self.arguments_group = None
        self.arguments_list = None
        self.arguments_parser = None
        self.arguments_tree = None
        self.arguments_type = None
        self.id = None
        self.file = None
        self.program = None


    def get_argument_parser(self, file='../arguments.xml', id=None, program=None):
        self.file = file
        self.id = id
        self.arguments_tree = ElementTree.parse(self.file)
        self.arguments_dictionary_list = []
        for n, name in enumerate(self.arguments_tree.findall('name')):
            self.arguments_list = list(name)
            if self.id == dict(name.attrib).get('id'):
                if __debug__:
                    print('--- usage ---')
                    print('%s: %s' % (self.arguments_list[0].tag, self.arguments_list[0][0].text))
                self.argument_dictionary = {}
                self.argument_dictionary[self.arguments_list[0].tag] = self.arguments_list[0][0].text
                self.arguments_dictionary_list.append(self.argument_dictionary)
                self.arguments_parser = ArgumentParser(self.program,self.arguments_list[0][0].text)
                if __debug__:
                    for key, group in enumerate(self.arguments_list):
                        print('--- list group begin ---')
                        print(key, group, group.tag)
                        self.argument_dictionary = {}
                        for key, element in enumerate(group):
                            if element.tag == 'choices':
                                print(key, element, element.tag)
                                for key, choices in enumerate(element):
                                    print(key, choices, choices.tag, choices.text)
                            else:
                                print(key, element, element.tag, element.text)
                if __debug__:
                    print('--- list begin ---')
                i = 1
                while i < self.arguments_list.__len__():
                    if __debug__:
                        print('--- list group begin ---')
                    self.argument_dictionary = {}
                    j = 0
                    while j < list(name)[1].__len__():
                        if __debug__:
                            print(self.arguments_list[i].get('id'),
                                  self.arguments_list[i][j].tag, self.arguments_list[i][j].text)
                        if self.arguments_list[i][j].tag == 'choices':
                            choices_list = list()
                            for k, v in enumerate(self.arguments_list[i][j]):
                                if __debug__:
                                    print(k, v)
                                if str(v.text).isdigit():
                                    choices_list.append(int(v.text))
                                    self.arguments_type = int
                                else:
                                    choices_list.append(v.text)
                                    self.arguments_type = self.argument_dictionary.get('type')
                            self.argument_dictionary[self.arguments_list[i][j].tag] = choices_list
                        else:
                            self.argument_dictionary[self.arguments_list[i][j].tag] = self.arguments_list[i][j].text
                        j = j + 1
                    self.arguments_dictionary_list.append(self.argument_dictionary)
                    self.arguments_parser.add_argument(self.argument_dictionary.get('short'),
                                                       self.argument_dictionary.get('long'),
                                                       action = self.argument_dictionary.get('action'),
                                                       nargs = self.argument_dictionary.get('nargs'),
                                                       default = self.argument_dictionary.get('default'),
                                                       type = self.arguments_type,
                                                       choices = self.argument_dictionary.get('choices'),
                                                       required = self.argument_dictionary.get('required'),
                                                       help = self.argument_dictionary.get('help'),
                                                       metavar = self.argument_dictionary.get('metavar'),
                                                       dest = self.argument_dictionary.get('destination'))
                    i = i + 1
                    if __debug__:
                        print('--- list group end ---')
                if __debug__:
                    print('--- list end ---')
        return self.arguments_parser


    def get_dict_for_argument_parser(self, file='../arguments.xml', id=None, program=None):
        self.file = file
        self.id = id
        self.arguments_tree = ElementTree.parse(self.file)
        self.arguments_dictionary_list = []
        for name in self.arguments_tree.findall('name'):
            self.arguments_list = list(name)
            if self.id == dict(name.attrib).get('id'):
                print('--- usage ---')
                print('%s: %s' % (self.arguments_list[0].tag, self.arguments_list[0][0].text))
                self.argument_dictionary = {}
                self.argument_dictionary[self.arguments_list[0].tag] = self.arguments_list[0][0].text
                self.arguments_dictionary_list.append(self.argument_dictionary)
                print('--- list begin ---')
                i = 1
                while i < self.arguments_list.__len__():
                    self.argument_dictionary = {}
                    j = 0
                    print('--- list group begin ---')
                    while j < list(name)[1].__len__():
                        print(self.arguments_list[i].get('id'),
                              self.arguments_list[i][j].tag, self.arguments_list[i][j].text)
                        if self.arguments_list[i][j].tag == 'choices':
                            choices_list = list()
                            for k, v in enumerate(self.arguments_list[i][j]):
                                print(k, v)
                                if str(v.text).isdigit():
                                    choices_list.append(int(v.text))
                                    self.arguments_type = int
                                else:
                                    choices_list.append(v.text)
                                    self.arguments_type = self.argument_dictionary.get('type')
                            self.argument_dictionary[self.arguments_list[i][j].tag] = choices_list
                        else:
                            self.argument_dictionary[self.arguments_list[i][j].tag] = self.arguments_list[i][j].text
                        j = j + 1
                    self.arguments_dictionary_list.append(self.argument_dictionary)
                    i = i + 1
                    print('--- list group end ---')
                print('--- list end ---')
        return self.arguments_dictionary_list


    def show_content_of_file(self, file='../arguments.xml'):
        self.file = file
        self.arguments_tree = ElementTree.parse(self.file)
        for name in self.arguments_tree.findall('name'):
            arguments_list = list(name)
            print('%s: %s' % (self.arguments_tree.find('name').tag, dict(name.attrib).get('id')))
            print('%s: %s' % (arguments_list[0].tag, arguments_list[0][0].text))
            print('--- list begin ---')
            i = 1
            while i < arguments_list.__len__():
                print('--- list group begin ---')
                j = 0
                while j < list(name)[1].__len__():
                    print(arguments_list[i].get('id'), arguments_list[i][j].tag, arguments_list[i][j].text)
                    j = j + 1
                i = i + 1
                print('--- list group end ---')
            print('--- list end ---')
        print('')


if __name__ == '__main__':
    Arguments().show_content_of_file('../../docs/arguments.xml')
    Arguments().get_dict_for_argument_parser('../../docs/arguments.xml', 'wiki')

