# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:45:58 2019

@author: Bopaki Tebalo

Chunks: 'lerui' in a sentence.
        'letlhaodi' in a sentence.
        'lebadi' in a sentence.
        'leemedi' in a sentence.
        'leamanyi' in a sentence.
        'lesupi' in a sentence.
        'letlhalosi' in a sentence.
Dikarolo tsa puo:
    leina(noun)
    leemedi(pronoun)
    lediri(verb)
    ditlhaodi(qualificatives):
        lesupi(demostrative) e.g  Go nole kgomo ele fela-'ele' ke lesupi(a mangwe ke bo 'e' 'eo') o othe a supa gore selo se go buiwang ka sone 
        lebadi(enumerative)  e.g  Go nole kgomo ele nngwefela-'nngwe' ke lebadi
        letlhaodi(adjective) e.g Monna yo moleele o lobelo.
"""
import nltk
import time
from nltk.chunk import RegexpParser
from nltk import Tree
import os
from django.conf import settings
import json

class Setswana_Nltk():
    def __init__(self):
        self.counter = 0
        self.is_last_lerui = False

    def tagger(self, dic0, key):
        """
        @descrption :: Returns the value of the given key from the dictionary.
                       The value is the Part of speech tag and the given key is
                       the word i.e. 'Monna'
                       If key(word) does not exist in the dictionary it is 
                       analyzed to determine its part of speech tag. Proper
                       nouns are identified by uppercazed first letter. Adjectives
                       are further divided into subclasses i.e ADJ1 prefix is 'mo' 
                       and ADJ2 prefix is 'ba'
        @inputs:
            @dic0 :: A Dictionary containing a list of tagged strings.
            @key: A search key
        @output ::
            @tag :: Returns part of speech tag, otherwise returns 'XX'(none)
        """
        dic = {'mo': 'ADJ1',
               'ba': 'ADJ2',
               'me': 'ADJ3',
               'le': 'ADJ4',
               'ma': 'ADJ5',
               'se': 'ADJ6',
               'lo': 'ADJ7',
               'bo': 'ADJ8',
               'go': 'ADJ9',
               'di': 'ADJ9'}
        if(key == '.' or key == ','):
            return key
        # print(key)
        elif(key.lower() in dic0):
            # print(key)
            if(dic0[key.lower()] == 'ADJ'):
                if(key[:2] in dic and len(key) > 2):
                    return dic[key.lower()[:2]]
                else:
                    return dic0[key.lower()]
            elif(dic0[key.lower()] == 'VRB'):
                if(key[len(key)-2:] == 'ng'):
                    return 'VRB_ng'
                else:
                    return 'VRB'
            return dic0[key.lower()]
        # check if the vrb with ng exists in the corpus by removing the 'ng'.
        elif(key[:-2] in dic0 or key.lower()[:-2] in dic0):
            # print(key.lower()[:-2])
            if(dic0[key.lower()[:-2]] == 'VRB'):
                return 'VRB_ng'
            elif(dic0[key.lower()[:-2]] == 'NN'):
                return 'NN'
        elif(key[:1].isupper()):
            return 'NN'
        elif(key[:4] == 'goo-' or key[:8] == 'goo-rra-'):
            return 'EE1'
        else:
            return 'XX'

    def word_net_lemmatiser(self, word):
        """
        Transforms a word to its root form and returns an array of possible roots,
            1. Checks for repititions i.e. lesweusweu >> sweu.
            2. Determine the class of the word i.e. Verb, Noun, Adjective, Adverb.
        """
        substlist = []
        """Extract a list of substrings from a word, from left to right and from right to left."""
        for i in range(len(word)):
            if(len(word[:i+1]) > 1):
                substlist.append(word[:i+1])
        for i in range(len(word)):
            if(len(word[i+1:]) > 1):
                substlist.append(word[i+1:])

        """Check for repititions."""
        for substr in substlist:
            count = word.count(substr)
            if(count > 1 and len(substr) > 3):
                rep = substr+substr
                if(rep in word):
                    print(substr+'-'+word)
                    # f.writelines(substr+'-'+word+ '\n') # write new lines
                    return substr
                else:
                    return 'XX'

    def create_dictionary(self):
        """
        @description :: Create a dictionary data structure
        @input :: setswana_copus.txt file
        @output :: {'Monna':'NN','Lela':'VRB'}
        """
        dic = {}
        file_path = os.path.join(settings.BASE_DIR, 'sesigo\\assets', 'corpus_v3.txt')
        with open(file_path, "r+") as input_file:
            lines = input_file.readlines()
            for line in lines:
                dic.update(self.array_to_dictionary(
                    self.text_to_array((line.strip("\n")).strip())))
        return dic

    def text_to_array(self, line):
        """
        @description :: Split a line from a text file into tokens, whenever 
                        there is a fullstop/period.
        @input :: text(string)
        @output :: array of words
        """
        return line.split('.')

    def array_to_dictionary(self, array):
        """
        @description :: Create a hashMap given a arr, use the value at index 
                        0(zero) as the tag value and the following array values 
                        as the keys.
        @input:
            @array: list of strings. i.e.['NN',legapu', 'lesole', 'lesedi', 'letagwa']
        @output::
            @dic :: corpus 
                        @Description :: Dictionary implementation
                                        @key :: word(pro)
                                                @datatype :: string
                                        @value :: part of speech tag(index zero of the array) i.e. 'NN'
                                                  @datatype :: string 
                        @Example :: dic = {'legapu':'NN', 'lesole':'NN','lesedi':'NN','letagwa':'NN'}
        """
        return {i: array[0] for i in array[1:]}

    def get_word(self, line):
        """
        Split a line from a text file into tokens, whenever there is a fullstop/period.
        """
        return line.split('.')

    def part_of_speech_tagger(self, sentence):
        """
        @description :: Calls the tagger()
                        Tags words in a sentence. 
        @input :: @words :: Sequence of tokens to be tagged 
                             @datatype :: list(str)
        @tagset :: the tagset to be used
                   @datatype :: str
        @output: The tagged tokens
                 @datatype: list(tuple(str, str))
                 @Description :: Creates a list of tuples 
                 i.e. [('Monna','NN'),('elama','VRB'),('montsho','ADJ')]
        """

        dic = self.create_dictionary()
        tagged = []  # declare tagged list
        lerui_concords = ['ya', 'wa', 'la',
                          'tsa', 'sa', 'ba', 'jwa', 'ga', 'a']
        for i, word in enumerate(sentence):
            if(word in lerui_concords):
                self.lerui_cc_counter(
                    self.counter, word, dic, tagged, self.is_last_lerui, sentence[i+1])
                self.is_last_lerui = True
            else:
                # update the list.
                tagged.append(tuple([word, self.tagger(dic, word)]))
                self.is_last_lerui = False
        # print(tagged)
        return tagged

    def lerui_cc_counter(self, counter, word, dic, tagged, is_last_lerui, next_word):
        """
        @description :: 
        @Input variables :: counter :: int :: count the number of lerui concords in a sentence.
                            word :: string :: a word from a sentence
                            dic :: dictionary :: a hashmap of parts of speech tags
                            tagged :: array :: 
                            is_last_lerui :: boolean
                            next_word :: string ::
        @Output :: counter :: int ::
        """
        if(self.is_last_lerui == True):
            if(self.tagger(dic, next_word) == 'NN'):
                tagged.append(
                    tuple([word, self.tagger(dic, word)+'_'+str(counter)]))
                self.counter += 1
            else:
                tagged.append(
                    tuple([word, self.tagger(dic, word)+'_'+str(counter-1)]))
                self.counter = counter
        elif(self.counter > 0):
            tagged.append(
                tuple([word, self.tagger(dic, word)+'_'+str(counter)]))
            self.counter += 1
        else:
            tagged.append(
                tuple([word, self.tagger(dic, word)+'_'+str(counter)]))
            self.counter += 1

    def untagged(self, tagged):
        """
        Return a list of untagged words.
        param: List of tuples(string, string).
        param type: array of objects.
        return: untagged tuples(string,'XX').
        return type: List of tuples.
        """
        file = open("assets\\untagged.txt", "a+")
        for tup in tagged:
            if(tup[1] == "XX"):
                print(tup[0] + " "+tup[1])
                file.writelines(tup[0] + "\n")

    def generator(self, tokens):
        """
        Perform language analysis.
        param tokens: sentence tokens in an array.
        param type: array of string.
        return: chunk.
        return type: object.
        """
        #print("Here:")
        #print(settings.BASE_DIR)
        file_path = os.path.join(settings.BASE_DIR, 'sesigo\\assets', 'regs3.txt')
        text2 = open(file_path, "rb")
  
        chunkGram = text2.read().decode("utf8", "ignore")
        text2.close()
        file_path1 = os.path.join(settings.BASE_DIR, 'sesigo\\assets', 'chunked.txt')
        f = open(file_path1, "w+")
        for sentence in tokens:
            tokenized = nltk.word_tokenize(sentence)
            self.counter = 0
            self.is_last_lerui = False
            tagged = self.part_of_speech_tagger(tokenized)
            # print(tagged)
            chunkParser = nltk.RegexpParser(chunkGram)
     
            tree = chunkParser.parse(tagged)
            f.writelines(str(tree))
        f.close()
        json_str = self.tuple_to_json(tree)
        #json_str = json.dumps(json_str,ensure_ascii=False, indent=2, separators=(',',':'))
        json_str = json.dumps(json_str, separators=(',',':'))
        return json_str

    def sanitize_input(self, input_data):
        #print(input_data)
        sanitized_data = input_data.replace('\n','')
        #print(sanitized_data)
        return sanitized_data
    def tuple_to_json(self, input_structure):
        # Initialize a dictionary to hold the parsed structure
        parsed_structure = {}

        # Split the input structure by spaces
        stringfy = str(input_structure)
        sanitized = self.sanitize_input(stringfy)
        elements = sanitized.split()

        # Start parsing
        current_dict = parsed_structure  # The current dictionary
        stack = []  # A stack to keep track of nested dictionaries

        for element in elements:
            while element.endswith(')'):
                element = element[:-1]  # Remove the trailing ')'

            if '/' in element:
                value, key  = element.split('/')
                current_dict[key] = value

            elif '(' in element:
                key = element.strip('()')
                current_dict[key] = {}
                stack.append(current_dict)  # Push the current_dict onto the stack
                current_dict = current_dict[key]  # Set the current_dict to the new nested dictionary

            elif ')' in element:
                current_dict = stack.pop()  # Pop the previous dictionary from the stack

        return parsed_structure

    def display_chunks(self, tree, chunk):
        """
        Display to thescreen and Write the chunks to the text file.
        param: tree, chunk 
        param type: object, string
        return: chunk
        rtype: str
        """
        #open("C:\\Users\\Bopaki\\Desktop\\all_test_results.txt", 'w').close()
        f1 = open("all_test_results.txt", "a+")
        for subtree in tree.subtrees(filter=lambda t: t.label() == chunk):
            chunked = ""
            for tup in subtree.leaves():
                chunked += tup[0]+" "
            print(chunked + ">>> "+chunk)
            #f1.writelines(chunked +">>> "+chunk+ '\n')
        f1.close()
