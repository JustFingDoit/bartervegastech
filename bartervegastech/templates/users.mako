# -*- coding: utf-8 -*- 
<%inherit file="base.mako"/>
<%def name="head_tags()">
    <title>Barter Vegas Tech: Users</title>
</%def>

 <%def name="body()">

		<div id="users-topper" class="container">
	
		<div class="row">
		
			<div id="users-feature" class="eleven columns hide-on-phones">
			
				<span id="users-feature-line" class="hide-on-phones"><strong>Hire</strong> designers, programmers, engineers, internet technology pros, web developers, UI/UX designers, graphic artists, and other <a href="https://twitter.com/#%21/search/%23VegasTech" id="vt-hash-link-users" class="has-tip tip-top" data-width="180" title="Follow the #VegasTech hashtag on Twitter" target="_blank">#VegasTech</a> talent! It's <strong class="blue">easy</strong> and <strong class="red">free</strong>!</span>
			
			</div> 			
			<div id="users-feature-mobile" class="eleven columns show-on-phones">
			
				<span id="users-feature-line-mobile" class="show-on-phones hide-on-desktops"><strong>Hire</strong> designers, programmers, engineers, internet technology pros, web developers, UI/UX designers, graphic artists, and other <a style="" href="https://twitter.com/#%21/search/%23VegasTech" id="vt-hash-link-users" class="has-tip tip-top" data-width="180" title="Follow the #VegasTech hashtag on Twitter" target="_blank">#VegasTech</a> talent! It's <strong class="blue">easy</strong> and <strong class="red">free</strong>!</span>
				
			</div>
			
			<div class="one columns">
			
				&nbsp;
			
			</div> 		
		</div> 	
	</div> 	
				
		<div id="main" class="container">
	
		<div class="row">
		
						<div id="users-reasons" class="eight columns">
			
				<div class="panel">
				
					<h3>3 reasons to post your job on Hire#VegasTech</h3>
					
					<ul>
					
						<li class="heart-icon">
						
							<h5>Help support the #VegasTech movement</h5>
							
							<p>The #VegasTech community is a collaborative group that 
supports each other and is committed to developing a vibrant technology 
and startup community in Las Vegas. By posting here, you're helping us 
turn Las Vegas into <a href="http://downtownproject.com/" title="See how the CEO of Zappos is transforming Las Vegas" target="_blank" id="tip-zappos" class="has-tip tip-top" data-width="200">the next technology hub</a>.</p>
						
						</li>
						
						<li class="baby-icon">
						
							<h5>Posting a job doesn't get easier than this</h5>
							
							<p>We made it quick and easy - just register your company or 
startup once and post up to 25 job openings at a time. They stay active 
for 45 days and can be deactivated whenever you want.</p>
						
						</li>
						
						<li class="piggybank-icon">
						
							<h5>Did we mention it was free?</h5>
							
							<p>Some job boards charge up to $200 for a single post! Need we say more?</p>
						
						</li>
					
					</ul>
				
				</div> 			
			</div> 			
						<a name="signup"></a>
			<div id="users-signup" class="four columns">
			
				<div class="panel">
			
					<a href="#" title="Already a member? Login" id="signup-login" data-reveal-id="login-modal" data-animation="fade" class="nice small button white radius">Login</a>
				
					<h2><strong class="blue">Pain-free</strong> <strong class="red">sign up</strong></h2>
					<p><em>All fields required</em>. A confirmation email will be sent to the email you provide below.</p>
					
					<div id="user-signup-form">
					
						${signupform | n}
					
					</div> 				
				</div> 			
			</div> 		
		</div> 	
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


 </%def>
 

 <%def name="navlinks()">
 					<li><a href="/" title="Home">Home</a></li>
					
					<li><a href="/about" title="About #VegasTech">About</a></li>
%if request.session.get('logged_in') != None and request.session.get('logged_in') >= 0:
										
						<li><a href="/account" title="Account" >Account</a></li>
						
						<li><a href="/user/logout" title="Logout">Logout</a></li>
%else:					
										
						<li><a href="/users" title="User Section" id="current">Users</a></li>
					
						<li><a href="#" title="User Login" id="navbar-login-btn" data-reveal-id="login-modal" data-animation="fade" class="small button nice radius blue">Login</a></li>
%endif
 </%def>

