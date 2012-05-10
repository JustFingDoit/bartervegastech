# -*- coding: utf-8 -*- 
<!DOCTYPE html>  
<html class=" js no-touch no-ie8compat" lang="en"><!--<![endif]-->
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width">
	<link href="http://BarterVegasTech.com/favicon.ico" rel="shortcut icon" type="image/x-icon">

		<link rel="author" href="http://BarterVegasTech.com/humans.txt">
		
${self.head_tags()}
    
	<meta name="description" content="Jobs for programmers, designers, developers, artists, and web or IT professionals in Las Vegas, Nevada. Supporting #VegasTech!">
	<meta name="keywords" content="jobs, vegas, las vegas, hire, vegastech, search, programmers, designers, job board, developer, employment, startup, start up, job, job search, career, tech jobs">

		<link rel="stylesheet" href="/css/foundation.css">
	<link rel="stylesheet" href="/css/app.css">
	<!--[if lt IE 9]>
		<link rel="stylesheet" href="/stylesheets/ie.css">
	<![endif]-->
	<link rel="stylesheet" href="/css/main.css">
	<link rel="stylesheet" href="/css/css.css" type="text/css">
	
		<script src="/js/jquery-1.js"></script>
	<!--[if lt IE 9]>
		<script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
	<![endif]-->
    
</head>

<body>
<!-- Begin Main Body Wrapper -->

  ${self.header()}
  <!-- Begin content.wrapper -->

    ${self.body()}
  <!-- End content.wrapper -->

  <div class="container">
  ${self.footer()}
  </div>
<!-- End Main Body Wrapper -->


<div id="nav-modal" class="reveal-modal">

	<h3>Navigation</h3>
	
	<dl class="nice tabs vertical">
	
		<dd><a href="/" title="Home">Home</a></dd>
		
		<dd><a href="/about" title="About">About</a></dd>
		
				
			<dd><a href="/users" title="users">Members</a></dd>
			
			<dd><a href="#" id="modal-login-link" title="Login">Login</a></dd>
			
				
	</dl>
	
	<a class="close-reveal-modal">×</a>
	
</div> 
<div id="login-modal" class="reveal-modal">

	
	<h3>Login</h3>
	
	<span class="white round label">Login is for <em>everyone</em>!</span>
	
	<form name="login" id="login-form" method="post" action="/user/login" class="nice">
		
		<div id="login-form-container">
		
			<label for="login-email">Username</label>
			<input name="username" id="login-email" class="expand input-text" placeholder="tickles" required="required" maxlength="50" type="text">
						
			<label for="login-password">Password</label>
			<input name="password" id="login-password" class="expand input-text" placeholder="Your password" required="required" maxlength="50" type="password">
						
			<div id="login-form-submit">
			
				<button type="submit" title="Login" id="login-submit" name="loginsubmit" class="small blue nice radius button">Login</button>
			
			</div> 			
			<a href="/users#signup" title="Sign up for free">Sign up</a> | <a href="#" onclick="$('#login-form-container').hide(); $('#login-form-pass-recover').show();" title="Forgot your password?">Forgot your password?</a>
		
		</div> 		
		<div id="login-form-pass-recover">
		
			<p>Forgot your password? Please enter the email address associated 
with your account in the input below and we'll email you a 
password-reset link.</p>
			
			<label for="pw-recover-email">Email address</label>
			<input name="pw-recover-email" id="pw-recover-email" class="expand input-text" placeholder="name@example.com" maxlength="50" type="email">
			
			<div id="pw-recover-form-submit">
			
				<button type="submit" title="Send password recovery link" id="pw-recover-submit" name="pw-recover-submit" class="small blue nice radius button">Submit</button>
			
			</div> 			
			<a href="#" title="Back to login form" onclick="$('#login-form-pass-recover').hide(); $('#login-form-container').show();">Login Form</a>
		
		</div> 	
	</form>
	
	<a class="close-reveal-modal" id="close-login-modal-reveal">×</a>

</div> 

<script src="/js/modernizr.js"></script>­<style>@media (touch-enabled),(-webkit-touch-enabled),(-moz-touch-enabled),(-o-touch-enabled),(-ms-touch-enabled),(modernizr){#touch{top:9px;position:absolute}}</style>
<script src="/js/foundation.js"></script>
<script src="/js/app.js"></script>
<script>
$(function(){
	$('#modal-login-link').click(function(e){
		e.preventDefault();
		$('#nav-modal').trigger('reveal:close');
		$('#login-modal').reveal({
			animation: 'fade'
		});
	});
	$('#close-login-modal-reveal').click(function(e){
		e.preventDefault();
		$('#login-modal').trigger('reveal:close');
	});
});
</script>




</body>

</html>

<%def name="head_tags()">
<!-- Dummy head tags method -->
</%def>


<%def name="header()">

<a name="top"></a>
<div id="navbar" class="container">

	<div class="row">
	
			<div id="navbar-logo" class="four columns">
			
				<a href="#" id="nav-mobile-btn" data-reveal-id="nav-modal" data-animation="fade" class="small nice radius blue button show-on-phones">Nav</a>
			
				<a href="/" title="Home Page"><img src="/images/barter-vegas-tech-logo.png" alt="Hire #VegasTech Logo" title="Home" id="logo" class="hide-on-phones"><img src="/images/barter-vegas-tech-logo.png" alt="Hire #VegasTech Logo" title="Home" id="logo-mobile" class="show-on-phones"></a>
				
			</div> 			
			<div id="navbar-links" class="eight columns hide-on-phones">
			
				<ul>
				
                ${self.navlinks()}
						
									
				</ul>
				
			</div> 	
	</div> 	
</div> 

</%def>



<%def name="footer()">
	<footer class="row">
	
		<div id="footer-left" class="three columns hide-on-phones">
		
			<span id="copyright">A <a href="http://justfingdo.it/" title="Just F'ing Do it">Just F'ing Do It</a> Production</span>
			
			<br>
			
			<span id="created-by">Designed by <a href="http://twitter.com/GeoffSanders" class="has-tip tip-top" data-width="180" title="Follow Geoff on Twitter" target="_blank">@GeoffSanders</a></span>
			<span id="created-by">Coded by <a href="http://twitter.com/jchysk" class="has-tip tip-top" data-width="180" title="Follow Yo Sub on Twitter" target="_blank">@jchysk</a></span>
		
		</div> 		
		<div id="footer-center" class="six columns hide-on-phones">
		
			<ul>
				
				<li><a href="/" title="Home">Home</a></li>
				
				<li><a href="/about" title="About Barter #VegasTech">About</a></li>
%if request.session.get('logged_in') != None and request.session.get('logged_in') >= 0:

					<li><a href="/account" title="User Section">Account</a></li>
					
					<li><a href="/user/logout" title="Logout">Logout</a></li>

%else:				
								
					<li><a href="/users" title="User Section">Users</a></li>
					
					<li><a href="#" data-reveal-id="login-modal" data-animation="fade" title="Contact Us">Login</a></li>
%endif					
								
			</ul>
		
		</div> 		
		<div id="footer-right" class="three columns hide-on-phones">
		
			<a href="/" title="Home"><img src="/images/barter-vegas-tech-logo.png" alt="Hire #VegasTech Logo" id="footer-logo"></a>
			
			<div id="footer-support-logos">
			
				<span id="footer-humanstxt"><a href="/humans.txt" title="View our Humans.txt file" target="_blank"></a></span>
				
				<span id="footer-html5"><a href="http://www.w3.org/html/logo/" title="Support &amp; Spread HTML5" target="_blank"></a></span>
			
			</div> 		
		</div> 		
				<div id="footer-mobile" class="show-on-phones">
		
			<a href="#" id="nav-mobile-btn-footer" data-reveal-id="nav-modal" class="small nice radius blue button">Nav</a>
			
			<br>
		
			<a href="/" title="Home"><img src="/images/barter-vegas-tech-logo.png" alt="Hire #VegasTech Logo" id="footer-logo-mobile"></a>
			
			<br>
			
			<span id="copyright-mobile">©2012 <a href="http://bartervegastech.com/" title="BarterVegasTech.com">BarterVegasTech.com</a></span>
			
			<br>
			
			<span id="created-by-mobile">Created by <a href="http://twitter.com/GeoffSanders" title="Follow Geoff on Twitter" target="_blank">@GeoffSanders</a></span>
			
			<br>
			
			<a href="#top" id="footer-mobile-top-btn" class="small nice radius white button">Top</a>
		
		
		</div> 	
	</footer> 

</%def>

