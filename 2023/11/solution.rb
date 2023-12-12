class GalaxyObservation
  def initialize(file_name: "input.txt")
    parse_image
  end

  def distance_pair_sums(expand_factor: 1)
    locations = galaxy_locations(expand_factor:)
    num_galaxies = locations.length
    
    pairs_sum = 0

    for i in 0...num_galaxies
      current_row, current_col = locations[i]
      for j in (i + 1)...num_galaxies
        other_row, other_col = locations[j]
        distance = (current_row - other_row).abs + (current_col - other_col).abs
        pairs_sum += distance
      end
    end

    pairs_sum
  end

  def galaxy_locations(expand_factor: 1)
    # Subtract 1 since we're already tracking the original indices 
    expand_factor -= 1

    er = empty_rows(@grid)
    ec = empty_cols(@grid)

    locations = []
    
    er_seen = 0
    for row in 0...@grid.length
      er_seen += expand_factor if er.include?(row)
      ec_seen = 0
      for col in 0...@grid[0].length
        ec_seen += expand_factor if ec.include?(col)
        locations << [row + er_seen, col + ec_seen] if @grid[row][col] == '#'
      end
    end

    locations
  end

  def parse_image(file_name: "input.txt")
    file_path = File.join(__dir__, file_name)
    f = File.open(file_path)

    @grid = []

    for line in f 
      @grid << line.strip
    end
    
    f.close

    @grid
  end

  def empty_rows(grid)
    set = Set.new

    for row in 0...grid.length
      set << row unless grid[row].include?("#")
    end

    set
  end

  def empty_cols(grid)
    set = Set.new

    for col in 0...grid[0].length
      empty = true
      for row in 0...grid.length
        if grid[row][col] != '.'
          empty = false
          break
        end
      end
    
      set << col if empty
    end

    set
  end
end

go = GalaxyObservation.new
print "Distance pair sums: #{go.distance_pair_sums}\n"
print "Bigger distance pair sums: #{go.distance_pair_sums(expand_factor: 1000000)}"
