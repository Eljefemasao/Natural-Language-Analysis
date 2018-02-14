<html>
<body>
  <h1>Overview</h1>
  Our final project's purpose is to let application reads a document and detects a type of book using Doc2Vec. Stage1is for getting used to the consept of Doc2Vec. And Stage2 is main porject.

<div>
Stage 1:
<p> Now analysis.py are written to be trained by ten soruce books which were done morpheme analysis. And after that, It calculates Input's degree of relatedness using Doc2Vec. At this stage Output will be ten similar words from source books when Input is a book's word. In the same way, Output will be ten source books title when Input is a book's title.</p>

Usage is very easy:

```sh
$ python3 analysis.py
```

  Depending on input, the output will be displayed as the result like the image below. 
  <div>
<img alt="er" src="https://github.com/Eljefemasao/Natural-Language-Analysis/blob/image/image/graph1.png")
     </div>
</div>

<div>
  Stage 2:
  <p>detect_files.py is main project which reads some sentence as Input from sorce book's document and detects the document's field as Output.</p>
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

</body>
</html>
B
