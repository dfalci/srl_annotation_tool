# -*- coding: utf-8; -*-
from utils import Singleton
from sentenca import SRLParser
from dotmap import DotMap
import random



@Singleton
class SentenceDatabase(object):

    def __init__(self):
        self.parser = SRLParser()
        self.target = [
            u'Durante sua vida, Albert Einstein publicou centenas de livros e artigos.',
            u'Naquele momento, o sistema estava apto a registrar todas as transações',
            u'Não é fácil registrar todos os elementos desejados neste modelo.'
        ]
        self.sentences = {}
        self.questions = []


    def prepare(self):
        for s in self.target:
            sent = self.parser.gerar_sentenca(s)
            if sent != None:
                self.sentences[sent.id] = sent
                self.questions.extend(sent.questions)

        random.shuffle(self.questions)

    def get_question(self, indice):
        return self.questions[indice]


if __name__ == '__main__':
    print SentenceDatabase.Instance().get_question(0).toDict()
    print SRL
