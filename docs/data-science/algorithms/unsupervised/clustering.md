# Clustering

In this section, we will start to explore unsupervised learning, where we work 
with data that isn't accompanied by labels. One of the primary techniques 
within this realm is clustering, which aims to uncover patterns or structures 
in the data by grouping similar data points together. A popular method for 
achieving this is k-means clustering, which aims to identify clusters of 
similar observations.

## K-means

K-means was briefly introduced in the [Introduction](../index.md#example_1) to 
Supervised vs. Unsupervised Learning and used to segment customers based on 
their annual spending and average basket size.

<div style="text-align: center;">
    <iframe src="/assets/data-science/algorithms/clusters.html" width="600" height="450">
    </iframe>
    <figcaption>
        An exemplary application of k-means clustering to segment customers.
    </figcaption>
</div>

The algorithm groups similar data points together based on their attributes
without being told what these groups should be. 

To get a better understanding of k-means, we will explore the theory behind it
and employ the algorithm to cluster data from Spotify and a semiconductor 
manufacturer.
