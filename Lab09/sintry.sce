//xq(find(((q(i)-d/2)<= xq)&(xq<=(q(i)+d/2)))) =
//        q(i).*ones(1,length(find(((q(i)-d/2)<=xq)&(xq<=(q(i)+d/2)))));
//        en_code(find(xq == q(i)))= (i-1).*ones(1,length(find(xq == q(i))));

fs = 10000;
fm = 100;
time = [0: 1.0/fs : 2.0/fm];

//plot(sin(2*%pi*fm*time));
//plot(time);

n = 8 ;
del = 0.586;

input = (3.5*del)*(sin(2*%pi*fm*time)
function ql = quant8(x)
    
    xmax = max(abs(x));
    xq = x / xmax;
//    d = 2/n
    q = del*[0,n-1];
    q = q-((n-1)/2)*d;
    for i = 1:len(x)
        
//        
    end
//    q = q-((L-1)/2)*d;
    for i = 1:len(x)
       
        if (x(i)< ) then
        end
    end
    
endfunction