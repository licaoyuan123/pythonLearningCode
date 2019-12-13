import functools

def log(txt):
	if isinstance(txt,str):
		def log1(func):
			@functools.wraps(func)
			def wraps(*a,**kw):
				print('begin call:%s'%txt)
				func(*a,**kw)
				print('end call:%s'%txt)
			return wraps
		return log1
	else:
		print(type(txt))
		@functools.wraps(txt)
		def wraps(*a,**kw):
			print('begin call', txt.__name__)
			txt(*a,**kw)
			print('end call', txt.__name__)
		return wraps

@log('decorator with args')
def now(x,y):
	print(x*y)

now(2,3)

@log
def add(x,y):
	print(x+y)

add(2,3)
