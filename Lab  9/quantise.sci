function xq = quantize ( x , b ,mx,mn)

//      Levels
 l = 2ˆb;

//      StepSize or delta
 s=(mx−mn) / l;

// Quantization levels
 ql = [mn: s :mx ] ;

// Decision Levels
 dl =[mn+( s /2 ) : s :mx];
 index = 1;
 xq = [] ;

 while index <= length(x)
	count =2;
	while count <= length(ql)
		if x(index) > ql(count)
			count = count +1;
			continue
		else
			if x(index) <= dl(count − 1)
				xq(1, index) =  ql(count −1);
			else
				xq(1 ,index ) = ql(count);
			end
		end
		break;
	end
	index = index +1;
 end

 end function