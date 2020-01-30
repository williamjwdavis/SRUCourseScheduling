<!DOCTYPE html> 
<html> 
<head> 
<title>Academic scheduling</title> 
<style type="text/css">.field {display: inline-block;}</style>
</head>

<body>

<?php
function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
?>


<form method="post" autocomplete="off" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
<p id="par1"></p>
<button type="button" onclick="hello()">Add class</button> 
<input type="hidden" name="hidden1" id="hidden1">
<input type="submit" value="Done adding classes">
</form>



<script type="text/javascript">


var ii=0;
var text="";
function hello()
{
  ii=ii+1;
  jj=ii+1;
document.getElementById("par"+ii).innerHTML +=
  '<br><fieldset class="field">'+ 
  'Course name: <input type="text" name="courseName'+ii+'" maxlength="20" size="20"><br><br>'+ 
  'Number of credits: <input type="text" name="credits'+ii+'" maxlength="1" size="1"><br><br>'+ 
  'Expected enrollment: ' +
  'Min: <input type="text" name="minEnrollment'+ii+'" maxlength="4" size="4"> '+ 
  'Max: <input type="text" name="maxEnrollment'+ii+'" maxlength="4" size="4"><br><br>'+ 
  'Number of days class meets: ' +
  'Min: <input type="text" name="minDaysClassMeets'+ii+'" maxlength="1" size="1"> '+ 
  'Max: <input type="text" name="maxDaysClassMeets'+ii+'" maxlength="1" size="1"><br><br>'+
  'Can class meet more than once per day? '+ 
  '<input type="radio" name="oncePerDay'+ii+'" value="Yes"> Yes '+ 
  '<input type="radio" name="oncePerDay'+ii+'" value="No" checked> No'+
  '</fieldset>'+
  '<p id="par'+jj+'"></p>';

  document.getElementById("hidden1").value = ii;	
  
}


</script>





<?php
$numCourses = $_POST["hidden1"]; 
?>


<?php
$courseName = Array(); for ($i = 1; $i <= $numCourses; ++$i) {$courseName[$i] = test_input($_POST["courseName" .$i]);}
$credits = Array(); for ($i = 1; $i <= $numCourses; ++$i) {$credits[$i] = $_POST["credits" .$i];}
$minEnrollment = Array(); for ($i = 1; $i <= $numCourses; ++$i) {$minEnrollment[$i] = $_POST["minEnrollment" .$i];}
$maxEnrollment = Array(); for ($i = 1; $i <= $numCourses; ++$i) {$maxEnrollment[$i] = $_POST["maxEnrollment" .$i];}
$minDaysClassMeets = Array(); for ($i = 1; $i <= $numCourses; ++$i) {$minDaysClassMeets[$i] = $_POST["minDaysClassMeets" .$i];}
$maxDaysClassMeets = Array(); for ($i = 1; $i <= $numCourses; ++$i) {$maxDaysClassMeets[$i] = $_POST["maxDaysClassMeets" .$i];}
$oncePerDay = Array(); for ($i = 1; $i <= $numCourses; ++$i) {$oncePerDay[$i] = $_POST["oncePerDay" .$i];}
?>





<?php
$myfile = fopen("newfile.txt", "w");

for ($i = 1; $i <= $numCourses; ++$i) {fwrite($myfile, $courseName[$i] . "\n");}
for ($i = 1; $i <= $numCourses; ++$i) {fwrite($myfile, $credits[$i] . "\n");}
for ($i = 1; $i <= $numCourses; ++$i) {fwrite($myfile, $minEnrollment[$i] . "\n");}
for ($i = 1; $i <= $numCourses; ++$i) {fwrite($myfile, $maxEnrollment[$i] . "\n");}
for ($i = 1; $i <= $numCourses; ++$i) {fwrite($myfile, $minDaysClassMeets[$i] . "\n");}
for ($i = 1; $i <= $numCourses; ++$i) {fwrite($myfile, $maxDaysClassMeets[$i] . "\n");}
for ($i = 1; $i <= $numCourses; ++$i) {fwrite($myfile, $oncePerDay[$i] . "\n");}

fclose($myfile);
?>

</body> 
</html>