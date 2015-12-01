function [levelNos, xq,ql,qv] = quantise (x, mx,mn, l )
    s = (mx - mn )/l;
    ql = [mn:s:mx];
    qv = [mn-s/2: s : mx +s/2];
    index = 1;
    
    levelNos = [];
    xq = [];
    
    while index  <=  length(x)
        count = 1;
        while count <= length(ql)
            if (x (index) > ql(count) ) then
                count = count + 1;
                continue;
            else
                levelNos(1,index) = count;
                xq(1,index)  =  qv(count);
                break;
            end
        end
//        disp( levelNos(1,index),xq(1,index),x(1,index) );
        index = index +1;
    end
endfunction

function [levelNos, xq,ql,qv] = reconstruct_fn (x, mx,mn, l )
    s = (mx - mn )/l;
    ql = [mn:s:mx];
    qv = [mn-s/2: s : mx +s/2];
    index = 1;
    
    levelNos = [];
    xq = [];
    
    while x(1,index)  <=  length(x)
        count = 1;
        while count <= length(ql)
            if (x (index) > ql(count) ) then
                count = count + 1;
                continue;
            else
                levelNos(1,index) = count;
                xq(1,index)  =  qv(count);
                break;
            end
        end
//        disp( levelNos(1,index),xq(1,index),x(1,index) );
        index = index +1;
    end
endfunction

// Input

fs = 100;
fm = 5;
time = [0:1/fs:5/fm];
input = sin(2*%pi* fm * time);


mx = 150;
mn =-150;

//Main

input = mx*input;

//Taking differences
y = input;
for i = 2:length(y)
    y(i) = y(i) - y(i-1);
end

[mx,mxind] = max(y);
[mn,mnind] = min(y);
[levelNos, xq,ql,qv] = quantise (y, mx,mn, 4 ); 
y = levelNos;

txSignal = dec2bin(y);
//Reconstruction 

z = bin2dec(txSignal);
z(1) = qv(z(1))/5
for i = 2:length(z)
    z(i) = z(i-1) + qv(z(i))
end

recons = z

// Mean Square Error   Calculations
sm = 0;
for i = 1:length(input)
    sm = sm + (input(i) - recons(i))^2;
end
sm = sm / length(input);
disp(sm);
plot(input);
plot(recons);
