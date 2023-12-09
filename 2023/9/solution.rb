def prediction_sum(file_name: "input.txt")
  file_path = File.join(__dir__, file_name)
  f = File.open(file_path)

  sum = 0

  for line in f
    history = parse_line(line)
    sequences = difference_sequences(history)
    sum += extrapolate_value(sequences)
  end
  
  f.close

  sum
end

def backward_prediction_sum(file_name: "input.txt")
  file_path = File.join(__dir__, file_name)
  f = File.open(file_path)

  sum = 0

  for line in f
    history = parse_line(line)
    sequences = difference_sequences(history)
    sum += extrapolate_backward_value(sequences)
  end
  
  f.close

  sum
end

def extrapolate_value(sequences)
  n = sequences.length
  prev_value = 0
  for i in 0...n
    sequence = sequences[n - i - 1]
    prev_value = prev_value + sequence[-1]
  end

  prev_value
end

def extrapolate_backward_value(sequences)
  n = sequences.length
  prev_value = 0
  for i in 0...n
    sequence = sequences[n - i - 1]
    prev_value = sequence[0] - prev_value
  end

  prev_value
end

def difference_sequences(history)
  sequences = [history]

  until indifferent?(sequences[-1])
    sequences << differences(sequences[-1])
  end

  sequences
end

def parse_line(line)
  line.strip.split.map(&:to_i)
end

def differences(history)
  differences = []
  for i in 1...history.length
    differences << history[i] - history[i - 1]
  end

  differences
end

def indifferent?(differences)
  differences.all?(&:zero?)
end

puts "Forward prediction sum: #{prediction_sum}"
puts "Backward prediction sum: #{backward_prediction_sum}"
