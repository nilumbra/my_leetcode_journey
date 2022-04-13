# @param {Integer} x
# @param {Integer} y
# @param {Integer[][]} points
# @return {Integer}
def nearest_valid_point(x, y, points)
    min = Float::INFINITY
    min_idx = -1
    points.each_with_index do |point, idx| 
        if point[0] == x || point[1] == y
            manh = (point[0] - x).abs + (point[1] - y).abs
            # puts "#{((point[0] - x).abs + (point[1] - y).abs)} #{min_idx}"
            if point[0] == x && point[1] == y
                return idx
            end
            if point[0] == x && manh < min
                min = manh
                min_idx = idx
            end
            if point[1] == y && manh < min
                min = manh
                min_idx = idx
                # print ((point[0] - x).abs + (point[1] - y).abs), min_idx
            end
        end
    end
    min_idx
end