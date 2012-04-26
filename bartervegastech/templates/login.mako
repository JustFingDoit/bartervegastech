<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
    <title>Login</title>
</head>
<body>
    <span id='message'>${message}</span>
    <form action="/users/login" method="post">
        <label for="username">User name:</label> <input type="text" name="username" value="${username}"/><br/>
        <label for="password">Password:</label> <input type="password" name="password" value="${password}"/><br/>
        <input type="submit" name="login_button" value="Log In"/>
      </form>
</body>
</html>