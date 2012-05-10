# -*- coding: utf-8 -*- 
<%inherit file="base.mako"/>
<%def name="head_tags()">
    <title>Barter Vegas Tech: Home</title>
</%def>

 <%def name="body()">
		<div id="home-topper" class="container">
	
		<div class="row">
		
			<div id="topper" class="twelve columns">
			
				<span><strong>Hooray for trading things!</strong></span>
			
			</div> 		
		</div> 	
	</div> 	
					
		<div id="main" class="container">
	
		<div class="row">
		
						<div id="jobs" class="eight columns">
			
				
<div class="panel">
 
<div id="job-list">

	<ul>
	
	        %for listing in listings:
					<li class="list-row" onclick="window.location='${listing.url}';">
			
				<div class="row job-list-row hide-on-phones">
				
					<div class="six columns position">
					
						${listing.title} <span class="white radius round label">${listing.type}</span>
					
					</div>
					
					<div class="three columns category">
					
						${listing.category}
					</div>
					
					<div class="three columns last">
					
						${listing.username}
					</div>
				
				</div> 				
				<div class="mobile-job-list-row show-on-phones position">
				
					<span class="comp">${listing.username}</span>
					${listing.title}
					<br><span class="white radius label">${listing.type}</span>
				
				</div>
				
			</li> 	
			
			%endfor		
 						
	</ul>

</div> </div>			
			</div> 			
						<div id="sidebar" class="four columns hide-on-phones">
				
				<h5>The latest <a href="https://twitter.com/#%21/search/%23VegasTech" id="vt-hash-link-users" class="has-tip tip-top" data-width="180" title="Follow the #VegasTech hashtag on Twitter" target="_blank">#VegasTech</a></h5>
				
				<div id="sidebar-box" class="twitter-feed">

                    <img src="/images/feed-bottom-fade.png" alt="fade" id="feed-bottom-fade">
					
					<iframe src="http://www.hirevegastech.com/twitter.php" name="twitter-feed" id="twitter-feed-iframe" height="420" seamless="seamless" scrolling="no"></iframe>
				
				</div> 				
								<div id="sponsor-notice">
				
					<p>Want to help cover hosting costs?<br />Send BTC to 13PB4zydRkeNLni7nSCBU2piMJsQFE8NEt</p>
				
				</div> 				
			</div> 		
		</div> 	
	</div> 

 </%def>
 
 <%def name="navlinks()">
 					<li><a href="/" title="Home" id="current">Home</a></li>
					
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

