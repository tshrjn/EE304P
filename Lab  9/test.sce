n=4;      
a=zeros(5,1);
a(1)=-150;
a(3)=0;
a(5)=150;
delta=.9957;
 for i=1:1:2
    a(3-i)=a(3)-i*(delta);
    a(3+i)=a(3)+i*(delta);
end

x_i=zeros(4,1);
for i=1:1:n
    x_i(i)=a(2)+(i-3/2)*delta;
end

x=[0 0:.001:1];
func=x_i(n)*sin(2*3.1416*50*x);
[r,c]=size(func);
y=zeros(r,c);
yprime=zeros(r,c);
//yprime(1)=0;
//y(1)=0;
xrecon=zeros(r,c);

func(1)=0;
Qvalue=zeros(r,c);
Qlevel=zeros(r,c);
nu=log2(n);

//    [Qvalue(i),level(i)]=Quant(a,x_i,func(i));
//    bin(i,:)=dec2bin(level(i),nu);
//end
//
//
//MS_PCM=MeanSquare(func,Qvalue);
    [y(i),level(i)]=Quant(a,x_i,(func(i)-yprime(i-1)));
    yprime(i)=y(i)+yprime(i-1);           
    bi(i,:)=dec2bin(Qlevel(i),nu);
end

y
xrecon(1)=0;

for i=2:1:c
//    [xrecon(i)]=reciever(y(i),xrecon(i-1));
    [xrecon(i)]=reciever_bin(bi(i,:),xrecon(i-1),x_i(1));      ///            reconstructed signal
end
MS_DPCM=0;
for i=1:1:c
    MS_DPCM=MS_DPCM+(func(i)-xrecon(i))^2;
end

 MS_DPCM=MS_DPCM/c
////////////////////////////////////////////////////////////////////////////////////////////////////

x=[0 0:.00005:.25];
func=x_i(n)*sin(2*3.1416*50*x);

[maxval maxind]=max(func);
[minval minind]=min(func);
delta=abs((maxval-minval)/(maxind-minind));
[r,c]=size(func);
deltax=zeros(r,c);
deltax(1)=0;
deltabit=zeros(r,c);
deltabit(1)=1;
func(1)=0;
//delta=.25;

for i=2:1:c
    [deltabit(i)]=delMod(func(i),func(i-1));
end

for i=1:1:c
    [deltax(i)]=del_rec(deltabit,i,delta);
end

MS_Delta=MeanSquare(func,deltax)

MS_Delta=0;
for i=1:1:c
    MS_Delta=MS_Delta+(func(i)-deltax(i))^2;
end
MS_Delta=MS_Delta/c

///////////////////////////////////////////////////////////////////////////////////////////////////////////
