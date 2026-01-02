from solid import *
from solid.utils import *

R_bmb = 30


def b(H, R):
    yari = up(7.5 * R)(rotate([70, 0, 0])(cube([100 * R, 100 * R, 3 * R], center=True)))
    saki = cylinder(h=200, r=R) - cylinder(h=200, r=R - 3) - yari
    fushi = cylinder(h=3, r=R + 3)
    tsutsu = cylinder(h=H, r=R) - cylinder(h=H, r=R - 3)
    if H > 100:
        return tsutsu + up(H / 2)(fushi) + up(H)(fushi) + up(H)(saki)
    else:
        return tsutsu + up(H)(fushi) + up(H)(saki)


output_f = (
    translate([0, (R_bmb + 3) * (3**0.5) / 2, 0])(b(200, R_bmb))
    + translate([R_bmb + 3, -(R_bmb + 3) * (3**0.5) / 2, 0])(b(100, R_bmb))
    + translate([-R_bmb - 3, -(R_bmb + 3) * (3**0.5) / 2, 0])(b(100, R_bmb))
)
output_f = (
    up(100)(output_f)
    + translate([0, -8, 0])(cylinder(h=100, r=2 * (R_bmb + 5)))
    + translate([0, -8, 30])(cylinder(h=10, r=2 * (R_bmb + 7)))
    + translate([0, -8, 90])(cylinder(h=10, r=2 * (R_bmb + 7)))
)

for i in range(72):
    output_f += translate([0, -8, 0])(
        rotate([0, 0, 5 * i])(translate([0, 2 * (R_bmb + 5), 0])(cylinder(h=140, r=3)))
    )

scad_render_to_file(output_f, "cadmatsu.scad")
