function [c] = PCM_Encoding(x,L,en_code)
//Encoding:Converting Quantized decimal sample values into binary
//x=input sequence
//L=number of qunatization levels
//encode=normalized input sequence
n=log2(L);
c=zeros(length(x),n);
fori=1:length(x)
	forj=n:-1:0
		if(fix(en_code(i)/(2^j))==1)
			c(i,(n-j))=1;
			en_code(i)=en_code(i)-2^j;
		end
	end
end
disp(c)