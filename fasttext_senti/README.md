# Text Classification using Facebook FastText

The dataset for this training is downloaded from this [Kaggle Dataset](https://www.kaggle.com/bittlingmayer/amazonreviews)

## bz2 file format
The files downloaded are in bz2 format. Following command is used to decompress

```bunzip2 filename.bz2``` 

OR 

 ```bzip2 -d -k your-filename-here.bz2```
 

## FastText Quantization
When we are working with huge datasets, the model generated will be very huge. The size of the model depends on

- The vocabulary (no. of words )
- Hashtable size which contains the n-grams of words / characters
- Vector size of the words

## Validate the scores
We can see that there is no impact on score (recall, precision) due to quantization. Following proves that 

```
text_classification/amazonreviews$ python3 fasttext_senti.py.py -v amazon.train 
Warning : `load_model` does not return WordVectorModel or SupervisedModel any more, but a `FastText` object which is very similar.
(944, 0.8919491525423728, 0.8919491525423728)

```
After changing the model name to ```model_amazon_q.bin```
```
text_classification/amazonreviews$ python3 fasttext_senti.py -v amazon.train 
Warning : `load_model` does not return WordVectorModel or SupervisedModel any more, but a `FastText` object which is very similar.
(944, 0.8919491525423728, 0.8919491525423728)
```

## References
- To download huge datasets from Kaggle directly to linux machine follow [this article](https://github.com/Kaggle/kaggle-api)

- Post-training quantization in FastText. [link](https://flavioclesio.com/2019/03/22/post-training-quantization-in-fasttext-or-how-to-shrink-your-fasttext-model-in-90/)

- Decompressing bz2 format [Howto](https://www.cyberciti.biz/faq/linuxunix-how-to-extract-and-decompress-a-bz2-tbz2-file/)

- fastText [documentation](https://fasttext.cc/docs/en/faqs.html#how-can-i-reduce-the-size-of-my-fasttext-models)