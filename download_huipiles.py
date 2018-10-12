import re
import requests
from bs4 import BeautifulSoup
import os
import urllib


def get_images():
  # We specify the website where we will download the images from.
  site = 'http://huipilesdeguatemala.blogspot.com/2011/09/huipiles-cotidianos.html'

  # We will use urllib and BeautifulSoup to collect the images
  page = urllib.request.urlopen(site).read()
  soup = BeautifulSoup(page, 'html.parser')   # We parse the html

  # We find all the 'a' tags that have an outer link (since this is how the blog links the huipiles).
  img_links = soup.findAll('a', attrs={'href': re.compile("^http://")})

  # We look for all the img_links that end with 'jpg':
  imgs = [link.get('href') for link in img_links if link.get('href')[-3:] == 'jpg']
  n_imgs = len(imgs)    # The number of images, which we will loop over
  
  return imgs, n_imgs

def main():
  imgs, n_imgs = get_images()

  for i in range(n_imgs):
	  new_site = str(imgs[i])
	  file_name = 'output%i.jpg' % i

	  directory = os.path.dirname(os.path.realpath(__file__)) + '/huipiles/'
	  if not os.path.exists(directory):
		  os.makedirs(directory)

	  with open(os.path.join(directory, file_name), 'wb') as f:
		  try:
			  response = requests.get(new_site)
			  f.write(response.content)
		  except IOError:
			  print("Close, but no cigar.")

if __name__=='__main__':
  main()
