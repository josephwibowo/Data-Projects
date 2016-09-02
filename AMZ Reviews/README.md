## Amazon Reviews Sentiment Analysis
This project creates a supervised learning model that helps classify an Amazon review as helpful or unhelpful based on the words in the review.

Sentiment analysis determines the attitude or intentions of a writer in a given context. In this case, the sentiment being determined is helpfulness given the context of an Amazon reivew of a product.
Many methods exist to perform such a complex analysis. This project uses Bag of Words and Random Forests to create the model.

Bag of Words is a natural language processing method that represents text as a vector of each unique word in the text as well as the frequency of how often the word occurs in the text. This allows classifiers or other ML methods to train on the data using probability and statistics as the text is now represented numerically.
I will not get into Random Forests as it is a rather complex topic that is not easy to explain. Please google the topic for more information. 

### Data Source
Because the review file is too large to be uploaded, please download it locally at [Julian McAuley's website](http://jmcauley.ucsd.edu/data/amazon/).
The review dataset used in this example is the Health and Personal Care dataset.

### Helpful vs. Unhelpful
In order to train the model, I needed to give the training data my own sentiment labels. I did so using the following standard:
* Ratio of helpful/unhelpful votes is 0-25% - Useless
* Ratio of helpful/unhelpful votes is 25-50% - Unhelpful
* Ratio of helpful/unhelpful votes is 50-75%  - Moderately Helpful
* Ratio of helpful/unhelpful votes is 75-100% - Helpful

## Authors
* **Joseph Wibowo** - [LinkedIn](https://www.linkedin.com/in/josephwibowo) - [Blog](https://datasciencenewb.wordpress.com/)
