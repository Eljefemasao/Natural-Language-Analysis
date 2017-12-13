<html>
<body>
  <h1>Overview</h1>
  Our final purpose is to let application read a document and detect a type of book using Word2Vec and Doc2Vec.
  <div>
<img alt="er" src="https://github.com/Eljefemasao/Natural-Language-Analysis/blob/image/image/graph1.png")
  </div>
     <h2>What is Word2Vec</h2>
  Word2Vec is a particularly computationally-efficient predictive model for learning word embeddings from raw text. This model converts target words as vector and it makes model calculates degree of relatedness each other.
  <h2>Why Learn Word Embeddings [ADMONITION]</h2>
  Imange and audio processing systems work with rich, high-dimensional datasets encoded as vectors of the individual raw pixel-intensities for image data, or e.g. power spectral density coefficients for audio data. For tasks like object or speech recognition we know that all the information required to successfully perform the task is encoded in the data (because humans can perform these tasks from the raw data). However,natural language processing systems traditionally treat words as discrete atomic symbols, and therefore 'cat' may be represented as Id537 and 'dog' as Id143. These encodings are arbitrary, and provide no useful information to the system regrading the relationships that may exist between the individual symbols.
  This means that the model can leverage very little of what it has learned about 'cats'when it is processing data about 'dogs' (such that they are both animals,for-legged,pets,etc.). Representing words as unique, discrete ids furthermore leads to data sparsity, and usually means that we may need more data in order to successfully train statical models. Using vector representations can overcome some of these obstacles.
</body>
</html>
