class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = sum((l * l for x, y, l in squares))
        events = [(y, 1, l) for x, y, l in squares] + [(y + l, 0, l) for x, y, l in squares]
        events.sort()

        combined_width = 0
        curr_area = 0
        prev_height = 0
        for i in range(len(events)):
            y, start, l = events[i]
            height_diff = y - prev_height

            area_diff = combined_width * height_diff
            if curr_area + area_diff >= total_area / 2:
                # curr_area + (combined_width * optimal_height_diff) = total_area / 2
                optimal_height_diff = (total_area / 2 - curr_area) / combined_width
                return prev_height + optimal_height_diff
            
            combined_width += l if start else -l
            curr_area += area_diff
            prev_height = y