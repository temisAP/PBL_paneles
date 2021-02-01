clc;
close all;
clear all;

%% PARAMETROS

% Tiempos
ts = 1;         % s
td = 10;        % s
to1 = 10;       % s
to2 = 5;        % s
to3 = 10;       % s
to4 = 5;        % s

tt = ts + td + to1 + to2 + to3 + to4;

% Distancias y giros
ds = 8;         % mm
gd1 = 90;       % deg
gd2 = 180;      % deg
go1 = 90;       % deg
go2 = 135;      % deg
go3 = 45;       % deg
go4 = 90;       % deg


%% Construir leyes

step = 10;

% Mecanismo de suelta
suelta = linspace(0,ds,ts*step+1);

% Mecanismo de despliegue
desp_1 = linspace(0,gd1,td*step+1);
desp_2 = linspace(0,gd2,td*step+1);

% Mecanismo de orientacion
ori_1 = linspace(0,go1,to1*step+1);
ori_2 = linspace(go1,go2,to2*step+1);
ori_3 = linspace(go2,go3,to3*step+1);
ori_4 = linspace(go3,go4,to4*step+1);
ori = [ori_1(1:end-1), ori_2(1:end-1), ori_3(1:end-1), ori_4];
    
N = length([suelta, desp_1, ori]) - 2;
t = linspace(0, tt, N);

z_s = zeros(1,(N-length(suelta)));
z_d = zeros(1,(length(z_s)-length(desp_1)));
z_o = zeros(1,(length(suelta)+length(desp_1)-2));

suelta = [suelta, (z_s + ds)];
desp_1 = [zeros(1,N-length(z_s)), desp_1, (z_d + gd1)];
desp_2 = [zeros(1,N-length(z_s)), desp_2, (z_d + gd2)];
ori = [z_o, ori];


%% Plots
figure()
    plot(suelta)

figure()
    hold on
    plot(desp_1)
    plot(desp_2)
    
figure()
   plot(ori)
   
leyes = [{suelta},{desp_1},{desp_2},{ori}];

   
%% EXPORTAR DXFs
% Cargar archivo xls con datos de sensores
archivo = [{'Suelta'},{'Despliegue_1'}, {'Despliegue_2'}, {'Orientacion'}];
path = 'Ley_DXF\';

for i = 1:length(leyes)

    % Guardar el sensor i en un archivo dxf
    FID = dxf_open([path archivo{i} '.dxf']);
    x = t'; 
    y = leyes{i}'; 
    z = zeros(size(x));
    dxf_polyline(FID,x,y,z);
    dxf_close(FID);

end