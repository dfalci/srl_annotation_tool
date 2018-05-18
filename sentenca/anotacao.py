# -*- coding: utf-8; -*-
import uuid
from dotmap import DotMap

def create_question(sentence_id, chunks, pergunta=None, opcoes = [], texto_aberto=False, pode_pular=True, permitir_nao_se_aplica=True, opcao_obrigatoria=False, contiguidade=False, skip_list=[]):
    retorno = DotMap({})
    retorno.id = str(uuid.uuid1())
    retorno.sentence_id = sentence_id
    retorno.chunks = [chunks] if not isinstance(chunks, list) else chunks
    retorno.pergunta = pergunta
    retorno.pode_pular = pode_pular
    retorno.opcoes = opcoes
    retorno.texto_aberto = texto_aberto
    retorno.nao_se_aplica = permitir_nao_se_aplica
    retorno.opcao_obrigatoria=opcao_obrigatoria
    retorno.contiguidade= contiguidade
    retorno.skip_list = skip_list
    retorno.respostas = []
    return retorno

def create_option(texto, valor=None):
    retorno = DotMap()
    retorno.texto = texto
    retorno.valor = valor if valor != None else texto
    retorno.respostas = []
    return retorno

def create_sentence(texto, verbo):
    retorno = DotMap({})
    retorno.id = str(uuid.uuid1())
    retorno.texto = texto
    retorno.verbo = verbo
    retorno.quantidade_respostas = 0
    return retorno







if __name__ == '__main__':
    print create_question(['teste', u'é', 'para'], u'qual é a cor do cavalo branco de napoleao?', opcoes=[create_option('teste1')])




