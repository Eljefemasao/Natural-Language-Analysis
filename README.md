<html>
<body>

<div>
  <img alt="er" src="https://github.com/Eljefemasao/Natural-Language-Analysis/blob/image/image/doc2vec.png">
</div>

<div>
  <h1>Overview</h1>
<p>Our final project's purpose is to let application reads a document and detects a type of book using Doc2Vec. I tackled Stage1 for getting used to the concept of Doc2Vec and Stage2 for main project.
</p>
</div>  

<div>
Stage 1:
<p> Now analysis.py are written to be trained by ten source books which were done morpheme analysis. And after that, It calculates Input's degree of relatedness using Doc2Vec. At this stage Output will be ten similar words from source books when Input is a book's word. In the same way, Output will be ten source books title when Input is a book's title.</p>

Usage is very easy:

```sh
$ python3 analysis.py
```

  Depending on input, the output will be displayed as the result like the image below.
  <div>
<img alt="er" src="https://github.com/Eljefemasao/Natural-Language-Analysis/blob/image/image/graph1.png">
     </div>
</div>
<div>
  <img alt="er" src="https://github.com/Eljefemasao/Natural-Language-Analysis/blob/image/image/graph_dot.png">
</div>
<div>
  Stage 2:
  <p>detect_files.py is main project which reads some sentence as Input from sorce book's document and detects the document's field as Output.</p>

Usage:
  ```sh
  $ python3 detect_files.py
  ```
  For instance, I'm going to input some sentence from one of '日本文学' document.
  <div>
    <img alt="er" src="https://github.com/Eljefemasao/Natural-Language-Analysis/blob/image/image/input.png">
  </div>
<div>
  <p>Depending on input, the output will be displayed as the result like the image below.</p>
</div>
  <div>
    <img alt="er" src="https://github.com/Eljefemasao/Natural-Language-Analysis/blob/image/image/result1.png">
  </div>
  <div>
    <img alt="er" src="https://github.com/Eljefemasao/Natural-Language-Analysis/blob/image/image/result2.png">
  </div>  
</div>


  <h2>Files</h2>

  Basic files:  
  <ul>
    <li>analysis.py- have function contain implementation of a simple doc2vec.</li>
    <li>create_file.py- extract train data from directory test_file.</li>
    <li>make_index.py- extract directory test_file from directory 917.</li>
    <li>detect_files.py- have TOPIC_ANALYZE function. This is main project.</li>
  </ul>

  Major dependencies are:

  <ul>
    <li>python:3.6.3</li>
    <li>gensim:3.2.0</li>
    <li>MeCab-0.996</li>
    <li>mecab-ipadic-neologd</li>
    <li>scikit-learn:0.19.1</li>
    <li>pandas:0.20.3</li>
    <li>numpy:1.14.0</li>
    <li>tqdm:4.19.4</li>
  </ul>

  <h2>Directories</h2>

  Basic directories:
  <ul>
    <li>test_file- have documents which were done morpheme analysis for train model at analysis.py.</li>
    <li>classify_novel- have each title(string) of Source Books for analysis.py.</li>
    <li>source- have documents which were done morpheme analysis for train model at detect_files.py.</li>
  </ul>

  <h2>About Source Books</h2>
  Source Books are here <a href="http://yozora.main.jp/9/ndc91.html">http://yozora.main.jp/9/ndc91.html</a>

  <h2>License</h2>
  This project is released under the <a href="https://github.com/Eljefemasao/Natural-Language-Processing/blob/master/LICENSE">MIT License</a>. For more information, see the LICENSE file.
</body>
</html>
