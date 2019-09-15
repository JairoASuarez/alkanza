#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sept 15 2019
@author: Jairo Suarez
"""
import argparse
import sys
from os import path
from typing import Dict
from random import choice

_END = '$END'
_LINEBREAK = '$LINEBREAK'


class Grammar:
    def __init__(self, grammar_path: str) -> None:
        if not path.isfile(grammar_path):
            print("Grammar file '{}' doesn't exists.".format(grammar_path))
            sys.exit(1)
        self.rules = self._parse_rules(grammar_path)

    @staticmethod
    def _parse_rules(grammar_path: str) -> Dict:
        """
        Parses grammar file to rules dictionary
        :param grammar_path: str
        :return: Dict of rules
        """
        rules = {}
        with open(grammar_path, 'r') as grammar_file:
            for line in grammar_file:
                rule_name, expressions = line.split(':')
                tokens_list = [expression.split('|') for expression in expressions.split()]
                rules['<{}>'.format(rule_name)] = Rule(tokens_list)
        return rules


class Rule:
    def __init__(self, tokens_list: list) -> None:
        self.tokens_list = tokens_list


class Generator:
    def __init__(self, grammar_path: str, start_rule: str) -> None:
        self._grammar = Grammar(grammar_path)
        self._start_rule = start_rule
        self._poem = ""

        if self._start_rule not in self._grammar.rules.keys():
            print("Start rule '{}' is not valid.".format(self._start_rule))
            sys.exit(1)

    def generate_poem(self) -> None:
        """
        Generates a random poem
        :return: None
        """
        self._generate_word(self._start_rule)
        print(self._poem)

    def _generate_word(self, token: str) -> None:
        """
        Generates a word recursively
        :param token: str
        :return:  None
        """
        if token in self._grammar.rules.keys():
            rule = self._grammar.rules[token]
            for tokens in rule.tokens_list:
                self._generate_word(choice(tokens))
        elif token == _LINEBREAK:
            self._poem = '{}\n'.format(self._poem)
        elif token != _END:
            self._poem = '{}{} '.format(self._poem, token)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Terminal application to generate random poems from a grammar.')
    parser.add_argument('-g', dest='grammar_path', help='Grammar file path', default='grammar.txt')
    parser.add_argument('-s', dest='start_rule', help='Start rule', default='<POEM>')
    args = parser.parse_args()
    grammar_path_arg = args.grammar_path
    start_rule_arg = args.start_rule
    Generator(grammar_path_arg, start_rule_arg).generate_poem()
