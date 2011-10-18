#!/usr/bin/env python3


import os
import re
import sys


def criar_pdf(nomes, nome='certificado.svg'):
	for participante in open(nomes).readlines():
		nome_participante = participante.strip().replace(' ', '_').lower()
		with open(nome) as arquivo_original, open(nome_participante + '.svg', 'w') as arquivo_temporario:
			dados = re.sub('__nome__', participante, arquivo_original.read())
			arquivo_temporario.write(dados)
		os.system('inkscape --export-pdf={nome}.pdf {nome}.svg'.format(nome=nome_participante))
		os.remove(nome_participante + '.svg')


criar_pdf(*sys.argv[1:])