<?php

$arr = [1, 1, 1, 1, 4, 5, 6];
print_r($arr);
// Array
// (
//     [0] => 1
//     [1] => 1
//     [2] => 1
//     [3] => 1
//     [4] => 4
//     [5] => 5
//     [6] => 6
// )

print_r(array_unique($arr));
// Array
// (
//     [0] => 1
//     [4] => 4
//     [5] => 5
//     [6] => 6
// )