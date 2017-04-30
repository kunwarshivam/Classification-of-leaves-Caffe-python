<?php
session_start();
?>
<html>
<head>
<title>Final Year Project-13BEE0084</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" type="text/css" href="mycss2.css">
<link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Ubuntu">
</head>
<body>
<div class="fix">
  <br>
<h1>Design of a Neural Network Model for Classification of Leaves</h1>
<nav id="menu">
<a href="index.html">Home </a>
<a href = "https://www.linkedin.com/in/mathew-mithra-noel-18125794/">LinkedIn: Mathew M. Noel</a>
<a href = "https://www.linkedin.com/in/kunwarshivam">LinkedIn: Kunwar Shivam Srivastav</a>
<a href = "https://github.com/kunwarshivam/Classification-of-leaves-Caffe-python">GitHub</a>
</nav>
<br>
</div>
<section id="sec">
<p id="pro">
 This project,<b> Design of a Neural Network Model for Classification of Leaves</b>, has been completed by <em>13BEE0084, Kunwar Shivam Srivastav</em> as a part of final year project
under the guidance of <em>Dr. Mathew M. Noel</em> of <em>School of Electrical Engineering(SELECT)</em> of <em>VIT University, Vellore.</em> <br>
</p>
<p id="data">
<b>Datasets used:</b><br>
To go to the homepage of the dataset, click ->
<a href="http://cs-chan.com/downloads_MKLeaf_dataset.html">Malaykew Leaf Dataset</a></ol>
<br></p>
<p id="image">
<b>Image:</b><br>
<br>
<img src="abcd/image.jpg">
<br>
<br>
</p>
<p id="result">
<b>This leaf belongs to, or is most similar to:</b> <br>
<p id="output">
<?php $class = substr($_SESSION['output'], 16969); echo "<b>$class</b>"; session_unset();session_destroy();?>
</p>
</p>
<html>
<body>
<p id="ty">
Thank You.
</p>
<p id="fo">
<img src="maple-leaf.jpg"/>
</body>
</html>
