module BoxLid() {
    difference() {
       // Espessura da caixa
       cube([ 42.5, 62.5, 33/3], center = true); 
       // Interior
       translate([0,0,1.5]) cube([41, 61, 31.5/3], center = true);
    }     
}
BoxLid();