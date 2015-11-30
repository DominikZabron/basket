#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from os import chdir, remove
chdir("/home/dominik/Dropbox/baskets/tests")

short_defender = 'SHORT-DEFENDER.txt'
short_midfielder = 'SHORT-MIDFIELDER.txt'
short_attacker = 'SHORT-ATTACKER.txt'
long_attacker = 'LONG-ATTACKER.txt'
long_midfielder = 'LONG-MIDFIELDER.txt'
long_defender = 'LONG-DEFENDER.txt'

short = "SSHRT"
long = "BUY"

def send_order(symbol, side, price, basket):
	"""Wprowadza kolejne zlecenie do koszyka."""
	if price:
		file = open(basket, 'a')	
		form = "1={0}~2={1}~3=WTPZADOM~4=ASRDOT~5=DAY~6={2}~8=100~\n".format(symbol, side, price)
		file.write(form)
		file.close()
		
def delete_order(symbol, basket):
	"""Usuwa zlecenie z koszyka."""
	pattern = '1={0}'.format(symbol)
	old_file = open(basket)
	old_content = old_file.read()
	l = old_content.find(pattern)
	old_file.close()
	if not l == -1:
		r = old_content.find("\n", l) + 1
		new_content = old_content.replace(old_content[l:r], "")
		remove(basket)
		new_file = open(basket, 'w')
		new_file.write(new_content)
		new_file.close()
		

def symbol_query():
	"""Nadaje zapytanie o symbol."""
	symbol = raw_input("Symbol: ").upper()
	if symbol:
		return symbol
	else:
		exit()

def price_query(basket):
	"""Nadaje zapytanie o cenę."""
	price = raw_input("Cena {0}: ".format(basket)).replace(",", ".")
	return price
	

	
	
def meta_manager():
	"""Nadaje zapytania w odpowiedniej kolejności. 
	
	Każde zlecenie zapisuje do odpowiedniego koszyka zleceń, powtarzające się usuwa.
	""" 
	symbol = symbol_query()
	
	side = short
	
	basket = short_defender
	delete_order(symbol, basket)
	price = price_query(basket)
	send_order(symbol, side, price, basket)
	
	
	basket = short_midfielder
	delete_order(symbol, basket)
	price = price_query(basket)
	send_order(symbol, side, price, basket)
	
	basket = short_attacker
	delete_order(symbol, basket)
	price = price_query(basket)
	send_order(symbol, side, price, basket)
	
	side = long
	
	basket = long_attacker
	delete_order(symbol, basket)
	price = price_query(basket)
	send_order(symbol, side, price, basket)
	
	basket = long_midfielder
	delete_order(symbol, basket)
	price = price_query(basket)
	send_order(symbol, side, price, basket)
	
	basket = long_defender
	delete_order(symbol, basket)
	price = price_query(basket)
	send_order(symbol, side, price, basket)
	


if __name__ == "__main__":
	while True:
		meta_manager()

