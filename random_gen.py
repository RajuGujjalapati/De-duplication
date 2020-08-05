import random
import string
#generating list of 10 random numbers.
random_list = random.sample(range(234234532445,873546372634), 164)
aadhar_random_list=[str(i) for i in random_list]
print(random_list)

letters=string.ascii_letters
store_strings=[]
for i in range(164):
	a=''.join(random.choice(letters) for i in range(5))
	store_strings.append(a)

random_list_num = random.sample(range(2342,9999), 164)
random_num_str = [str(i) for i in random_list_num]

# single_char = random.sample(string.ascii_letters, 164)
single_char=[]
for i in range(164):
	a=''.join(random.choice(letters) for i in range(1))
	single_char.append(a)
res=[''.join(x) for x in zip(store_strings,random_num_str,single_char)]
print(res)


