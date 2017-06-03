function MAX = ltov(tot,dep,thresh,term,apr,fee)




if isempty(fee); fee = 0;   end
if isempty(term);term = 25; end
if isempty(tot); tot = 1e5:5e5; end

loan = tot - dep;
rat  = (loan./tot)*100;
plot(tot,rat,'r','LineWidth',3);

if nargin > 2
    hold on;
    i   = findthenearest(rat,thresh);
    MAX = tot(i);
    refline([0 rat(i)]);
    title(sprintf('%d%% loan to value = %d house',round(thresh),MAX));
end

if nargin == 6
    loan    = MAX - dep;
    adjloan = loan + (loan*(apr*.01)) + fee;     
    repay   = adjloan / (term*12);
    
    MAX.HouseVal = MAX;
    MAX.Repayments = repay;
end