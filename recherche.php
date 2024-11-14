<?php
//connexion
$server="localhost";
$user="root";
$password="";
$database="projet";
$connect=mysqli_connect($server,$user,$password,$database);

//recuperation
$a=$_POST["nom"];

//request
$res=" SELECT * FROM recettes WHERE Nom LIKE '$a' or '$a%' or '%$a' or '%$a%' ";
if(mysqli_query($connect,$res)){
    echo "voila vrai"
}
?>