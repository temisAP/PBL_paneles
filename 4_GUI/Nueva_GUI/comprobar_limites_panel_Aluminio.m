Alt_p=400;

Long_p = 400;

Offset_Y =1;

Offset_X =1;

Hinge_Dim_X = 2*9;

Cupon_Cells =10;

Cupon_Dim_X = 84; 

Cupon_Dim_Y =  (Cupon_Cells - 1)*41 + 52;

max_Cupon_N_Y = floor((Alt_p + 1 - 2*Offset_Y)/(Cupon_Dim_Y +1));

max_Cupon_Cells = floor((Alt_p + 41 -52 -2*Offset_Y)/41);

max_Cupon_N_X = floor((Long_p +1-2*Hinge_Dim_X-2*Offset_X)/(Cupon_Dim_X+1));