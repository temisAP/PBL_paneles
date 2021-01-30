Alt_p=400;

Long_p = 400;

Offset_Y =5;

Offset_X =12;

Hinge_Dim_X = 2*9;

Cupon_Cells =10;

Cell_Dim_X = 80; 

Cell_Dim_Y = 40;

max_Cupon_N_Y = floor((Alt_p - 2*Offset_Y+4)/(Cell_Dim_Y*Cupon_Cells+(Cupon_Cells-1)*1+4));

max_Cupon_Cells = floor((Alt_p -2*Offset_Y + 1)/(40+1));

max_Cupon_N_X = floor((Long_p + 1-2*Hinge_Dim_X-2*Offset_X)/(Cell_Dim_X+1));