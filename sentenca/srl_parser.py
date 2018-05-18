# -*- coding: utf-8; -*-
from utils import Singleton
from nltk.tokenize import word_tokenize
from nltk.stem import RSLPStemmer
from anotacao import create_sentence, create_question



class SRLParser(object):

    def __init__(self):
        self.stemmer = RSLPStemmer()
        self.verbs = {}
        self.verbs[self.stemmer.stem('publicar')] = ['Quem publica?', 'O que publica?', 'Onde publica?', 'Quando publica?', 'Alcance da publicação?', 'Qualidade da publicacao?']
        self.verbs[self.stemmer.stem('registrar')] = ['Quem registra?', 'Quando registra?', 'Onde registra?', 'Qual o meio de registro?', 'O que se registra?']


    def parse_sentence(self, frase):
        tokens = word_tokenize(frase, language='portuguese')
        for t in tokens:
            verb_config = self.verbs.get(self.stemmer.stem(t.lower()), None)
            if not verb_config is None:
                return (t, verb_config, tokens)
        return (None, None, None)

    def generate_question(self, verb, option):
        return option


    def gerar_sentenca(self, sentenca):
        verbo, config, tokens = self.parse_sentence(sentenca)
        if verbo != None:
            sent = create_sentence(sentenca, verbo)
            sent.questions = []
            for c in config:
                sent.questions.append(create_question(sent.id, tokens, pergunta=self.generate_question(verbo, c), skip_list=[verbo]))
            return sent
        return None



if __name__ == '__main__':
    parser = SRLParser()
    print parser.gerar_sentenca('Durante a sua vida, Albert Einstein publicou centenas de artigos e revistas')
    print parser.gerar_sentenca('Reginaldo quer publicar um novo artigo')
    print parser.gerar_sentenca('Vou publicar uma coisa muito legal')



