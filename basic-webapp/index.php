<?php
session_start();
?>
<html>
<head>
<title>Final Year Project-13BEE0084</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
html{
height:130%;
background: -webkit-linear-gradient(bottom right, teal, turquoise, white, cyan, cornflowerblue);
background: -o-linear-gradient(bottom right, teal,turquoise, white,cyan, cornflowerblue);
background: -moz-linear-gradient(bottom right, teal, turquoise, white, cyan, cornflowerblue);
background: linear-gradient(to bottom right, teal, turquoise, white, cyan,cornflowerblue);
}
body{
background-color: rgb(239, 240, 241);
font-family: "Times New Roman", Georgia, Serif;
border-style: groove;
border-width: 15px 15px 15px 15px;
margin: 0px 100px 0px 100px;
padding: 0px 10px 0px 10px;

}
div.fix{
border-bottom: solid;
background-color: white;
border-bottom-color: gray;
border-top: solid;
border-top-color: gray;
text-align: center;
height: 100px;
}
section{
text-align: center;
margin: 0px 0px 50px 0px;
}
#menu{
width: 100%;
border-style: solid;
border-width: 1px 1px 1px 1px;
text-align: center;
}
a{
text-decoration: none;
color: black;
}
a:hover{
background-color: rgb(210,210,210);}
</style>
</head>
<body>
<div class="fix">
<img src="maple-leaf.jpg" style="width: 70px; height: 70px;float:left;">
<h1>Design of a Neural Network Model for Classification of Leaves</h1>
<nav id="menu">
<a href="index.html">Home </a>|
<a href = "https://github.com/kunwarshivam/Classification-of-leaves-Caffe-python">GitHub Page</a>|
<a href = "https://www.linkedin.com/in/kunwarshivam">LinkedIn: Kunwar Shivam Srivastav</a>|
<a href = "https://www.linkedin.com/in/mathew-mithra-noel">LinkedIn: Mathew M. Noel</a>|
</nav>
</div>
<section>
<br><br><br>
<br>
<p id="project_details" style="text-align:left;">
 This project,<b> Design of a Neural Network Model for Classification of Leaves</b>, has been completed by <em>13BEE0084, Kunwar Shivam Srivastav</em> as a part of final year project
under the guidance of <em>Dr. Mathew M. Noel</em> of <em>School of Electrical Engineering(SELECT)</em> of <em>VIT University, Vellore.</em> <br>
</p>
<li style="text-align:left;">
Datasets used:<br>
<ol><a src="http://leafsnap.com/dataset/" style="text-decoration:underline;">LeafSnap-Dataset</a></ol>
<ol><a src="http://cs-chan.com/downloads_MKLeaf_dataset.html" style="text-decoration:underline;">Malaykew Leaf Dataset</a></ol>
</li>
<p style="text-align:center; border-style:solid; border-width: 1px 1px 1px 1px; border-color:gray;">
<b>Image:</b><br>
<br>
<img src="abcd/image.jpg" style="width:227px; height:227px;margin: 0px 0px 50px 0px;">
<br>
</p>
<br>
<p style="text-decoration: underline;">
This leaf belongs to, or is most similar to: <br>
</p>
<p id="output">
<?php $class = substr($_SESSION['output'], 16969); echo "<b>$class</b>"; session_unset();session_destroy();?>
</p>
<br>

</form>
<html>
<body>
<p style="border-style:solid;border-color:gray;">
Thank You.
</p>
</body>
</html>
