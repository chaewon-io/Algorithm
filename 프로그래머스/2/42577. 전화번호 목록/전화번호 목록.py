def solution(phone_book):
	phone_book_set = set(phone_book)
	
	for num in phone_book:
		for i in range(1, len(num)):
			if num[:i] in phone_book_set:
				return False
				
	return True