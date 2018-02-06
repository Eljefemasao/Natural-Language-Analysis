<html>
<body>
  <h1>Overview</h1>
  Our final purpose is to let application reads a document and detects a type of book using Word2Vec and Doc2Vec.
<p> Now analysis.py are written to be trained by ten soruce books which were done morpheme analysis and after that, calculates Input's degree of relatedness using doc2vec. At this stage Output will be ten similar words from source books when Input is a book's word. In the same way, Output will be ten source books title when Input is a book's title.</p>

  Depending on input, the output [$ python3 analysis.py] is displayed as the result like the image below. 
  <div>
<img alt="er" src="https://github.com/Eljefemasao/Natural-Language-Analysis/blob/image/image/graph1.png")
     </div>
  <h2>Files</h2>

  Basic files:  
  <ul>
    <li>analysis.py- have function contain implementation of a simple doc2vec.</li>
    <li>create_file.py- extract train data from directory test_file.</li>
    <li>make_index.py- extract directory test_file from directory 917.</li>
    <li>detect_files.py- have TOPIC_ANALYZE function. This is main project.</li>
  </ul>
  
  Major dependiencies are:
  
  <ul>
    <li>python3.6.3</li>
    <li>gensim</li>
    <li>MeCab-0.996</li>
    <li>mecab-ipadic-neologd</li>
    <li>sklearn</li>
  </ul>
  <h2>About Source Books</h2>
  Source Books are here <a href="http://yozora.main.jp/9/ndc91.html">http://yozora.main.jp/9/ndc91.html</a>

  <h2>Word2Vec</h2>
  Word2Vec is a particularly computationally-efficient predictive model for learning word embeddings from raw text. This model converts target words as vector and it makes model calculates degree of relatedness each other.
</body>
</html>
B
