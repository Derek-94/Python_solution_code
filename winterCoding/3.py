def count_flavor(cakes, row_start, row_end, col_start, col_end):
    flavors = '';
    for i in range(row_start, row_end):
        flavors += cakes[i][col_start:col_end];
    return len(set(flavors))

def solution(cakes, cut_rows, cut_columns):
    answer = 0;
    
    total_pieces = (len(cut_rows) + 1) * (len(cut_columns) + 1);
    
    cut_rows.insert(0, 0);
    cut_rows.append(len(cakes));
    cut_columns.insert(0, 0);
    cut_columns.append(len(cakes));
    
    for i in range(len(cut_rows) - 1):
        row_start = cut_rows[i];
        row_end = cut_rows[i + 1];
        for j in range(len(cut_columns) - 1):
            col_start = cut_columns[j];
            col_end = cut_columns[j + 1];
            answer = max(count_flavor(cakes, row_start, row_end, col_start, col_end), answer);
    
    return answer