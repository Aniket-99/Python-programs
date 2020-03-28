from urllib.request import urlparse


# Get domain name(example.com)

def get_domain_name(url):
	try:
		results = get_sub_domain(url).split('.')
		return results[-2] + '.' + results[-1]
	except:
		return ''



# Get sub domain name (name.example.com)
def get_sub_domain(url):

	try:
		return urlparse(url).netloc
	except:
		return ''

#print(get_domain_name("https://google.com/index.php"))