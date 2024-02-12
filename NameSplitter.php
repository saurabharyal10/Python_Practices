<?php


$name = array("Trapper Wolf","Cara Dune","Bo-Katan Kryze","Paul Sun-Hyung Lee","Dee Bradly Baker");

foreach ($name as $value) {

$parts = explode(' ', $value);

if (count($parts) === 2) {
    $parts[2] = Null;
    // list($firstname, $lastname) = $parts;

    $firstname = $parts[0];
    echo "First name: ";
    echo trim($firstname); 
    echo"<br>";
    
    $middlename = $parts[2];
    echo "Middle name: ";
    echo trim($middlename);
    echo"<br>";

    $lastname = $parts[1];
    echo "Last name: ";
    echo trim($lastname);
    echo"<br>";
} else if (count($parts) === 3) {
    // list($firstname, $middlename, $lastname) = $parts;
    $firstname = $parts[0];
    echo "First name: ";
    echo trim($firstname); 
    echo"<br>";

    $middlename = $parts[1];
    echo "Middle name: ";
    echo trim($middlename);
    echo"<br>";

    $lastname = $parts[2];
    echo "Last name: ";
    echo trim($lastname);
    echo"<br>";
    }
    echo"<br>";
}

?>