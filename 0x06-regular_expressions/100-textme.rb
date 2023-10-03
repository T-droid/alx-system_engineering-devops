#!/usr/bin/env ruby
paragraph = ARGV[0]

sender_match = paragraph.match(/from:\s*([a-zA-Z0-9+]+).*$/i)
receiver_match = paragraph.match(/to:\s*([+1-9]+).*$/i)
flags_match = paragraph.match(/flags:\s*([0-1\-:]+).*$/i)

sender = sender_match ? sender_match[1] : "Sender not found"
receiver = receiver_match ? receiver_match[1] : "Receiver not found"
flags = flags_match ? flags_match[1] : "Flags not found"

puts "#{sender}, #{receiver}, #{flags}"
