def total_steps(file_name: "input.txt")
  file_path = File.join(__dir__, file_name)
  f = File.open(file_path)

  sequence = f.readline.strip
  f.readline

  network = Hash.new
  for line in f
    add_network(network, line)
  end
  
  steps = traverse_network(network, sequence)

  steps
end

def ghost_total_steps(file_name: "input.txt")
  file_path = File.join(__dir__, file_name)
  f = File.open(file_path)

  sequence = f.readline.strip
  f.readline

  network = Hash.new
  for line in f
    add_network(network, line)
  end

  steps = ghost_traversal(network, sequence)

  steps
end

def add_network(network, line)
  source, dest = line.split('=').map(&:strip)
  left, right = dest[1..-2].split(',').map(&:strip)

  network[source] = [left, right]
end

def traverse_network(network, sequence)
  direction = {
    "L": 0,
    "R": 1
  }

  sequence_length = sequence.length
  current_node = "AAA"
  step = 0

  while current_node != "ZZZ"
    next_direction = direction[sequence[step % sequence_length].to_sym]
    current_node = network[current_node][next_direction]

    step += 1
  end

  return step
end

def ghost_traversal(network, sequence)
  direction = {
    "L": 0,
    "R": 1
  }
  
  current_nodes = network.keys.select { |node| node[-1] == 'A' }
  nodes_n = current_nodes.length
  step = 0
  finished_nodes = 0

  while finished_nodes != nodes_n
    next_direction = direction[sequence[step % sequence.length].to_sym]
    step += 1
    finished_nodes = 0
    current_nodes.each_with_index do |node, i|
      next_node = network[node][next_direction]
      pp next_node if next_node == 'LQZ'
      finished_nodes += 1 if next_node[-1] == 'Z'
      current_nodes[i] = next_node
    end
  end

  step
end



print "Total steps: #{total_steps}"
#print "Ghost total steps: #{ghost_total_steps}"
