o <?php
    error_reporting(0);
    $x = 1000;
    extract($_GET);
    $arr = array();
    $anim="bison|dolphin|eagle".
    "pony|ape|cow|monkey|lobster".
    "duck|deer|spider|rabbit|turkey";

    $animals = explode("|", $anim);
    shuffle($animals);
    foreach($animals as $animal){
        $arr[$x++] = $animal;
    }
    
    if(preg_match("/([0-9]|[a-z])/i", $q1))
    {
         die("");
    }
    if(preg_match("/([0-9]|[a-z])/i", $q2)){

     die("");
    }
    $p = strcmp($arr[strlen($anim)^strlen($x)][3],"k");
    echo $arr[strlen($anim)^strlen($x)][3];
    if(strcmp($p, (int)"spider") == "rabbit"){
        if((int)($q1^$q2) === strlen($x)){
            include 'flag.php';
           class B {
             function __destruct() {
               echo "pretty close";
                                }
                              }
          if (isset($part2)) {
                echo "uHMMM";
                ob_start();
                echo "congratulation : " . $flag . "\n";
                $a = unserialize($part2);
                ob_end_clean();
                               }


        }
    }
    
    show_source(__FILE__);
?>