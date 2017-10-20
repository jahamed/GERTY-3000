unless ARGV[0] then
  raise "No file specified. Please pass a file path as an argument"
end

path = ARGV[0]

file = File.open("#{path}", "rb")
contents = file.read
contents = contents.encode('utf-8', 'utf-8')

contents = contents.gsub(/\r\n/, ' ')
contents = contents.gsub(/[\u201c\u201d]/, '\"')
contents = contents.gsub('\"', '""')
puts contents