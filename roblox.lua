local HS = game:GetService("HttpService")
local ip = "http://localhost:42069"

HS:PostAsync(ip, [[print("hello world!")]])
