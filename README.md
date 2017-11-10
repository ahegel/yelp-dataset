# Predicting Star Ratings on Yelp

## Summary

Which business attributes have the greatest impact on a Yelp business' star rating? Using a variety of regression models, I was able to predict (within about 0.75 stars accuracy) a business' star rating given only its business attributes. Some of the attributes that proved most predictive include:

* Karaoke music
* Catering
* Bike parking
* Street parking
* Intimate ambiance

You can walk through the analysis [here](https://github.com/ahegel/yelp-dataset/blob/master/Predicting%20Star%20Ratings.ipynb).

## Dataset

This project uses the [Yelp Open Dataset](https://www.yelp.com/dataset), which includes 5 files:

* `business.json`: Contains business data including location data, attributes, and categories.
* `review.json`: Contains full review text data including the user_id that wrote the review and the business_id the review is written for.
* `user.json`: User data including the user's friend mapping and all the metadata associated with the user.
* `checkin.json`: Checkins on a business.
* `tip.json`: Tips written by a user on a business. Tips are shorter than reviews and tend to convey quick suggestions.

I've filtered the dataset to include only businesses in Cleveland, Ohio, and included the filtered data in the `data` directory of this repo. To create your own subset of the Yelp dataset, you can use `create_sample_data.py` and alter the line below based on your own desired filter:

```python
business_sample = business_df[business_df['city'].str.contains('leveland')]
```
