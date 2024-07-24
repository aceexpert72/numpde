function f = fam(a)
    function y=fx(x)
        y=exp(a.*x);
    end
f=@fx;
end

