#!/usr/bin/env ruby
#puts ARGV[0].match(/\[from:(\w+)\]\s\[to:([^w]?\w+)\]\s\[flags:([^w?]\d:[^w?]:[^w?]\d:\d:[^w]\d)\]/)
match_data = ARGV[0].match(/\[from:([^w]?\w+)\]\s\[to:([^w]?\w+)\]\s\[flags:([^w]?\d:[^w]?\d*:[^w]?\d:[^w]?\d:[^w]?\d)\]/)

if match_data
  sender = match_data[1]
  receiver = match_data[2]
  flags = match_data[3]

  puts "#{sender},#{receiver},#{flags}"
end
