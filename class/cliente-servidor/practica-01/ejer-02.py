from urllib.parse import urlparse

u = urlparse(
    "https://docs.python.org:443/3/library/socket.html?highlight=bind#socket.socket.bind"
)
print(
    u.scheme,
    "\n",
    u.hostname,
    "\n",
    u.port,
    "\n",
    u.path,
    "\n",
    u.query,
    "\n",
    u.fragment,
)
