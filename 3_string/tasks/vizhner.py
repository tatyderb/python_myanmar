eng = 'abcdefghijklmnopqrstuvwxyz'

def vizhner_text(keyword, text):
	res = []
	n = len(keyword)
    i_keyword = 0       # i counter in text, i_keyword counter in keyword
	for i in range(len(text)):
		# print(i, i_keyword, keyword[i_keyword], text[i])
		# space remain space
		if not text[i] in eng:
			res.append(text[i])
		else:
			res.append(vizhner_letter(text[i], keyword[i_keyword], eng))
            i_keyword = (i_keyword + 1) % n
	return ''.join(res)

# code letter in alphabet al to new alphabet according first_letter shift
def vizhner_letter(letter, first_letter, al):
	code_al = new_alphabet(first_letter, al)
	i = al.find(letter)		
	return code_al[i]	
	
# create new alphabet from al and first letter of new alphabet
def new_alphabet(first_letter, al):
	k = al.find(first_letter)
	return al[k:] + al[:k]

# keyword = "lemon"
# text = "attack at dawn"
keyword = input()
text = input()
res = vizhner_text(keyword, text)
print(res)

def test_new_alphabet():
	b = new_alphabet('d', eng)
	print(b)
    assert b == 'defghijklmnopqrstuvwxyzabc'

def test_vizhner_letter():
	keyword = "lemon"
	text = "attack at dawn"
	coded_text = vizhner_text(keyword, text)
	let = 'a'
	let2 = vizhner_letter(let, 'l', eng)
	print(let, let2) # a -> l expected
    assert let2 == 'l'

	let = 't'
	let2 = vizhner_letter(let, 'e', eng)
	print(let, let2) # t -> x expected
    assert let2 == 'x'

