from random import randint
def direct(list_of_words,cache_size,cache_line):
	block_size = int(cache_size/cache_line)
	number_of_block = int(128/block_size)
	main_memory = list()
	i = 0
	while(i < len(list_of_words)):
		block = list_of_words[i : i+block_size]
		main_memory.append(block)
		i = i + block_size
	cache_positions = list()
	i = 0
	while(i < cache_line):
		positions = list()
		j = i
		while(j < number_of_block):
			positions.append(j)
			j = j + cache_line
		cache_positions.append(positions)
		i = i + 1
	cache = list()
	cache_address = list()
	i = 0
	for i in range(cache_line):
		cache.append("null")
	i = 0
	for i in range(cache_line):
		cache_address.append("null")
	print("enter number of address to be loaded : ")
	number_of_address = int(input())
	if(number_of_address > 0):
		print("enter those address : ")
		for i in range(number_of_address):
			address = input()
			line_bit = int(power_of_two(cache_line))
			offset = int(power_of_two(block_size))
			front_tag = int(power_of_two(128) - (line_bit + offset))
			batch = binary_to_decimal(address[0:front_tag+line_bit])
			batch_word = binary_to_decimal(address[front_tag+line_bit:])
			tag = binary_to_decimal(address[0:front_tag])
			line_number = binary_to_decimal(address[front_tag:front_tag+line_bit])
			batch = main_memory[batch]
			cache[line_number] = batch
			cache_address[line_number] = address
			print("address " + address + " is added to cache and the desired data was : " + batch[batch_word])
	print("do you want to do any further operation (type  yes/no )")
	further_operation = (input()).lower()
	if(further_operation == "yes"):
		while(True):
			print("the operations available are : ")
			print("1) print the cache and the address in cache ( type - 1 ) ")
			print("2) add an address in cache ( type - 2 ) ")
			print("3) search any address in cache ( type - 3 ) ")
			print("4) exit ( type - 4 ) ")
			operation = int(input())
			if(operation == 1):
				print("the cache is printed below : ")
				print(cache)
				print("the address has been printed below : ")
				print(cache_address)
			elif(operation == 2):
				print("enter the address to be loaded : ")
				address = input()
				if(address in cache_address):
					line_bit = int(power_of_two(cache_line))
					offset = int(power_of_two(block_size))
					front_tag = int(power_of_two(128) - (line_bit + offset))
					batch_word = binary_to_decimal(address[front_tag+line_bit:])
					line_number = binary_to_decimal(address[front_tag:front_tag+line_bit])
					print("this address is already present in cache memory")
					print("the data for desired address is : "+ (cache[line_number])[batch_word])
				else:
					line_bit = int(power_of_two(cache_line))
					offset = int(power_of_two(block_size))
					front_tag = int(power_of_two(128) - (line_bit + offset))
					batch = binary_to_decimal(address[0:front_tag+line_bit])
					batch_word = binary_to_decimal(address[front_tag+line_bit:])
					tag = binary_to_decimal(address[0:front_tag])
					line_number = binary_to_decimal(address[front_tag:front_tag+line_bit])
					batch = main_memory[batch]
					cache[line_number] = batch
					# cache.insert(line_number,batch)
					cache_address[line_number] = address
					print("address " + address + " is added to cache and the desired data was : " + batch[batch_word])
			elif(operation == 3):
				print("enter the address to be searched : ")
				address = input()
				if(address in cache_address):
					line_bit = int(power_of_two(cache_line))
					offset = int(power_of_two(block_size))
					front_tag = int(power_of_two(128) - (line_bit + offset))
					batch_word = binary_to_decimal(address[front_tag+line_bit:])
					line_number = binary_to_decimal(address[front_tag:front_tag+line_bit])
					print("IT'S A HIT!")
					print("this address is present in cache memory")
					print("the data for desired address is : "+ (cache[line_number])[batch_word])
				else:
					line_bit = int(power_of_two(cache_line))
					offset = int(power_of_two(block_size))
					front_tag = int(power_of_two(128) - (line_bit + offset))
					line_number = binary_to_decimal(address[front_tag:front_tag+line_bit])
					if(cache_address[line_number] == "null"):
						line_bit = int(power_of_two(cache_line))
						offset = int(power_of_two(block_size))
						front_tag = int(power_of_two(128) - (line_bit + offset))
						batch = binary_to_decimal(address[0:front_tag+line_bit])
						batch_word = binary_to_decimal(address[front_tag+line_bit:])
						tag = binary_to_decimal(address[0:front_tag])
						line_number = binary_to_decimal(address[front_tag:front_tag+line_bit])
						batch = main_memory[batch]
						cache[line_number] = batch
						cache_address[line_number] = address
						print("IT'S A MISS!")
						print("address " + address + " is added to cache and the desired data was : " + batch[batch_word])
					else:
						print("IT'S A MISS!")
						print("there was a replacment done in cache")
						line_bit = int(power_of_two(cache_line))
						offset = int(power_of_two(block_size))
						front_tag = int(power_of_two(128) - (line_bit + offset))
						batch = binary_to_decimal(address[0:front_tag+line_bit])
						batch_word = binary_to_decimal(address[front_tag+line_bit:])
						tag = binary_to_decimal(address[0:front_tag])
						line_number = binary_to_decimal(address[front_tag:front_tag+line_bit])
						batch = main_memory[batch]
						cache[line_number] = batch
						cache_address[line_number] = address
						print(" now the address " + address + " is added to cache and the desired data was : " + batch[batch_word])
			else:
				print("thank you!")
				break;
	else:
		print("thank you!")

def associated(list_of_words,cache_size,cache_line):
	block_size = int(cache_size/cache_line)
	number_of_block = int(128/block_size)
	main_memory = list()
	i = 0
	while(i < len(list_of_words)):
		block = list_of_words[i : i+block_size]
		main_memory.append(block)
		i = i + block_size
	cache_index = 0
	cache = list()
	i = 0
	for i in range(cache_line):
		cache.append("null")
	cache_address = list()
	i = 0
	for i in range(cache_line):
		cache_address.append("null")
	print("enter number of address to be loaded : ")
	number_of_address = int(input())
	if(number_of_address > 0):
		print("enter those address : ")
		for i in range(number_of_address):
			if(cache_index == cache_line):
				cache_index = 0
			address = input()
			line_bit = int(power_of_two(cache_line))
			offset = int(power_of_two(block_size))
			front_tag = int(power_of_two(128) - (line_bit + offset))
			batch = binary_to_decimal(address[0:front_tag+line_bit])
			batch_word = binary_to_decimal(address[front_tag+line_bit:])
			tag = binary_to_decimal(address[0:front_tag])
			batch = main_memory[batch]
			cache[cache_index] = batch
			cache_address[cache_index] = address
			cache_index = cache_index + 1
			print("address " + address + " is added to cache and the desired data was : " + batch[batch_word])
	print("do you want to do any further operation (type  yes/no )")
	further_operation = (input()).lower()
	if(further_operation == "yes"):
		while(True):
			print("the operations available are : ")
			print("1) print the cache and the address in cache ( type - 1 ) ")
			print("2) add an address in cache ( type - 2 ) ")
			print("3) search any address in cache ( type - 3 ) ")
			print("4) exit ( type - 4 ) ")
			operation = int(input())
			if(operation == 1):
				print("the cache is printed below : ")
				print(cache)
				print("the address has been printed below : ")
				print(cache_address)
			elif(operation == 2):
				if(cache_index == cache_line):
					cache_index = 0
				print("enter the address to be loaded : ")
				address = input()
				if(address in cache_address):
					line_bit = int(power_of_two(cache_line))
					offset = int(power_of_two(block_size))
					front_tag = int(power_of_two(128) - (line_bit + offset))
					batch = binary_to_decimal(address[0:front_tag+line_bit])
					batch_word = binary_to_decimal(address[front_tag+line_bit:])
					tag = binary_to_decimal(address[0:front_tag])
					batch = main_memory[batch]
					print("this address is already present in cache memory")
					print("the data for desired address is : "+ batch[batch_word])
				else:
					line_bit = int(power_of_two(cache_line))
					offset = int(power_of_two(block_size))
					front_tag = int(power_of_two(128) - (line_bit + offset))
					batch = binary_to_decimal(address[0:front_tag+line_bit])
					batch_word = binary_to_decimal(address[front_tag+line_bit:])
					tag = binary_to_decimal(address[0:front_tag])
					batch = main_memory[batch]
					cache[cache_index] = batch
					cache_address[cache_index] = address
					cache_index = cache_index + 1
					print("address " + address + " is added to cache and the desired data was : " + batch[batch_word])	
			elif(operation == 3):
				if(cache_index == cache_line):
					cache_index = 0
				print("enter the address to be searched : ")
				address = input()
				if(address in cache_address):
					line_bit = int(power_of_two(cache_line))
					offset = int(power_of_two(block_size))
					front_tag = int(power_of_two(128) - (line_bit + offset))
					batch = binary_to_decimal(address[0:front_tag+line_bit])
					batch_word = binary_to_decimal(address[front_tag+line_bit:])
					tag = binary_to_decimal(address[0:front_tag])
					batch = main_memory[batch]
					print("IT'S A HIT!")
					print("this address is present in cache memory")
					print("the data for desired address is : "+ batch[batch_word])
				else:
					if("null" in cache):
						line_bit = int(power_of_two(cache_line))
						offset = int(power_of_two(block_size))
						front_tag = int(power_of_two(128) - (line_bit + offset))
						batch = binary_to_decimal(address[0:front_tag+line_bit])
						batch_word = binary_to_decimal(address[front_tag+line_bit:])
						tag = binary_to_decimal(address[0:front_tag])
						batch = main_memory[batch]
						cache[cache_index] = batch
						cache_address[cache_index] = address
						cache_index = cache_index + 1
						print("IT'S A MISS!")
						print("address " + address + " is added to cache and the desired data was : " + batch[batch_word])
					else:
						print("IT'S A MISS!")
						print("there was a replacment done in cache")
						line_bit = int(power_of_two(cache_line))
						offset = int(power_of_two(block_size))
						front_tag = int(power_of_two(128) - (line_bit + offset))
						batch = binary_to_decimal(address[0:front_tag+line_bit])
						batch_word = binary_to_decimal(address[front_tag+line_bit:])
						tag = binary_to_decimal(address[0:front_tag])
						batch = main_memory[batch]
						cache[cache_index] = batch
						cache_address[cache_index] = address
						cache_index = cache_index + 1
						print(" now the address " + address + " is added to cache and the desired data was : " + batch[batch_word])		
			else:
				print("thank you!")
				break;
	else:
		print("thank you!")

def n_way(list_of_words,cache_size,cache_line,k):
	block_size = int(cache_size/cache_line)
	number_of_block = int(128/block_size)
	main_memory = list()
	i = 0
	while(i < len(list_of_words)):
		block = list_of_words[i : i+block_size]
		main_memory.append(block)
		i = i + block_size
	number_of_set = int(cache_line/k)
	bit_size_of_set_number = power_of_two(number_of_set)
	number_of_lines_in_each_set = int(cache_line/number_of_set)
	set_positions = list()
	for i in range(number_of_set):
		set_positions.append(list())
	for i in range(number_of_block):
		kmodn = int(i % number_of_set)
		(set_positions[kmodn]).append(i)
	cache = list()
	cache_address = list()
	for i in range(number_of_set):
		set_of_lines = list()
		for j in range(number_of_lines_in_each_set):
			set_of_lines.append("null")
		cache.append(set_of_lines)
	for i in range(number_of_set):
		set_of_lines = list()
		for j in range(number_of_lines_in_each_set):
			set_of_lines.append("null")
		cache_address.append(set_of_lines)
	print("enter number of address to be loaded : ")
	number_of_address = int(input())
	if(number_of_address > 0):
		print("enter those address : ")
		for i in range(number_of_address):
			address = input()
			if(True):
				line_bit = int(power_of_two(cache_line/k))
				offset = int(power_of_two(block_size))
				front_tag = int(power_of_two(128) - (line_bit + offset))
				batch = binary_to_decimal(address[0:front_tag+line_bit])
				batch_word = binary_to_decimal(address[front_tag+line_bit:])
				tag = binary_to_decimal(address[0:front_tag])
				batch = main_memory[batch]
				set_number = binary_to_decimal(address[(front_tag+line_bit)-bit_size_of_set_number:front_tag+line_bit])
				cache_set = cache[set_number]
				address_set = cache_address[set_number]
				if("null" in address_set):
					index_inside = cache_set.index("null")
					(cache[set_number])[index_inside] = batch
					(cache_address[set_number])[index_inside] = address
					print("address " + address + " is added to cache and the desired data was : " + batch[batch_word])
				else:
					random_set_entry = randint(0,number_of_lines_in_each_set - 1)
					(cache[set_number])[random_set_entry] = batch
					(cache_address[set_number])[random_set_entry] = address
					print("address " + address + " is added to cache and the desired data was : " + batch[batch_word])
	print("do you want to do any further operation (type  yes/no )")
	further_operation = (input()).lower()
	if(further_operation == "yes"):
		while(True):
			print("the operations available are : ")
			print("1) print the cache and the address in cache ( type - 1 ) ")
			print("2) add an address in cache ( type - 2 ) ")
			print("3) search any address in cache ( type - 3 ) ")
			print("4) exit ( type - 4 ) ")
			operation = int(input())
			if(operation == 1):
				print("the cache is printed below : ")
				print(cache)
				print("the address has been printed below : ")
				print(cache_address)
			elif(operation == 2):
				print("enter the address to be loaded : ")
				address = input()
				if(True):
					line_bit = int(power_of_two(cache_line/k))
					offset = int(power_of_two(block_size))
					front_tag = int(power_of_two(128) - (line_bit + offset))
					batch = binary_to_decimal(address[0:front_tag+line_bit])
					batch_word = binary_to_decimal(address[front_tag+line_bit:])
					tag = binary_to_decimal(address[0:front_tag])
					batch = main_memory[batch]
					set_number = binary_to_decimal(address[(front_tag+line_bit)-bit_size_of_set_number:front_tag+line_bit])
					cache_set = cache[set_number]
					address_set = cache_address[set_number]
					if(address in address_set):
						print("this address is present in cache memory")
						print("the data for desired address is : "+ batch[batch_word])
					elif("null" in address_set):
						null_index = address_set.index("null")
						(cache[set_number])[null_index] = batch
						(cache_address[set_number])[null_index] = address
						print("address " + address + " is added to cache and the desired data was : " + batch[batch_word])
					else:
						random_set_entry = randint(0,number_of_lines_in_each_set - 1)
						(cache[set_number])[random_set_entry] = batch
						(cache_address[set_number])[random_set_entry] = address
						print("address " + address + " is added to cache and the desired data was : " + batch[batch_word])
			elif(operation == 3):
				print("enter the address to be searched : ")
				address = input()
				if(True):
					line_bit = int(power_of_two(cache_line/k))
					offset = int(power_of_two(block_size))
					front_tag = int(power_of_two(128) - (line_bit + offset))
					batch = binary_to_decimal(address[0:front_tag+line_bit])
					batch_word = binary_to_decimal(address[front_tag+line_bit:])
					tag = binary_to_decimal(address[0:front_tag])
					batch = main_memory[batch]
					set_number = binary_to_decimal(address[(front_tag+line_bit)-bit_size_of_set_number:front_tag+line_bit])
					cache_set = cache[set_number]
					address_set = cache_address[set_number]
					if(address in address_set):
						print("IT'S A HIT!")
						print("this address is present in cache memory")
						print("the data for desired address is : "+ batch[batch_word])
					else:
						if("null" in address_set):
							print("IT'S A MISS!")
							null_index = address_set.index("null")
							(cache[set_number])[null_index] = batch
							(cache_address[set_number])[null_index] = address
							print("there was no replacement required")
							print("address " + address + " is added to cache and the desired data was : " + batch[batch_word])
						else:
							print("IT'S A MISS!")
							random_set_entry = randint(0,number_of_lines_in_each_set - 1)
							(cache[set_number])[random_set_entry] = batch
							(cache_address[set_number])[random_set_entry] = address
							print("there was a replacement done")
							print("address " + address + " is added to cache and the desired data was : " + batch[batch_word])
			else:
				print("thank you!")
				break;
	else:
		print("thank you!")

def binary_to_decimal(binary):
	i = len(binary) - 1
	j = 0
	summ = 0
	while(i >= 0):
		summ = summ + int(binary[i])*int(2**j)
		i = i - 1
		j = j + 1
	return int(summ)

def power_of_two(number):
	for i in range(999999):
		if(2**i == number):
			return i

file = open("words.txt","r")
all_words = file.read()
list_of_words = all_words.split('\n')
print("select method")
print("1) direct")
print("2) associated")
print("3) k-way")
method = int(input())
if(method == 1):
	cache_size = int(input("enter cache size : "))
	cache_line = int(input("enter cache lines : "))
	direct(list_of_words,cache_size,cache_line)
elif(method == 2):
	cache_size = int(input("enter cache size : "))
	cache_line = int(input("enter cache lines : "))
	associated(list_of_words,cache_size,cache_line)
else:
	cache_size = int(input("enter cache size : "))
	cache_line = int(input("enter cache lines : "))
	set_num = int(input("enter set : ")) 
	n_way(list_of_words,cache_size,cache_line,set_num)