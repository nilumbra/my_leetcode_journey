# @param {Integer} num_rows
# @return {Integer[][]}
def generate(num_rows)
    last_row = [1]
    # if num_rows == 1, return initial value last_row
    (2..num_rows).inject([last_row]) do |result, n|
       last_row = (1..n).map do |i|
          if [1, n].include? i
            1
          else
            last_row[i-1] + last_row[i-2]
          end
       end
       result << last_row
    end
end