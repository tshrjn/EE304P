// Functions are defined initially, start reading from THE Main !

function [levelNos,xq] = uniform_quantize ( x , b ,mx,mn)
    //Returns time-domain Quant. levels in decimal format & quatised values
    
//      Levels
 l = 2^b;

//      StepSize or delta or region width
 s = (mx - mn) / l;

// Quantization levels
 ql = [mn: s :mx ] ;
 qv = [mn - (s/2): s : mx + (s/2)]
// Decision Levels
// dl =[mn+( s /2 ) : s :mx];

disp(ql);
disp(qv);
 index = 1;
 xq = [] ;
 levelNos = [];

 while index <= length(x)
	count =2;
	while count <= length(ql)
		if x(index) < ql(1) then
            levelNos(1,index) = 1
            xq(1,index) = qv(1)
        elseif x(index) > ql(count)
			count = count +1;
			continue
		else
			xq(1,index) = qv(count );
			levelNos(1,index) = count ;
			//if x(index) <= dl(count − 1)
			//	xq(1, index) =  ql(count −1);
			//else
			//	xq(1 ,index ) = ql(count);
			//end
		end
		break;
	end
//    disp(x(index));
//    disp(xq(1,index));
//    disp(levelNos(1,index));
	index = index +1;
 end
endfunction


//n=100;
//a=zeros(n+1,1);

//******************** MAIN STARTS HERE *************************************************?
//      Input function 
fs = 100;
fm = 5;
time = [0:1/fs:2/fm];
input = sin(2*%pi*fm*time)
//plot(input)
//      End of input function

n = 4;

//          Setting Boundaries
//a = zeros(n+1);                     // Array of Boundaries
//a(1) = -150
//a(n+1) = 150
//a(floor(n/2)) = 0
//
//******************************************************************* PCM Begins ***************************/
maxBoundary = 150;
minBoundary = -150;

input = maxBoundary*input;
//plot(input)
xq = zeros(length(input));

[levelNos,xq] = uniform_quantize(input,2,maxBoundary,minBoundary);
txSignal = dec2bin(levelNos);
//plot(xq);
//disp(levelNos);
//plot(txSignal);

//plot(txSignal);

//**Channel Modellin here if required*****
//****************************************

// Error checking
sm = 0
for i = 1:length(xq)
    sm = sm + (input(i) - xq(i))^2;
    disp(xq(i) - input(i))
end
sm = sm/ length(xq);
//disp(sm,length(xq),length(input))
disp(sm)
