function [y] = pwfuncv(x)
    y=zeros(1,length(x));
    for i=1:length(x)
        if x(i) <= -1
            y(i)=3;
        elseif x(i)>=2
            y(i)=4*x(i)-8;
        else
            y(i)=-x(i)^2+4;
        end
    end
end
