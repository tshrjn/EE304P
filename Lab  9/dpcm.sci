    delta=.9957;
function [xrec]=reciever(quant,delay)
    xrec=quant+delay;
//    xrec=bin2dec(bit)*delta+x_i+delay;

endfunction

function [xrec]=reciever_bin(bit,delay,x_i)
//    xrec=qua+delay;
    xrec=bin2dec(bit)*delta+x_i+delay;

endfunction


//indicator=1;
function [bit]= delMod(x_high,x_low)
    if x_high > x_low then
        bit=1;
    else
        bit=-1;
    end
endfunction



function [xrec]=delrec(bit,n,delta)
    xrec=0;
    for i=1:1:n
        xrec=xrec+bit(i)*delta;
    end
endfunction


function [Q,level]= Quant(a,x_i,x)
    Q=0;
    level=0;
    [n,r]=size(x_i);
    for i=1:1:n
        if x>=a(i) & x<=a(i+1) then
            Q=x_i(i);
            level=i-1;
            break;
        end
    end
    
endfunction


function [d]= MeanSquare(x,x_i)
    [n,r]=size(x_i);
    d=0;
    for i=1:1:r
            d=d+((x(i)-x_i(i)).^2);
    end
    d=d/r;

endfunction
