# -*- coding: utf-8 -*- 
<%inherit file="base.mako"/>
<%def name="head_tags()">
    <title>Barter Vegas Tech: Login</title>
</%def>
<%def name="body()">

    <span id='message'>${message}</span>
    <form action="/users/login" method="post">
        <label for="username">User name:</label> <input type="text" name="username" value="${username}"/><br/>
        <label for="password">Password:</label> <input type="password" name="password" value="${password}"/><br/>
        <input type="submit" name="loginsubmit" value="Log In"/>
      </form>


</%def>

 <%def name="navlinks()">
 					<li><a href="/" title="Home">Home</a></li>
					
					<li><a href="/about" title="About #VegasTech">About</a></li>
					
%if request.session.get('logged_in') != None and request.session.get('logged_in') >= 0:
										
						<li><a href="/account" title="Account" >Account</a></li>
						
						<li><a href="http://www.hirevegastech.com" title="HireVegasTech.com - Free job board for #VegasTech" target="_blank" class="has-tip">Hire</a></li>
						
						<li><a href="/user/logout" title="Logout">Logout</a></li>
%else:										
						<li><a href="/users" title="User Section">Users</a></li>
						
						<li><a href="http://www.hirevegastech.com" title="HireVegasTech.com - Free job board for #VegasTech" target="_blank" class="has-tip">Hire</a></li>
					
						<li><a href="#" title="User Login" id="navbar-login-btn" data-reveal-id="login-modal" data-animation="fade" class="small button nice radius blue">Login</a></li>
%endif	
 </%def>