%%open and make visible
catia = actxserver('catia.application');
set(catia,'visible',1);
%%get ready to open file
prj_name = 'C:\Users\danie\OneDrive - Universidad Politécnica de Madrid\MUSE\S1\IGA\PBL\PBL_paneles\40\401\401_03.CATProduct';
invoke(get(catia,'Documents'),'Open',prj_name);
doc = get(catia,'activedocument');
rootproduct = get(doc,'product');
mass = get(get(rootproduct,'Analyze'),'Mass');
area = get(get(rootproduct,'Analyze'),'WetArea'); %is in mm3
%%Wont work because of the pass by reference
feature('COM_SafeArraySingleDim', 1)
array = {1;2;3};
invoke(get(rootproduct,'Analyze'),'GetGravityCenter',array);
%%close catia
invoke(catia,'quit');
invoke(catia,'delete');