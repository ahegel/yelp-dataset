# Yelp Dataset

## Question

This project determines the most important drivers of user engagement with a business on Yelp. Key questions:

* What aspects of a Yelp business profile correlate with better or worse user engagement?
* To improve user engagement, should a business add more pictures, try to encourage more influential reviewers to rate them, offer specials or coupons, allow take-out orders, have better parking, or something else in order to best drive user engagement?

## Dataset

This project uses the [Yelp Open Dataset](https://www.yelp.com/dataset), which includes 5 files:

* `business.json`: Contains business data including location data, attributes, and categories.
* `review.json`: Contains full review text data including the user_id that wrote the review and the business_id the review is written for.
* `user.json`: User data including the user's friend mapping and all the metadata associated with the user.
* `checkin.json`: Checkins on a business.
* `tip.json`: Tips written by a user on a business. Tips are shorter than reviews and tend to convey quick suggestions.

I've filtered the dataset to include only businesses in Arizona or Nevada.