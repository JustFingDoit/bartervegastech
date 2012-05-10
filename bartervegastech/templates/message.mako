# -*- coding: utf-8 -*- 
<%inherit file="base.mako"/>
<%def name="head_tags()">
    <title>Barter Vegas Tech: Message</title>
</%def>

<%def name="body()">

	<div id="main" class="container">
		
		<div class="row">
		
			<div id="about-main" class="eight columns">
			
				<div class="panel hide-on-phones">
					
					<p class="big">${message}</p>
					
				</div> 				
				<div class="panel show-on-phones">
					
					<p class="big-mobile">${message}</p>
					
				</div> 				
			
			</div> 			
		
		</div>
	</div>

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
