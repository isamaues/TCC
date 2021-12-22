module Box() {
    difference() {
       // Espessura da caixa
       cube([39.5, 59.5, 30.5], center = true); 
       // Interior
       translate([0,0,1.5]) cube([38, 58, 29], center = true);
       translate([0, 29.75, -7.5 - 3.5 + 11 + 2]) cube([7, 2, 4], center = true);
    }
}

module BoxLid() {
    difference() {
       // Espessura da caixa
       cube([ 42.5, 62.5, 33/3], center = true); 
       // Interior
       translate([0,0,1.5]) cube([41, 61, 31.5/3], center = true);
    }        
}

module VibrationModuleSlot() {
    difference() {
        // Espessura da caixa
        cube([22, 23, 11], center = true);
        // Interior
        translate([0,1,0]) cube([21, 24, 12], center = true); 
    }
}

//apoio caixa de pilhas
translate([10,-26.75,-1.25]) cube([2,6,28], center=true);
translate([-10,-26.75,-1.25]) cube([2,6,28], center=true);

//Alças
translate([38/2 + 7,0,-13.75]) cube([3,43,3], center=true);
translate([32/2 + 7,20,-13.75]) cube([8,3,3], center=true);
translate([32/2 + 7,-20,-13.75]) cube([8,3,3], center=true);

translate([-38/2 - 7,0,-13.75]) cube([3,43,3], center=true);
translate([-32/2  -7,20,-13.75]) cube([8,3,3], center=true);
translate([-32/2 - 7,-20,-13.75]) cube([8,3,3], center=true);   

union() {
    Box();
    //translate ([60,0,-33/3 +1.75]) BoxLid();
    translate([0, 0, -7.5]) VibrationModuleSlot();
}