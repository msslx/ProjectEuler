"""
Project Euler Problem 22
========================

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""

# Get all names and sort them
x = sorted(
    [name for name in
     open('resources/022_names.txt').readline().replace('"', '').split(',')]
)
# get the value of the character with ord() and multiply it with the position
# of the word. Sum up all characters in a word, then sum up all words.
# enumerate(x) would be more pythonic, but this is shorter
print(sum([sum([(j+1)*(ord(i)-64) for i in x[j]]) for j in range(len(x))]))