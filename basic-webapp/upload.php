<?php
session_start();
header("Location: index.php");
?>
<html>
<body>
<p id="some_div"></p>
<script>
var timeLeft = 5;
var elem = document.getElementById('some_div');
var timerId = setInterval(countdown, 1000);
countdown();
function countdown() {
  if (timeLeft == 0) {
    clearTimeout(timerId);
  } else {
    elem.innerHTML = timeLeft + ' seconds remaining';
    timeLeft--;
  }
}
</script>
<?php
$target_dir = "abcd/";
exec('rm abcd/*jpg');	
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = pathinfo($target_file,PATHINFO_EXTENSION);
// Check if image file is a actual image or fake image
if(isset($_POST["submit"])) {
    $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
    if($check !== false) {
        echo "File is an image - " . $check["mime"] . ".";
        $uploadOk = 1;
    } else {
        echo "File is not an image.";
        $uploadOk = 0;
    }
}
// Check if file already exists
if (file_exists($target_file)) {
    echo "Sorry, file already exists.";
    $uploadOk = 0;
}
// Check file size
if ($_FILES["fileToUpload"]["size"] > 5000000) {
    echo "Sorry, your file is too large.";
    $uploadOk = 0;
}
// Allow certain file formats
if($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg"
&& $imageFileType != "gif" ) {
    echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
    $uploadOk = 0;
}
// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
    echo "Sorry, your file was not uploaded.";
// if everything is ok, try to upload file
} else {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        echo "The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded.";
       exec('mv abcd/*.jpg abcd/image.jpg');	
	$_SESSION["output"]=shell_exec('python predict.py 2>&1'); 
	   echo '<br><a href="index.php">Click here after timer stops to see results...</a>';

    } else {
print_r($_FILES) ;
        echo "Sorry, there was an error uploading your file.";
    }
}
?>
</body>
</html>
