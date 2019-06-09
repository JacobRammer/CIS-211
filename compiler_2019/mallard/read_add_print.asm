# Lovingly crafted by the robots of CIS 211 2019W
# 2019-06-05 19:25:22.123419 from mallard/read_add_print.mal
#
   LOAD  r12,r0,r0[510]
   STORE  r12,var_x
   LOAD  r12,r0,r0[510]
   STORE  r12,var_y
    LOAD r13,var_x
    LOAD r12,var_y
   ADD  r13,r13,r12
   STORE  r13,r0,r0[511]
	HALT  r0,r0,r0
var_x: DATA 0
var_y: DATA 0
