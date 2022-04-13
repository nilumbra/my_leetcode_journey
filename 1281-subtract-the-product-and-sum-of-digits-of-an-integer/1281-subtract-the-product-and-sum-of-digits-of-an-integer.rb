# @param {Integer} n
# @return {Integer}
def subtract_product_and_sum(n)
    sum, prod = 0, 1
    place = 0
    until n == 0 do
        r = n % (10 ** (place + 1))
        digit = r / (10 ** place)
        sum += digit
        prod *= digit
        n = n - r
        
        place += 1
    end
    
    prod - sum
end