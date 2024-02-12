<html>
    <body>
        <h3>Common Elements are:</h3>
        <?php
$a = array('a','c','d','g','i');
$b = array('x','z','n','k','d','i','a','m','n');
$result = array_intersect($a, $b);
// print_r($result);
foreach ($result as $value) {
    echo "$value";
    echo "<br>";
}

?>
</body>
</html>
