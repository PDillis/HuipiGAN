# HuipiGAN


## Summary

We will generate, via a GAN, huipiles from different regions of Guatemala. Due to the size of the dataset, we won't separate it from region to region (as it should be, due ot the different techniques used in each region). Instead, we will simply generate new huipil that will be a combination of these.

At the end, a more pertinent question to answer is: how to better detect and stop illicit use of mayan fabrics? Indeed, it is a [point of conflict](https://www.plazapublica.com.gt/content/arte-robado-la-batalla-legal-de-las-tejedoras-mayas) [with great repercussions](https://www.mayanhands.org/blogs/news/the-huipil-in-danger) [for the mayan population](https://intercontinentalcry.org/es/tejedoras-mayas-proponen-ley-de-propiedad-intelectual-colectiva-2/) throughout Mesoamerica. Computer Vision might provide the key to solving this issue once and for all.

## Gathering Data

A first attempt to gather images from huipiles from around Guatemala was done via downloading the images documented in [this blogspot](http://huipilesdeguatemala.blogspot.com/2011/09/huipiles-cotidianos.html). Since downloading each image individually was a bit of a tedious work, we automated it using Python. We present the code in `download_huipiles.py`. 

However, it was noted that even after all this work, we only obtained around 19 images (of which 7 were corrupt), so we need another way to gather these images. Luckily we found a [Flickr album by Karen Elwell](https://www.flickr.com/photos/citlali/albums/72157600009235647) which she has graciously permitted me to use for this purpose. This way we managed to obtain 122 images, an order of magnitude more than what we previously had.
