# -*- coding: utf-8 -*- 
<%inherit file="base.mako"/>
<%def name="head_tags()">
    <title>Barter Vegas Tech: Home</title>
</%def>

 <%def name="body()">
		<div id="home-topper" class="container">
	
		<div class="row">
		
			<div id="topper" class="twelve columns">
			
				<span><strong>The next great tech city</strong> is seeking <strong>the next great tech talent</strong>... <em>is that you</em>?</span>
			
			</div> 		
		</div> 	
	</div> 	
					
		<div id="main" class="container">
	
		<div class="row">
		
						<div id="jobs" class="eight columns">
			
				
<div class="panel">
<div id="list-filter-box" class="hide-on-phones">

	<div id="list-filters">
		
		<form name="filter-jobs" id="filter-jobs-form" class="nice" method="get" action="">
	
			<dl class="sub-nav">
			
				<dt>Filter:</dt>
				
				<dd class="active"><a href="http://hirevegastech.com/?filter=all" class="current">All</a></dd>
				
				<dd><a href="http://hirevegastech.com/?filter=design">Design</a></dd>
				
				<dd><a href="http://hirevegastech.com/?filter=programming">Programming</a></dd>
				
				<dd><a href="http://hirevegastech.com/?filter=information-tech">I.T.</a></dd>
				
				<dd><a href="http://hirevegastech.com/?filter=engineering">Engineering</a></dd>
				
				<dd><a href="http://hirevegastech.com/?filter=other">Other</a></dd>

				<!-- <dd id="search-jobs"><input type="text" class="small input-text" name="search" placeholder="Search jobs" id="search-jobs-input"></dd> -->
				
			</dl>
		
		</form>
	
	</div> 	
</div> 
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
				
					<p>Want to see your company logo or advertisement here? <a href="mailto:info@hirevegastech.com" title="Email info@hirevegastech.com">Email us</a>.</p>
				
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
						
						<li><a href="/user/logout" title="Logout">Logout</a></li>
%else:										
						<li><a href="/users" title="User Section">Users</a></li>
					
						<li><a href="#" title="User Login" id="navbar-login-btn" data-reveal-id="login-modal" data-animation="fade" class="small button nice radius blue">Login</a></li>
%endif	
 </%def>

