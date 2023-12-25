class PipeMaze
  NORTH = [-1, 0]
  SOUTH = [1, 0]
  EAST = [0, 1]
  WEST = [0, -1]

  DIRECTIONS = [NORTH, SOUTH, EAST, WEST]

  CONNECT_DIRECTIONS = {
    '|': [NORTH, SOUTH],
    '-': [EAST, WEST],
    'L': [NORTH, EAST],
    'J': [NORTH, WEST],
    '7': [SOUTH, WEST],
    'F': [SOUTH, EAST]
  }

  def pipe_distance(file_name: "input.txt") 
    grid = parse_file_to_grid(file_name)

    start_row, start_col = starting_point(grid)
    starting_pipe = starting_pipe(start_row, start_col, grid)
    grid[start_row] = grid[start_row].sub('S', starting_pipe)

    visited = Set.new
    to_visit = [[start_row, start_col]]
    step = -1

    while !to_visit.empty?
      step += 1
      next_to_visit = Set.new

      while !to_visit.empty?
        point = to_visit.shift
        visited << point
        row, col = point
        pipe = grid[row][col]
        
        for direction in CONNECT_DIRECTIONS[pipe.to_sym]
          row_diff, col_diff = direction
          new_row = row + row_diff
          new_col = col + col_diff

          if valid_index?(new_row, new_col, grid) && !visited.include?([new_row, new_col])
            next_to_visit << [new_row, new_col]
          end
        end
      end

      to_visit = next_to_visit.to_a
    end
    
    enclosed_tiles(visited, grid)
    step
  end

  # TODO: consider squeezing between pipes
  def enclosed_tiles(main_loop, grid)
    outer_tiles = Array.new(grid.length) { Array.new(grid[0].length) { nil } }
    for col in 0...outer_tiles[0].length
      check_outer(outer_tiles, main_loop, grid, 0, col)
      check_outer(outer_tiles, main_loop, grid, grid.length - 1, col)
    end
    
    for row in 0...outer_tiles.length
      check_outer(outer_tiles, main_loop, grid, row, 0)
      check_outer(outer_tiles, main_loop, grid, row, grid[0].length - 1)
    end

    inner_tiles = 0
    for row in 0...outer_tiles.length
      for col in 0...outer_tiles[0].length
        inner_tiles += 1 if outer_tiles[row][col].nil? && !main_loop.include?([row, col])
      end
    end
    print "Inner tiles: #{inner_tiles}"
    inner_tiles
  end

  def check_outer(tiles, main_loop, grid, row, col)
    return unless valid_index?(row, col, grid)
    return unless tiles[row][col].nil?


    tiles[row][col] = true
    
    pp main_loop.include?([row, col])
    if main_loop.include?([row, col])
      return
    end

    for direction in DIRECTIONS
      row_diff, col_diff = direction
      check_outer(tiles, main_loop, grid, row + row_diff, col + col_diff)
    end 
  end

  def parse_file_to_grid(file_name)
    file_path = File.join(__dir__, file_name)
    f = File.open(file_path)
    
    grid = []

    for line in f
      grid << line.strip
    end

    f.close

    grid
  end

  def starting_point(grid)
    grid.each_with_index do |row, i|
      starting_index = row.index('S')
      return [i, starting_index] if starting_index
    end
  end
  
  def starting_pipe(row, col, grid)
    north = false
    south = false
    east = false
    west = false

    north = true if valid_index?(row - 1, col, grid) && ['|', '7', 'F'].include?(grid[row - 1][col])
    south = true if valid_index?(row + 1, col, grid) && ['|', 'L', 'J'].include?(grid[row + 1][col])
    east = true if valid_index?(row, col + 1, grid) && ['-', 'J', '7'].include?(grid[row][col + 1])
    west = true if valid_index?(row, col - 1, grid) && ['-', 'L', 'F'].include?(grid[row][col - 1])

    eligible_connecting_pipe(north: north, south: south, east: east, west: west)
  end

  def eligible_connecting_pipe(north:, south:, east:, west:)
    if north && south
      '|'
    elsif east && west
      '-'
    elsif north && east
      'L'
    elsif north && west
      'J'
    elsif south && west
      '7'
    elsif south && east
      'F'
    end
  end
  

  def valid_index?(row, col, grid)
    row >= 0 && row < grid.length && col >= 0 && col < grid[0].length
  end
end

print "Pipe distance: #{PipeMaze.new.pipe_distance}"


