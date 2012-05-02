# -*- coding: utf-8 -*- 
<%inherit file="base.mako"/>
<%def name="head_tags()">
    <title>Barter Vegas Tech: Reset Password</title>
</%def>
<%def name="body()">

    <span id='message'>${message}</span>
    <form action="/reset" method="post">
    	<input type="hidden" name="code" value="${forgot}"/>
        <label for="password">Password:</label> <input type="password" name="password" value=""/><br/>
        <label for="password">Confirm:</label> <input type="password" name="confirm" value=""/><br/>
        <input type="submit" name="reset-password" value="Reset Password"/>
      </form>


</%def>

 <%def name="navlinks()">
 					<li><a href="/" title="Home">Home</a></li>
					
					<li><a href="/about" title="About #VegasTech">About</a></li>
					
%if request.session.get('logged_in') != None and request.session.get('logged_in') >= 0:
										
						<li><a href="/account" title="Account" >Account</a></li>
						
						<li><a href="/user/logout" title="Logout">Logout</a></li>
%else:										
						<li><a href="/users" title="User Section">Users</a></li>
					
						<li><a href="#" title="User Login" id="navbar-login-btn" data-reveal-id="login-modal" data-animation="fade" class="small button nice radius blue">Login</a></li>
%endif	
 </%def>