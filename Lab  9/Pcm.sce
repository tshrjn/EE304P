//PCM Encoding
function [ c ] = PCM_Encoding (x ,L , en_code )
 // Encoding: Converting Quantized decimal sample values into binary
//x=input sequence
//L=number of qunatization levels
//encode=normalized input sequence
n = log2(L) ;
c = zeros( length(x), n);
for i = 1:length(x)
	for j = n : -1:0
		 if( fix( en_code(i ) /(2^j)) == 1)
			 c(i ,(n - j)) =1;
			 en_code(i) = en_code(i) - 2^j;
		 end
	end
 end
 disp (c)

PCM Transmission
1//Caption: PCM Transmission ( includes functions : 
uniform_pcm.sce, PCM_encoding.sce)
2//This program is a sample program for Pulse Code
Modulation transmission
3//step 1 :The given analog signal converted into
quantized sampl evalue
4//step 2: Then thequantized sample value converted
into binaryvalue
5 clc ;
6 close ;
7 t = 0:0.001:1;
8 x = sin (2* %pi * t ) ;
9 L = 16;
10 // S t e p 1
11 [ SQNR , xq , en_code ] = uniform_pcm (x , L ) ;
12 // S t e p 2
13 c = PCM_Encoding (x ,L , en_code ) ;
14 a = gca () ;
15 a . x_location =” o r i g i n ”;
16 a . y_location =” o r i g i n ”;
17 plot2d2 ( t *2* %pi , x ) ;
18 plot2d2 ( t *2* %pi , xq ,5) ;
19 title ( ’ Q u a n t i z a t i o n of Sampled a n al o g s i g n a l ’ )
20 legend ([ ’ Analog s i g n a l ’ , ’ Q ua n ti z e d S i g n a l ’ ])
Scilab code ARC 8 sinc new
1 function [ y ]= sinc_new (x )
2 i = find ( x ==0) ;
3 x ( i ) = 1; // From LS : don ’ t need t h i s i s /0
wa r ni ng i s o f f
4 y = sin ( %pi * x ) ./( %pi * x ) ;
5 y ( i ) = 1;
6 endfunction
111
Scilab code ARC 9 uniform pcm
1 function [ SQNR , xq , en_code ] = uniform_pcm (x , L )
2 // x = i n p u t s e q u e n c e
3 //L = number of q u n a t i z a t i o n l e v e l s
4 xmax = max( abs ( x ) ) ;
5 xq = x/ xmax ;
6 en_code = xq ;
7 d = 2/ L ;
8 q = d *[0: L -1];
9 q = q -(( L -1) /2) * d ;
10 for i = 1: L
11 xq ( find ((( q ( i ) -d /2) <= xq ) &( xq <=( q ( i ) + d /2) )) ) =...
12 q ( i ) .* ones (1 , length ( find ((( q ( i ) -d /2) <= xq ) &( xq <=(
q ( i ) + d /2) ) ) ) ) ;
13 en_code ( find ( xq == q ( i )) ) = (i -1) .* ones (1 , length (
find ( xq == q ( i ) ) ) ) ;
14 end
15 xq = xq * xmax ;
16 SQNR = 20* log