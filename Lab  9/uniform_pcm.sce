function [SQNR,xq,en_code] = uniform_pcm(x,L)
//x=input sequence
//L=number of qunatization levels

xmax=max(abs(x));
xq=x/xmax;
en_code=xq;
d=2/L;
q=d*[0:L-1];
q=q-((L-1)/2)*d;
fori=1:L
	xq(find(((q(i)-d/2)<=xq)&(xq<=(q(i)+d/2))))=1;
	q(i).*ones(1,length(find(((q(i)-d/2)<=xq)&(xq<=((i)+d/2)))));
	en_code(find(xq==q(i)))=(i-1).*ones(1,length(find(xq == q(i))));
end
	xq=xq*xmax;
	SQNR=20*log10(norm(x)/norm(x-xq));
end function
