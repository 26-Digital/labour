import nltk


class Model_Trainer():
    def __init__(self) -> None:
        self.counter = 0
        self.is_last_lerui = False

    def regx_creator(self, tokens):
        """
        param: tokens
        param type: object, string
        return: chunk
        rtype: str
        """
        file = open("Leamanyi\\new_regs.txt", "w+")
        file.writelines("leamanyi : ")
        for sentence in tokens:
            tagged = self.pos_tag(nltk.word_tokenize(sentence))
            start = "{<"
            end = ">}"
            separator = "><"
            regularExp = []
            for tup in tagged:
                regularExp.append(tup[1])
            regularExp1 = separator.join(regularExp)
            regularExp1 = regularExp1.strip("<.>")
            reg = start + regularExp1 + end
            file.writelines('                '+reg + '\n')
            # print(reg)
        file.close()

    def regx_trainer(self, tree, chunk):
        """
        param: tree, chunk 
        param type: object, string
        return: chunk
        rtype: str
        """
        file = open("trained.txt", "w+")
        for subtree in tree.subtrees(filter=lambda t: t.label() == chunk):
            start = "{<"
            end = ">}"
            separator = "><"
            regularExp = []
            for tup in subtree.leaves():
                regularExp.append(tup[1])
                regularExp1 = separator.join(regularExp)
                reg = start + regularExp1 + end
                file.writelines('                '+reg + '\n')
                # print(reg)
            file.close()
