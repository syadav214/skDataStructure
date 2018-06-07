"""
Get area of letter for selecting in a PDF for given heights.
"""

def designerPdfViewer(h, word):
	#subtract value of alphabet from ascii is 97
	width = len(word)
	word_height = []
	for letter in word:
		word_height.append(h[ord(letter) - 97])
	return max(word_height) * width


if __name__ == "__main__":
	h = map(int,'1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7'.split(' '))
	word = 'zaba'
	print designerPdfViewer(h, word)